# Write a program that reads an amount A and prints the minimum number of 2000,500,200,50,20,5,2 and 1 rupee notes required for the given amount. 

# input = 2257 
# output 

# 2000:1 500:0 200:1 50:1 20:0 5:1 2:1 1:0 

m = int(input())
print("2000:"+str(int(m/2000)), 
"500:"+str(int((m%2000)/500)), 
"200:"+str(int(((m%2000)%500)/200)), 
"50:"+str(int((((m%2000)%500)%200)/50)), 
"20:"+str(int((((((m%2000)%500)%200)%50)/20))), 
"5:"+str(int(((((((m%2000)%500)%200)%50)%20)/5))), 
"2:"+str(int(((((((m%2000)%500)%200)%50)%20)%5)/2)), 
"1:"+str(int((((((((m%2000)%500)%200)%50)%20)%5)%2)/1)))                     