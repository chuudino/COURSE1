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
