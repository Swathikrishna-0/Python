# Write a program that reads an amount A and prints the minimum number of 100, 50 , 20 and 10 rupee notes required for the given amount.

# input = 370 
# output

# 100 Notes : 3 
# 50 Notes : 1 
# 20 Notes : 1 
# 10 Notes : 0 

a = int(input())
print("100 Notes: "+str(int(a/100)))
print("50 Notes: "+str(int((a%100)/50)))
print("20 Notes: "+str(int(((a%100)%50)/20)))
print("10 Notes: "+str(int((((a%100)%50)%20)/10)))                                         