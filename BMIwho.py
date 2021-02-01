print ("="*15 + "标准体重" + "="*15)
while True:
    h = input("身高(cm)：")
    while True:
        try:
            h = float(h)
            break
        except:
            h = input("请输入数字！身高(cm):")
    sex = input("性别（w/m）：")
    while True:
        if sex == ("m") or sex == ("M"):
            sw = ((float(h) - 80)*0.7)
            break
        if sex == ("w") or sex == ("W"):   
            sw = ((float(h) - 70)*0.6)
            break
        else:
            sex = input("请输入数字！性别（w/m）：")
    rw = input ("体重(KG):")
    while True:
        try:
            rw = float(rw)
            break
        except:
            rw = input("请输入数字！体重(KG):")    
    if float(rw) >= float(sw):
        BMI = ((float(rw) - float(sw)) / float(sw) )
        if 0<= float(BMI) <=0.1:
            print("正常")
        elif 0.1 < float(BMI) <= 0:
            print("过重")
        elif float(BMI) >0.2:
            print("肥胖")
    if float(rw) < float(sw):
        BMI = ((float(sw) - float(rw)) / float(sw) )
        if 0<= float(BMI) <=0.1:
            print("正常")
        elif 0.1 < float(BMI) <= 0.2:
            print("过轻")
        elif float(BMI) >0.2:
            print("体重不足")
    Again = input("Again?(Y/N):")
    if Again != ("Y") and Again != ("y"):
	    break
print ("感谢使用")

