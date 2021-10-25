#User function Template for python3

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        #CODE HERE
        self.s.append(x)

    def pop(self):
        #CODE HERE
        try:
            a = self.s[-1]
            self.s.remove(self.s[-1])
            return a
        except Exception:
            return -1
            

    def getMin(self):
        #CODE HERE
        try:
            asd = self.s
            small = asd[0]
            for ele in range(1, len(asd)):
                if small > asd[ele]:
                    small = asd[ele]
            self.minEle = small
            return self.minEle
        except Exception:
            return -1        

#{ 
#  Driver Code Starts
#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# } Driver Code Ends