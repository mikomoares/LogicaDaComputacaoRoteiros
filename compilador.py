from sys import argv

if __name__ == "__main__":

    digitList=[]
    temp=[]

    for char in argv[1]:
        if char.isdigit():
            temp.append(char);
        else:
            num=0
            for index, numero in enumerate(temp):
                num += int(numero)*10**(len(temp) - index - 1)
            if temp!=[]:
                digitList.append(num)
            if char == "+" or char == "-":
                digitList.append(char)
            temp = []
    if char.isdigit():
            num=0
            for index, numero in enumerate(temp):
                num += int(numero)*10**(len(temp) - index - 1)
            if temp!=[]:
                digitList.append(num)
            temp = []
    for i in range(0, len(digitList)):
        if len(digitList)<=2:
            break
        elif isinstance(digitList[0], str) or isinstance(digitList[2], str) or isinstance(digitList[1], int):
            print ("ERRO")
            quit()
        elif digitList[1] == "+":
            digitList[0] = digitList[0] + digitList[2]
            digitList.pop(1)
            digitList.pop(1)
        elif digitList[1] == "-":
            digitList[0] = digitList[0] - digitList[2]
            digitList.pop(1)
            digitList.pop(1)
    print (digitList[0])




