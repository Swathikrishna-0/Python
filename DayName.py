# Given the weekday of the first day of the month, determine the day of the week of the given date in that month.

# input
# --------
# Monday 
# 16 

# Output
# --------
# Tuesday

# input2
# -----------
# Tuesday 
# 17 

# output
# --------
# Thursday

day = input()
date = int(input())
week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weekday = date%7
result = 0 
for i in range(len(week)):
    if day == week[i]:
        index = i 
        result = weekday + index - 1
        if result >= len(week):
            result = result%7
print(week[result])