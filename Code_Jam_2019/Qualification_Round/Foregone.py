for _ in range(int(input())):
    N = input()
    x = int(N)
    y = 0
    for i in range(len(N)):
        if N[i]=='4':
            x-=int('2'+'0'*(len(N)-i-1))
            y+=int('2'+'0'*(len(N)-i-1))
    print("Case #"+str(_+1)+":"+" "+str(x)+" "+str(y))