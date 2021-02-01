print("="*15+"YOUR BMI"+"="*15)
while True:
    W = input("体重(KG):")
    while True:
        try:
            W=float(W)
            break
        except:
            W = input("请输入数字！体重(KG):")
    H = input("身高(cm):")
    while True:
        try:
            H=float(H)
            break
        except:
            H = input("请输入数字！身高(cm):")
    SEX = input("性别(m/w):")
    BMI = float(W) / (float(H)/100)**2
    if float(BMI) <= 18.5:size =("偏瘦");
    elif 18.5 < float(BMI) <= 23.9:size =("正常");
    elif 23.9 < float(BMI) <= 27.9:size =("超重");
    elif float(BMI) > 27.9:size =("肥胖")
    print("="*34)
    if SEX.upper() == ("M"):
        n = ("先生")
    elif SEX.upper() == ("W"):
            n = ("女士")
    else:
        print("请正确输入您的性别");
        n = ("???")
    print ("="*15 +"List" + "="*15)
    print ("亲爱的"+ n)
    print("您的测试结果为:" )
    print(BMI)
    print(size)
    Again = input("Again?(Y/N):")
    if Again != ("Y") and Again != ("y"):break
print ("感谢使用")
