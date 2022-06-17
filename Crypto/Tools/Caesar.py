import os

# ============================================================================ #
#                               Caesar Cipher                                  #
#         凯撒密码是一种最简单且最广为人知的加密技术，是一种替换加密技术，           #
#  明文中的所有字母都在字母表上向後(或向前)按照一个固定数目进行偏移後被替换成密文     #
# ============================================================================ #

# 加密
def encryption():
    str_raw = input("请输入明文：")
    k = int(input("请输入位移值："))
    # 转化为小写
    str_change = str_raw.lower()
    # 转化为列表
    str_list = list(str_change)
    # 赋值
    str_list_encry = str_list
    i = 0
    while i < len(str_list):
        # 如果不是字母 不参与偏移
        if 97 <= ord(str_list[i]) <= 122:
            # 如果没有超过一轮26个英文字母，直接累加
            if ord(str_list[i]) < 123-k:
                str_list_encry[i] = chr(ord(str_list[i]) + k)
            # 超过一轮26个英文字母，累加后要反减26
            else:
                str_list_encry[i] = chr(ord(str_list[i]) + k - 26)
        i = i+1
    print ("加密结果为："+"".join(str_list_encry))

# 解密
def decryption():
    str_raw = input("请输入密文：")
    k = int(input("请输入位移值："))
    # 转化为小写
    str_change = str_raw.lower()
    # 转化为列表
    str_list = list(str_change)
    # 赋值
    str_list_decry = str_list
    i = 0
    while i < len(str_list):
        # 如果不是字母 不参与偏移
        if 97 <= ord(str_list[i]) <= 122:
            # 如果没有超过一轮26个英文字母，直接累加
            if ord(str_list[i]) >= 97 + k:
                str_list_decry[i] = chr(ord(str_list[i]) - k)
            # 超过一轮26个英文字母，累加后要反加26
            else:
                str_list_decry[i] = chr(ord(str_list[i]) + 26 - k)
        i = i + 1
    print ("解密结果为："+"".join(str_list_decry))

# 自解密
def auto_decryption():
    str_raw = input("请输入密文：")
    # 关键字CTF flag 可能出现的字段
    keyword = ["flag","cfg","FLAG","CTF"]
    str_list_decry = ""
    for i in range(0,26):
        k = i
        # 转化为小写
        str_change = str_raw.lower()
        # 转化为列表
        str_list = list(str_change)
        # 赋值
        str_list_decry = str_list
        j = 0
        while j < len(str_list):
            # 如果不是字母 不参与偏移
            if 97 <= ord(str_list[j]) <= 122:
                # 如果没有超过一轮26个英文字母，直接累加
                if ord(str_list[j]) >= 97 + k:
                    str_list_decry[j] = chr(ord(str_list[j]) - k)
                # 超过一轮26个英文字母，累加后要反加26
                else:
                    str_list_decry[j] = chr(ord(str_list[j]) + 26 - k)
            j = j + 1
        str_maybe = ''.join(str_list_decry)
        # 遍历关键字，看是否存在
        for w in keyword:
            if str_maybe.find(w) == 0:
                # print ("解密结果可能为：" + str + "偏移量：" + str(i))
                print("解密结果可能为：" + str_maybe + "\t\t偏移量：" + str(i))

    
# 程序入口
if __name__=='__main__':
    while True:
        print (u"1. 加密")
        print (u"2. 解密")
        print (u"3. 自解密")
        choice = input("请选择：")
        if choice == "1":
            encryption()
        elif choice == "2":
            decryption()
        elif choice == "3":
            auto_decryption()
        else:
            print (u"您的输入有误！")