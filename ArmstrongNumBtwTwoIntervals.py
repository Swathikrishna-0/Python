# Given two number M and N write a program to print all the armstrong numbers starting from M to N if there are no Armstrong numbers print -1 

# N = 153 
# 1^3 + 5^3 + 3^3 
# Output 153
# input 
# 150 
# 200
# Output 
# 153 

# Input 
# 1 
# 3 
# Output 
# 1 2 3 
A=int(input())
B=int(input())
flag = False
for i in range(A, B+1):
    x = len(str(i))
    sum1 = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum1 += digit ** x
        temp //= 10
    if i == sum1:
        flag = True
        print(i,end=" ")
if not flag:
    print(-1)