# Given a number N write a program to print a Pyramid and an Inverted Hollow Pyramid in 2 * N-1 rows using stars(*)

# input 
# 5
# output 
#     *
#    * * 
#   * * *
#  * * * *
# * * * * *
#  *     * 
#   *   * 
#    * *  
#     * 
N = int(input())
for i in range(N):
    print(' '*(N - i - 1)+'* '* (i + 1))
for j in range(N-1):
    stars =' '*(j + 1)+ '*' + ' '*(N*2-2*j-5) + '*'
    if j == (N - 2):
        stars = ' '*(N - 1) + '*'
    print(stars)