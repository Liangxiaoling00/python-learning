class Calculator:
    """简易计算器类"""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b

    @classmethod
    def evaluate(cls, expr):
        """
        类方法，接收字符串数学表达式，如 "3+5", "10 / 2"
        返回计算结果（浮点数或整数）
        """
        # 去除首尾空格，按运算符分割
        expr = expr.strip()
        # 支持的运算符
        for op in ['+', '-', '*', '/']:
            if op in expr:
                # 按运算符分割，注意可能包含空格
                parts = expr.split(op)
                if len(parts) != 2:
                    raise ValueError("表达式格式错误")
                a_str, b_str = parts[0].strip(), parts[1].strip()
                try:
                    a = float(a_str)
                    b = float(b_str)
                except ValueError:
                    raise ValueError("操作数不是有效的数字")
                # 创建临时实例来调用实例方法
                calc = cls()
                if op == '+':
                    result = calc.add(a, b)
                elif op == '-':
                    result = calc.subtract(a, b)
                elif op == '*':
                    result = calc.multiply(a, b)
                elif op == '/':
                    result = calc.divide(a, b)
                # 如果结果本应是整数则转为整数
                if result == int(result):
                    return int(result)
                else:
                    return result
        # 如果没有找到运算符
        raise ValueError("表达式中未找到支持的运算符 (+, -, *, /)")

# ---------- 测试代码 ----------
if __name__ == "__main__":
    # 测试实例方法
    calc = Calculator()
    print(calc.add(3, 5))          # 8
    print(calc.subtract(10, 4))    # 6
    print(calc.multiply(3, 4))     # 12
    print(calc.divide(10, 3))      # 3.333...
    print(calc.divide(10, 2))      # 5.0 (但会保留浮点)

    # 测试类方法
    print(Calculator.evaluate("3+5"))        # 8
    print(Calculator.evaluate("10 - 4"))     # 6
    print(Calculator.evaluate("3 * 4"))      # 12
    print(Calculator.evaluate("10 / 3"))     # 3.333...
    print(Calculator.evaluate("10 / 2"))     # 5 (整数)
    # 异常测试
    # print(Calculator.evaluate("10 / 0"))  # 抛出异常
