def isType(x):
    """判断输入参数的数据类型，返回中文字符串"""
    # 先处理布尔型（它是 int 的子类，但语义不同，此处归为整数）
    if type(x) is bool:
        return "整数"

    type_map = {
        int: "整数",
        float: "小数",
        complex: "复数",
        str: "字符串",
        list: "列表",
        dict: "字典",
        set: "集合",
        tuple: "元组"
    }
    return type_map.get(type(x), "未知类型")
f=eval(input("请输入参数"))
print(isType(f))