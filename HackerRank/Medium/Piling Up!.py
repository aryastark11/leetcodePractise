# Enter your code here. Read input from STDIN. Print output to STDOUT
T = list(map(int,input().split()))
while T[0] > 0:
    # refresh it for every testcase
    pile = [2147483648]    
    arr = []

    nums = list(map(int,input().split()))
    arr = list(map(int,input().split()))

    # sorted already
    i = 0
    j = nums[0]-1
    while(i != j):
        if arr[i] >= arr[j] and arr[i] <= pile[-1]:
            pile.append(arr[i])
            i += 1
        elif arr[j] >= arr[i] and arr[j] <= pile[-1]:
            pile.append(arr[j])
            j -= 1
        else: # cannot find any good cube to place on top
            break
    if (i ==j):  # middleMost element
        if arr[i] <= pile[-1]:
            pile.append(arr[i])

    if len(pile) - 1 == nums[0]:
        print("Yes")
    else:
        print("No")       

    T[0] -= 1