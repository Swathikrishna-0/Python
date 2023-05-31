# Input 
# 4 
# Output 
#    1
#   1 2
#  1 2 3 
# 1 2 3 4
#  1 2 3 
#   1 2 
#    1 
a= int(input())
for i in range(1,a+1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range((a-1),0,-1):
    print(" "*(a-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()