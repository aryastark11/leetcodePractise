# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = list(map(int,input().split()))
nums = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

happiness = 0
A = set(A)
B = set(B)

for i in range(0,n):
    if nums[i] in A:
        happiness += 1
    elif nums[i] in B:
        happiness -= 1
print(happiness)