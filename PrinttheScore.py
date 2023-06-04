# Input 
# 70
# Output 
# 40*2 = 80 -> 0-40
# 20*4 = 80 -> 41-60
# 10*6 = 60 -> 61-120
# 0*8 = 0   -> 121-above
# 220 + 50(bonus) 
# ans = 270
n = int(input())
rem = 0 
summ = 0
if n<=40:
   summ = n*2 + 50
if n>40:
    summ = 40*2 
    rem = n - 40 
    if rem>20:
        summ = summ + (20*4) 
        rem = rem - 20 
        if rem>60:
            summ = summ + (60*6)
            rem = rem - 60 
            if rem>1:
                summ = summ + (rem*8) + 50
        elif rem<60:
            summ = summ + (rem*6) + 50
    elif rem<20:
        summ = summ + (rem*4) + 50
print(summ)