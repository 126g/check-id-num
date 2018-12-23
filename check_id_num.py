def check_id_num(id_num):
    # 首先检查长度是否为18位
    if len(id_num) != 18:
        return False

    p = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 加权因子
    c = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']  # 校验码

    id = id_num[:17]  # 前17位为本体码
    code = id_num[-1:]  # 最后一位为校验码

    sum = 0
    for i in range(len(id)):
        sum += (p[i] * int(id[i]))
    sum %= 11

    if code.upper() == c[sum]:
        return True
    else:
        return False


def main():
    with open('sfzh.txt', 'r') as f:
        while True:
            id_num = f.readline().strip()

            if not id_num:
                break

            if not check_id_num(id_num):
                print("Error:", id_num)


if __name__ == '__main__':
    main()
