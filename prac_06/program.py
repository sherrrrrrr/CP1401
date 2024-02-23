def get_valid_number(prompt, low, high):
    """
    获取一个在指定范围内的有效数值。
    """
    while True:
        try:
            number = float(input(prompt))
            if low <= number <= high:
                return number
            else:
                print(f"请输入一个在 {low} 和 {high} 之间的数值。")
        except ValueError:
            print("无效输入，请输入一个数字。")

def calculate_bmi(height, weight):
    """
    根据身高和体重计算 BMI。
    """
    return weight / (height ** 2)

def determine_weight_category(bmi):
    """
    根据 BMI 值确定体重类别。
    """
    if bmi < 18.5:
        return "体重不足"
    elif bmi < 25:
        return "正常体重"
    elif bmi < 30:
        return "超重"
    else:
        return "肥胖"

def main():
    """
    主程序：获取用户身高和体重，计算并输出 BMI 及其类别。
    """
    height = get_valid_number("请输入身高（米）: ", 0, 3)
    weight = get_valid_number("请输入体重（千克）: ", 0, 300)
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    print(f"您的 BMI 是 {bmi:.1f}，属于{category}类别。")

if __name__ == "__main__":
    main()
