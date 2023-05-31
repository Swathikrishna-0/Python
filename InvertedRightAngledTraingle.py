# input
# 4 
# output 
# * * * * 
# + + + 
# + + 
# + 
n = int(input())
for i in range(n):
    if i==0:
        print(n*"* ")
    if i>0:
        print((n-i)*"+ ")