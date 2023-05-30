# Write a program that read a four-digit number N and checks if N is an Armstrong Number.

# N = 1643 
# 1^4+6^4+3^4+4^4 = 1643 


n = input()
sums = int(n[0])**4+int(n[1])**4+int(n[2])**4+int(n[3])**4
if(sums==int(n)):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")