# Given two numbers M and N write a program to print a Hollow Rectangle of M+2 rows and N+2 columns using pulses(+), hyphens(-) and pipes(|)

# input 
# 3
# 10 
# output
# +----------+
# |          |
# |          | 
# |          |
# +----------+
m = int(input())
n = int(input())
s= m+2
for i in range(s):
    if i==0:
        print("+"+(n*"-")+"+")
    elif i==(s-1):
        print("+"+(n*"-")+"+")
    else:
        print("|"+(n*" ")+"|")
        
        