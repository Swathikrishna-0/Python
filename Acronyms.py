# You are given some abbreviations as input. Write a program to print the acronym separated by a dot(.) of those abbreviations.

# Input 
# Indian Administrative service 
# Output 
# I.A.S 

# Input 
# Very Important Person 
# Output 
# V.I.P 

n = list(input().split())
l = []
for i in n:
    l.append(i[0])
print(".".join(l))