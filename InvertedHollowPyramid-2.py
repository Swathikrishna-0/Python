#Given a number N, write a program to print an inverted hollow pyramid of 2*N-1 rows using numbers. 

# Input:
# 3 
# Output:
#     1
#   2 2
# 3   3
#   2 2
#     1

# Input:
# 6
# Output:
#           1
#         2 2
#       3   3
#     4     4
#   5       5
# 6         6
#   5       5
#     4     4
#       3   3
#         2 2
#           1



n = int(input())
for i in range(1,n+1):
    if i==1:
        left_spaces = " "*((n-i)*2)
        print(left_spaces+str(i))
    else:
        left_spaces = " " * ((n-i)*2)
        hollow_spaces = " "*(2*i-3)
        numbers = str(i)
        print(left_spaces+numbers+hollow_spaces+numbers)
        k = n-1 
for j in range(1,n):
    if j ==n-1:
        left_spaces = " "*((j)*2)
        print(left_spaces+str(1))
    else:
        left_spaces = " "*((j)*2)
        hollow_spaces = " "*(2*k-3)
        numbers = str(k)
        print(left_spaces+numbers+hollow_spaces+numbers)
        k -= 1
        
        
        
        
        
        
        
        