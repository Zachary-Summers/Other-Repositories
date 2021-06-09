import datetime, sys
p = 97
q = 71
n = p*q
e = 11
d = ((p-1)*(q-1)+1)/e
m=0
class encryptor:
    global n
    global d
    global e
    global m
    global p
    global q
    def __init__(self,m,n,d,e):
        self.m=m
        self.n=n
        self.d=d
        self.e=e
    def encrypt(self):
        return ((self.m**self.e)%self.n)
    def decrypt(self):
        answer= (((self.m**(int(self.d)))%self.n ))
        return answer
    def add(self):
        print("\033[1;31;48mDo not use. Still in progress.")
        sys.exit()
        self.add = 0
        for i in range(0,self.m):
            add=0
            if self.decrypt(self.encrypt(i)+add)!=i:
                add+=n
        return add
    def test(self):
        print("\033[1;31;48mDo not use. Still in progress.")
        sys.exit()
        ans =[]
        for i in range(0,self.n):
            ans.append((self.encrypt(i),i))
        return ans
    def random(self):
        rand = self.encrypt()
        return rand
def randPoint(x,y,val=1):
    xObj,yObj = encryptor(x,n,d,e),encryptor(y,n,d,e)
    xRand,yRand = xObj.random(),yObj.random()
    randMultiply = ((xRand+yRand)/2)/2887
    randPoint = val*randMultiply
    return randPoint
#encrypted point = ((((x**11)%6887)+((y**11)%6887))/2)*valueOfPoint
#decrypted point =encryptedPoint/((((x**11)%6887)+((y**11)%6887))/2