class gpio:
    """
    希望使用者直接呼叫 gpio.D0 就可以找到對應編號的pin腳位
    但是這樣有可能 pin 腳位會被使用者改寫
    比如說 gpio.D0 = 1 但實際上是 gpio.D0 = 16
    所以這邊使用 property 來保護
    首先可以先把 D0~D8 的名稱都改成不容易被使用者使用的名稱
    這時候可以新增 def 來重新取名稱讓使用者可以繼續依照原本的習慣使用
    但是只宣告 def D0 的話使用者用起來會像這樣 gpio.D0()
    接著我們可以使用 property 來讓使用者可以直接使用 gpio.D0
    這樣就可以達到我們的目的了
    """

    def __init__(self):
        self._D0 = 16
        self._D1 = 5
        self._D2 = 4
        self._D3 = 0
        self._D4 = 2
        self._D5 = 14
        self._D6 = 12
        self._D7 = 13
        self._D8 = 15
        self._SDD3 = 10
        self._SDD2 = 9

    @property
    def D0(self):
        return self._D0

    @property
    def D1(self):
        return self._D1

    @property
    def D2(self):
        return self._D2

    @property
    def D3(self):
        return self._D3

    @property
    def D4(self):
        return self._D4

    @property
    def D5(self):
        return self._D5

    @property
    def D6(self):
        return self._D6

    @property
    def D7(self):
        return self._D7

    @property
    def D8(self):
        return self._D8

    @property
    def SDD3(self):
        return self._SDD3

    @property
    def SDD2(self):
        return self._SDD2


class led:
    """RGB 三色燈控制（支援 PWM 亮度/非 PWM 開關）。

    初始化由 main.py 傳入參數：
      - r_pin, g_pin, b_pin: RGB 三色腳位（可直接傳 gpio().D4 等）
      - pwm: 是否啟用 PWM

    亮度範圍規則（由 pwm 決定）：
      - pwm=False:每色 brightness 只能是 0/1 (關/開）
      - pwm=True :每色 brightness 必須是 0..1023 (duty)

        led_open(r, g, b)：分別控制 RGB 三色亮度/開關。
    """

    def __init__(self, r_pin, g_pin, b_pin, pwm=False):
        from machine import Pin

        self.r_pin = r_pin
        self.g_pin = g_pin
        self.b_pin = b_pin
        self.pwm_enabled = bool(pwm)
        self.freq = 1000

        if self.pwm_enabled:
            from machine import PWM

            self._r = PWM(Pin(self.r_pin), freq=self.freq, duty=0)
            self._g = PWM(Pin(self.g_pin), freq=self.freq, duty=0)
            self._b = PWM(Pin(self.b_pin), freq=self.freq, duty=0)

        else:
            self._r = Pin(self.r_pin, Pin.OUT, value=0)
            self._g = Pin(self.g_pin, Pin.OUT, value=0)
            self._b = Pin(self.b_pin, Pin.OUT, value=0)

    def led_open(self, r=1, g=1, b=1):
        """設定 RGB 三色燈亮度/開關。"""
        r = int(r)
        g = int(g)
        b = int(b)

        if self.pwm_enabled:
            r = max(0, min(1023, r))
            g = max(0, min(1023, g))
            b = max(0, min(1023, b))

            self._r.duty(r)
            self._g.duty(g)
            self._b.duty(b)
            return

        r = max(0, min(1, r))
        g = max(0, min(1, g))
        b = max(0, min(1, b))

        self._r.value(r)
        self._g.value(g)
        self._b.value(b)


