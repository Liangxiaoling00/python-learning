class Temperature:
    def __init__(self, degree):
        self.degree = degree

    def ToFahrenheit(self):
        """将 degree 视为摄氏温度，返回华氏温度"""
        return self.degree * 9 / 5 + 32

    def ToCelsius(self):
        """将 degree 视为华氏温度，返回摄氏温度"""
        return (self.degree - 32) * 5 / 9

# ------ 测试代码 ------
# 测试摄氏转华氏
t1 = Temperature(100)          # 摄氏100度
print(f"摄氏 {t1.degree}°C = {t1.ToFahrenheit():.1f}°F")   # 输出 212.0°F

# 测试华氏转摄氏
t2 = Temperature(212)          # 华氏212度
print(f"华氏 {t2.degree}°F = {t2.ToCelsius():.1f}°C")     # 输出 100.0°C




#另一种可交互代码

class Temperature:
    def __init__(self, degree):
        self.degree = degree

    def to_fahrenheit(self):
        return self.degree * 9 / 5 + 32

    def to_celsius(self):
        return (self.degree - 32) * 5 / 9

def main():
    print("温度转换程序（输入 q 退出）")
    while True:
        inp = input("请输入温度（如 100C 或 212F）：").strip()
        if inp.lower() == 'q':
            break
        if len(inp) == 0:
            continue
        unit = inp[-1].upper()
        value_str = inp[:-1]
        try:
            value = float(value_str)
        except ValueError:
            print("输入格式错误，请重新输入")
            continue

        temp = Temperature(value)
        if unit == 'C':
            result = temp.to_fahrenheit()
            print(f"{value}°C = {result:.1f}°F")
        elif unit == 'F':
            result = temp.to_celsius()
            print(f"{value}°F = {result:.1f}°C")
        else:
            print("单位只能是 C 或 F，请重新输入")

if __name__ == "__main__":
    main()