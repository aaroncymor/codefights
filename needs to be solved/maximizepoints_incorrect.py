"""
Two teams are playing a game of tennis. The team sizes are the same and each player 
from the first team plays against the corresponding player from the second team.
data transfer

Each player has a certain power level. If a player has a higher power level than 
her opponent, she is guaranteed to win and her team would get 1 point for that win 
while the opponents get a 0.

You are the coach of the first team and you know the power levels of all the players 
before the game starts. You want to rearrange the players in your team to earn the highest 
possible total score.

Example:

For team1 = [3,2,4] and team2 = [1,2,3] the answer is
maximizePoints(team1, team2) = 3

If you don't rearrange the players in the first team, it will get 2 points, since 3 > 1, 2 = 2 and 4 > 3.
However, if you rearrange the order of the players to [2, 3, 4], the first team will get 3 points.

    [input] array.integer team1
        The power levels of the players in the first team. Teams have less than 100 players and each power level is less than 100.

    [input] array.integer team2
        Array of the same length as team1, the power levels of the players of the second team.

    [output] integer
        The maximum number of points the first team can get.


"""

team1 = [3, 2, 4] 
team2 = [1, 2, 3]

def swap(team, index1, index2):
	temp = team[index1] 
	team[index1] = team[index2]
	team[index2] = temp
	return team

def maximizePoints(team1, team2):
	score = 0
	if len(team1) < 100 and len(team2) < 100 and len(team1) == len(team2):
		for i in range(len(team1)):
			j = i + 1 if i < len(team1) - 1 else 0
			if team1[i] > team2[i]:
				while j < len(team1):
					if team1[i] > team1[j] and team2[i] < team1[j] and team1[j] >= team2[j]:
						swap(team1, i, j)
						break
					j += 1				
			elif team1[i] < team2[i]:
				while j < len(team1):
					if team1[i] < team1[j] and team2[i] < team1[j]:
						swap(team1, i, j)
						break
					j += 1
		for k in range(len(team1)):
			if team1[k] > team2[k]:
				score += 1
	return score

print maximizePoints(team1,team2)



