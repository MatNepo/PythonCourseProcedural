# Lab_3: Divide players into 2 equal teams

list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Total amount of players
players_total = len(list_players)
# Amount of players in a team
players_in_team = players_total // 2
# Which players belong to the teams
team_1 = list_players[:players_in_team]
team_2 = list_players[players_in_team:]

# Output
print(team_1)
print(team_2)
