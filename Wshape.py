# Given a number N write a program to print the letter W of N rows using stars(*)
# input = 5 
# * * * * * * * * * 
#  * * * * * * * * 
#   * * *   * * * 
#    * *     * * 
#     *       * 
N = int(input())
print("* " * (2 * N - 1))
for k in range(1, N):
    print(" " * k, end="")
    print("* " * (N - k), end="")
    print("  " * (k - 1), end="")
    print("* " * (N - k))