for _ in range(int(input())):
    N = int(input())
    Path = input()
    MyPath = ""
    for i in Path: 
        if i=="S": MyPath+="E"
        else: MyPath+="S"
    print("Case #"+str(_+1)+ ": "+MyPath)