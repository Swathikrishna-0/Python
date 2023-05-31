# Given a number N write a program to print a Right Angled Traingle of N rows using stars(*)

# input 
# 4 
# output 
# * * * * 
#   * * * 
#     * * 
#       * 
n = int(input())
for i in range(1,n+1):
    if i ==1:
        print(n*"* ")
    elif i==n:
        left_spaces = "  "*(n-1) 
        print(left_spaces+"*")
    else:
       left_spaces = "  "*(i-1)
       stars = "* "*((n+1)-i) 
       print(left_spaces+stars)