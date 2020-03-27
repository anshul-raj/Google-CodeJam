from math import gcd

for _ in range(int(input())):
    N,L = map(int,input().split())
    array = list(map(int,input().split()))
    
    x=array[0]
    y=0
    temp = 0
    primes = []
    for i in array:
        if x!=i:
            if temp%2==0:
                primes.append(gcd(i,x))
            else:
                primes.append(x//gcd(i,x))
            break
        temp+=1
    
    temp = primes[0]
    
    dicti = {primes[0]:0}

    PrimesUsed = [primes[0]]

    for i in array:
        temp = i//temp
        primes.append(temp)
        if temp not in dicti:
            dicti[temp] = 0
            PrimesUsed.append(temp)
        
    PrimesUsed.sort()

    for i in range(len(PrimesUsed)):
        dicti[PrimesUsed[i]] = chr(i+65)
        
    ans = ""
    
    for i in primes:
        ans+=dicti[i]
    
    print("Case #"+str(_+1)+":",ans)