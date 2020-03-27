for _ in range(int(input())):
    N,K,P = map(int,input().split())

    teststring1 = ''
    teststring2 = ''
    teststring3 = ''
    teststring4 = ''
    
    for i in range(int(N)):
        s = bin(i%16)[2:]
        s = (4-len(s))*'0' + s
        teststring1 += s[3]
        teststring2 += s[2]
        teststring3 += s[1]
        teststring4 += s[0]
    
    print(teststring1,flush = True)
    response1 = input()
    print(teststring2,flush = True)
    response2 = input()
    print(teststring3,flush = True)
    response3 = input()
    print(teststring4,flush = True)
    response4 = input()

    array = []
    j=0
    for i in range(N):
        resp = response4[j]+response3[j]+response2[j]+response1[j]
        tester = bin(i%16)[2:]
        tester = (4-len(tester))*'0' + tester
        if resp == tester:
            j+=1
            if j>=len(response1):
                for p in range(i+1,N):array.append(str(p))
                break
        else:
            array.append(str(i))
    assert len(array)==K 
    print(*array,flush = True)
    input()