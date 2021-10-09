r = 0
i = 0
c = 0
e = 0
a = 0
s = 0

print("您有一次去岛屿旅游半年的机会，请根据提示完成任务: ")
while True:
    print("请从以下关键词中选一个")
    print("逃离城市，格物穷理，财富地位，高雅情调，秩序社会，温情社会")
    choice = input("从左至右依次是a-f，请输入代号: ")
    if choice == "a":
        while True:
            print("你希望远离社会的喧嚣与纷扰吗？")
            answer1 = input("请输入y代表是，n代表不是: ")
            if answer1 == "y":
                r += 1
                break
            elif answer1 != "n":
                print("请输入正确内容！")
                continue
            else:
                break

        while True:
            print("你想尝试自己创造并掌握生活，丰衣足食嘛？")
            answer2 = input("请输入y代表是，n代表不是: ")
            if answer2 == "y":
                r += 1
                break
            elif answer2 != "n":
                print("请输入正确内容！")
                continue
            else:
                break

        while True:
            print("你想面朝大海，春暖花开逃避竞争与内卷吗")
            answer3 = input("请输入y代表是，n代表不是: ")
            if answer3 == "y":
                r += 1
                break
            elif answer3 != "n":
                print("请输入正确内容！")
                continue
            else:
                break

        if r >= 2:
            print("你将去R岛生活半年，旅途愉快！")
            break

        else:
            print("您不适合这里，请重新选择……")
            r = 0
            continue

    if choice == "b":
        while True:
            print("如果给你一个机会和你感兴趣的领域大牛一起参加沙龙你会去吗？")
            answer4 = input("请输入y代表去，n代表不去: ")
            if answer4 == "y":
                i += 1
                break
            elif answer4 != "n":
                print("请输入正确内容！")
                continue
            else:
                break

        while True:
            print("你欣赏朝闻道夕死可矣吗？")
            answer5 = input("请输入y代表欣赏，n代表不欣赏: ")
            if answer5 == "y":
                i += 1
                break
            elif answer5 != "n":
                print("请输入正确内容！")
                continue
            else:
                break

        while True:
            print("你喜欢长时间沉浸式思考一个问题吗？")
            answer6 = input("请输入y代表喜欢，n代表不喜欢: ")
            if answer6 == "y":
                i += 1
                break
            elif answer6 != "n":
                print("请输入正确内容！")
                continue
            else:
                break

        if i >= 2:
            print("你将去I岛生活半年，旅途愉快！")
            break

        else:
            print("您不适合这里，请重新选择……")
            i = 0
            continue

    if choice == "c":
        while True:
            print("你希望观察或是体验社会精英阶级（企业家、红圈律师等）的生活并学习吗？")
            answer7 = input("请输入y代表希望，n代表不希望。")
            if answer7 == "y":
                e += 1
                break
            elif answer7 != "n":
                print("请输入正确内容！")
                continue
            else:
                break

        while True:
            print("你想拥有高质量、上流而奢侈的生活吗？")
            answer8 = input("请输入y代表想，n代表不想: ")
            if answer8 == "y":
                e += 1
                break
            elif answer8 != "n":
                print("请输入正确内容！")
                continue
            else:
                break

        while True:
            print("你想有一颗发达的商业头脑并缔造一个商业帝国吗？")
            answer9 = input("请输入y代表想，n代表不想: ")
            if answer9 == "y":
                e += 1
                break
            elif answer9 != "n":
                print("请输入正确内容！")
                continue
            else:
                break

        if e >= 2:
            print("您将前往E岛进行为其半年的旅游，旅途愉快!")
            break
        else:
            print("您不适合这里，请重新选择……")
            e = 0
            continue

    if choice == "d":
        while True:
            print("如果你有机会去法国的一个地方旅游，你更想去卢浮宫还是埃菲尔铁塔？")
            answer10 = input("请输入y代表卢浮宫，n代表后者: ")
            if answer10 == "y":
                a += 1
                break
            elif answer10 != "n":
                print("请输入正确内容！")
                continue
            else:
                break

        while True:
            print("你想与富有文艺气息的人做朋友吗？")
            answer11 = input("请输入y代表想，n代表不想: ")
            if answer11 == "y":
                a += 1
                break
            elif answer11 != "n":
                print("请输入正确内容！")
                continue
            else:
                break

        while True:
            print("你喜欢莫扎特，柴可夫斯基之类的古典乐，"
                  "莫奈与达芬奇等大师的画作，胡桃夹子之类的芭蕾舞吗？")
            answer12 = input("请输入y代表喜欢，n代表不喜欢: ")
            if answer12 == "y":
                a += 1
                break
            elif answer12 != "n":
                print("请输入正确内容！")
                continue
            else:
                break

        if a >= 2:
            print("您将去A岛旅游半年，旅途愉快!")
            break
        else:
            print("您不适合这里，请重新选择……")
            a = 0
            continue

    if choice == "e" or choice == "f":
        if choice == "e":
            c += 2
        else:
            s += 2

        while True:
            print("你更想去国内的一个民风淳朴的乡村养老还是去北欧的福利政策完善的城市养老？")
            answer13 = input("请输入y代表前者，n代表后者: ")
            if answer13 == "y":
                s += 1
                break
            elif answer13 != "n":
                print("请输入正确内容！")
                continue
            else:
                c += 1
                break

        while True:
            print("你在高楼林立的钢铁城市中会感到孤独或难以呼吸吗？")
            answer14 = input("请输入y代表会，n代表不会: ")
            if answer14 == "y":
                s += 1
                break
            elif answer14 != "n":
                print("请输入正确内容！")
                continue
            else:
                c += 1
                break

        while True:
            print("你喜欢一个桃花源似的社会还是喜欢程式化般稳定但不重情的社会？")
            answer15 = input("请输入y代表前者，n代表后者: ")
            if answer15 == "y":
                s += 1
                break
            elif answer15 != "n":
                print("请输入正确内容！")
                continue
            else:
                c += 1
                break

        result = "您将去S岛旅游半年，旅途愉快!" if s > c else "您将去C岛旅游半年，旅途愉快!"
        print(result)
        break

    else:
        print("请输入正确内容!")
        c = 0
        s = 0
        continue

input("请敲击回车以退出")