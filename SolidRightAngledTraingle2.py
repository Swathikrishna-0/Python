# Input 
# 4
# Output 
#       * 
#     * * 
#   * * * 
# * * * *
n = int(input())
for i in range(1,n+1):
    if i ==1:
        left_spaces = "  "*(n-1) 
        print(left_spaces+"*")
    elif i==n:
        print(n*"* ")
    else:
        left_spaces = "  "*(n-i)
        stars = "* "*i
        print(left_spaces+stars)