#hw5.py-due Oct 18 midnight

#5.25
def leap(y):
    if y%4==0 and y%100 !=0 or y%400==0:
        return True
    return False
#5.28
def geometric(ilst):
    for i in range(len(ilst)-1):
        if ilst[i]!=2*ilst[i-1]:
            return False
    return True

#5.34
def statement(tlst):
    w=[]
    d=[]
    totalT=[]
    for i in range(len(tlst)):
        if tlst[i]<0:
            w.append(tlst[i])
        if tlst[i]>0:
            d.append(tlst[i])
    dtotal=sum(d)
    totalT.append(dtotal)
    wtotal=sum(w)
    totalT.append(wtotal)
    return totalT

#5.35
def pixels(tdlst):
    #input the nonnegative 2d list
    #return whatever is >0
    posL=[]
    for l in tdlst:
        #(above)goes through each list item in the bigger overall list
        for i in l:#goes through each item in the individual smaller list
            if i>0:
                #count the positive shit
                #print(i)#see what items I am looking for
                posL.append(i)
    o=len(posL)
    return o
#5.36
'''
Implement function prime() that takes a positive integer as input and returns
True if it is a prime number and FAlse otherwise.
>>> prime(2)
True
>>> prime(17)
True
>>> prime(21)
False
'''
def prime(num):
    #find criteria to find prime numbers
    if num>1:
        #has to divide by itself and 1 only to be prime
        #assume num is prime until it isn't
        primeYN=True
        pp=num
        for num in range(2,pp):
            if pp%2==0 and pp%3==0:
                primeYN=False
        return primeYN


if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw5TEST.py'))
       
