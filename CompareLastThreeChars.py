# Write a program to check if the last three characters in the two given strings are the same. 

# apple
# pimple 
# o/p = True

first_line=input()
second_line=input()
length1=len(first_line)
length2=len(second_line)
last_three_first_line=first_line[-3:]
last_three_second_line=second_line[-3:]
result=last_three_first_line==last_three_second_line
print(result)    