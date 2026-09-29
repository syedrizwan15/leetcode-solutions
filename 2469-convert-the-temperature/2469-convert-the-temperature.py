class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        ans1=celsius+273.15
        ans2=(celsius*1.80)+ 32.00
        return [ans1,ans2]