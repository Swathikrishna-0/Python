# Write a function with the name calculate_league_points that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.

# Input 
# 4,1,2 
# Output 
# 16 

# Input 
# 2,0,9 
# Output 
# -1 

def calculate_league_points(wins, draws, losses):
    summ = (wins*4) + (draws*2) + (losses*(-1))
    print(summ)


statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])

calculate_league_points(wins,draws,losses)