

def findZeroes(arr, n, m) :
    # code here
    """
    count = 0
    maxCount = 0
    index = 0
    jj = m
    lastIndex = 0
    countOfZeroes = arr.count(0)

    if m >= countOfZeroes:
        # turn all 0s to 1s, m is greater
        return n
    while(index<n):
        # entry is 1
        if arr[index]:
            count += 1
        # entry is 0
        else:
            if jj:
                count += 1
                lastIndex = index
                jj -= 1
            else:
                if countOfZeroes:
                    # {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
                    # if m=0 but numberofZeroes still exists:
                    # get the 1s from last index --> to current index
                    jj = m
                    if jj:
                        count = index - lastIndex
                        lastIndex = index
                        jj -= 1
                    else:
                        count = 0
                        
            countOfZeroes -= 1
        
        if count > maxCount:
            maxCount = count
        index = index+1
    return maxCount
    """

    cnt0 = 0
    l = 0
    max_len = 0;
 
    # i decides current ending point
    for i in range(0, n):
        if arr[i] == 0:
            cnt0 += 1
 
        # If there are more 0's move
        # left point for current
        # ending point.
        while (cnt0 > m):
            if arr[l] == 0:
                cnt0 -= 1
            l += 1
         
 
        max_len = max(max_len, i - l + 1);
     
 
    return max_len    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__":         
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends