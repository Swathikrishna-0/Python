# write a program to print the kth smallest number in the list 

# input 
# 2,3,-1,5
# 1
# output 
# 2

# input 
# 30,52,24,19
# 1
# output
# 19

k=input().split(",")
num = int(input())
n=[]
for i in k:
  n.append(int(i))
m=sorted(n , reverse=True)
print(m[-num])