#There Might(Will) Be Better Version Than Mine
while True:
    a = int(input("Enter The First Number: "))
    b = int(input("Enter The Second Number: "))
    l1 = [] # creating an empty list to append factors of 'a' later
    x = 2

    if a == b: # if a is equal to b
        print("The H.C.F of",a,"and",b,"is",a)
        print("The L.C.M of",a,"and",b,"is",b)

    if a !=b : # if a is not equal to b
        while x<a:
            f = a/x
            i = int(f)
            if f==i:
                l1.append(x)   
            x = x+1 

        x = 2 # resetting value of x to redo for b
        l2 = [] # creating an empty list to append factors of 'n' later
        while x<a:
            f = b/x
            i = int(f)
            if f==i:
                l2.append(x)  
            x = x+1
        l1.extend(l2)

        x=2
        l = []
        while x<b:
            if l1.count(x)>=2:
                l.append(x)
            x = x+1
        hcf = l  

        if len(hcf)==0: #for Primes
            print("The H.C.F of",a,"and",b,"is",1,"(As They Are Co-Prime)")
            print("The L.C.M of",a,"and",b,"is",a*b)
        else:
            hcf = l[-1]
            print("The H.C.F of",a,"and",b,"is",hcf)
            lcm = int((a*b)/hcf)
            print("The L.C.M of",a,"and",b,"is",lcm)  
    print()
    #There Might(Will) Be Better Version Than Mine
