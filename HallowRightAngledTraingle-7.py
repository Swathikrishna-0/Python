# Given a number N write program to print a Hollow Right Angled Traingle of N rows using stars(*) and pluses(+)

# the first row contains N pluses(+) and the next N-1 rows contain stars(*):

# Input:
# 4
# Output:
# + + + + 
#   *   * 
#     * *
#       * 

# Input:
# 7
# Output:
# + + + + + + + 
#   *         *
#     *       * 
#       *     * 
#         *   * 
#           * * 
#             *
n = int(input())
for i in range(n):
    if i==0:
        print("+ "*n)
    elif i==n-1:
        print("  "*i + "*")
    else:
        print("  "*(i)+"* "+"  "*(n-i-2)+"*")
