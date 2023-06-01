# Input 
# Hello World
# Output 
# Ifmmp Xpsme
# print a letter next to the given letter

s = input()
for i in s:
    if i == " ":
        let = ord(" ")
        let2 = let 
        char = chr(let2)
    else:
        let = ord(i)
        let2 = let + 1 
        char = chr(let2)
    
    print(char,end="")