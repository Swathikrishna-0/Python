# You are given an integer N as input. Write a program to read N integers and print a list containing the first and last two input.

# Input 
# 6
# 1
# 2
# 3
# 4
# 5
# 6
# Output 
# [1,2,5,6]

# Input 
# 5
# 1
# 11
# 13
# 21
# 19
# Output 
# [1,11,21,19]

n = int(input())
list_ = []
for i in range(n):
    s = int(input())
    list_.append(s)
res = [] 
length = len(list_)
first_ = list_[0:2]
last_ = list_[length-2:length]
res = first_ + last_
print(res)