class wifi:
    # wifi 類別：用來管理 WiFi 連線與設定
    def __init__(self, ssid=None, password=None):
        import network

        self.ssid = ssid  # WiFi 名稱
        self.password = password  # WiFi 密碼
        self.sta = network.WLAN(network.STA_IF)  # 建立 STA（連接無線網路）介面
        self.ap = network.WLAN(network.AP_IF)  # 建立 AP（無線基地台）介面
        self.ap_activate = False  # AP 模式啟用狀態
        self.sta_activate = False  # STA 模式啟用狀態
        self.ip = None  # IP 設定

    def setup(self, sta_activate=True, ap_activate=False):
        """
        setup(sta_activate=True, ap_activate=False)\n
        啟用或關閉 STA/AP 模式。\n
        參數：\n
          sta_activate (bool): 是否啟用 STA (連接無線網路）模式，預設 True。\n
          ap_activate (bool): 是否啟用 AP (無線基地台）模式，預設 False。\n
        用法範例：\n
          wifi1 = wifi()\n
          wifi1.setup(sta_activate=True, ap_activate=False)
        """
        # 啟用或關閉 STA/AP 模式
        self.sta.active(sta_activate)
        self.ap.active(ap_activate)
        self.sta_activate = sta_activate
        self.ap_activate = ap_activate

    def scan(self):
        """
        scan()\n
        掃描並列出附近可用的 WiFi 網路及其訊號強度。\n
        無參數。\n
        用法範例：\n
          wifi1 = wifi()\n
          wifi1.scan()
        """
        # 掃描附近的 WiFi 無線網路
        if not self.sta.active():
            self.sta.active(True)
        networks = self.sta.scan()
        print("Available networks:")
        for net in networks:
            print(f"SSID: {net[0].decode()}, Signal strength: {net[3]}%")

    def connect(self, ssid=None, password=None, timeout=15):
        """
        connect(ssid=None, password=None, timeout=15)\n
        連接到指定的 WiFi 無線網路。\n
        參數：\n
          ssid (str): WiFi 名稱，預設為初始化時設定的名稱。\n
          password (str): WiFi 密碼，預設為初始化時設定的密碼。\n
          timeout (int): 連線超時時間（秒），預設 15 秒。\n
        用法範例：\n
          wifi1 = wifi()\n
          wifi1.connect('MyWiFi', 'mypassword')
        """
        # 連接到指定的 WiFi 無線網路
        import time

        if ssid is not None:
            self.ssid = ssid
        if password is not None:
            self.password = password
        if not self.sta.active():
            self.sta.active(True)
        if not self.sta.isconnected():
            print(f"Connecting to {self.ssid}...")
            self.sta.connect(self.ssid, self.password)
            start_time = time.time()
            while not self.sta.isconnected():
                if time.time() - start_time > timeout:
                    print("Connection timeout! Failed to connect.")
                    return False
                time.sleep(1)
                print(".", end="")
            print()  # 換行
        self.ip = self.sta.ifconfig()
        print("Connected! IP:", self.ip[0])
        return True


class MQTT:
    def __init__(self, client_id, server, user=None, password=None, keepalive=60):
        from umqtt.simple import MQTTClient

        self.client = MQTTClient(
            client_id=client_id,
            server=server,
            user=user,
            password=password,
            keepalive=keepalive,
        )

    def connect(self):
        try:
            self.client.connect()
        except:
            import sys

            sys.exit()
        finally:
            print("Connected to MQTT broker")

    def subscribe(self, topic, callback):
        self.client.set_callback(callback)
        self.client.subscribe(topic)

    def check_msg(self):
        self.client.check_msg()
        self.client.ping()

    def publish(self, topic, msg):
        topic = topic.encode("utf-8")
        msg = msg.encode("utf-8")
        self.client.publish(topic, msg)


class MP3:
    def __init__(self):
        """
        初始化 MP3 播放模組。
        初始化由 main.py 傳入參數：
          - uart_port: UART 埠號，預設為 1。
          - baudrate: 通訊鮑率，預設為 9600。

        """
        from machine import UART

        self.uart = UART(1, baudrate=9600)
        self.uart.init(9600, bits=8, parity=None, stop=1)

    def start(self, volume=100, song=1):

        volume = int(hex(volume), 16)
        song = int(hex(song), 16)

        buf1 = bytearray(5)
        buf1[0] = 0xAA
        buf1[1] = 0x13
        buf1[2] = 0x01
        buf1[3] = volume
        buf1[4] = buf1[0] + buf1[1] + buf1[2] + buf1[3]
        self.uart.write(buf1)

        buf1 = bytearray(6)
        buf1[0] = 0xAA
        buf1[1] = 0x07
        buf1[2] = 0x02
        buf1[3] = 0x00
        buf1[4] = song
        buf1[5] = buf1[0] + buf1[1] + buf1[2] + buf1[3] + buf1[4]
        self.uart.write(buf1)

    def stop(self):
        buf1 = bytearray(4)
        buf1[0] = 0xAA
        buf1[1] = 0x04
        buf1[2] = 0x00
        buf1[3] = 0xAE
        self.uart.write(buf1)
