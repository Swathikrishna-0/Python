# input 
# 3 
# output 
# * * * 
#  * * 
#   * 
#  * * 
# * * * 
N = int(input())

for i in range(N):
    spaces = " " * i 
    stars = "* " * (N - i)
    print(spaces + stars)
for i in range(1,N):
    stars = "* " * (i+1)
    spaces = " " * (N-i-1 ) 
    print(spaces + stars)
 