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
          sta_activate (bool): 是否啟用 STA（連接無線網路）模式，預設 True。\n
          ap_activate (bool): 是否啟用 AP（無線基地台）模式，預設 False。\n
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

    def connect(self, ssid=None, password=None):
        """
        connect(ssid=None, password=None)\n
        連接到指定的 WiFi 無線網路。\n
        參數：\n
          ssid (str): WiFi 名稱，預設為初始化時設定的名稱。\n
          password (str): WiFi 密碼，預設為初始化時設定的密碼。\n
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
            print("Connecting to network...")
            self.sta.connect(self.ssid, self.password)
            while not self.sta.isconnected():
                time.sleep(1)
        self.ip = self.sta.ifconfig()
        print("Network configuration:", self.ip)
