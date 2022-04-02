def show_team(names, team_size):
    help_show_team(names, team_size, [], 0)

def help_show_team(names, team_size, result_list, position):
    if len(result_list) == team_size:
        print(result_list)
        return
    if position == len(names):
        return
    
    help_show_team(names, team_size, result_list + [names[position]], position + 1)
    help_show_team(names, team_size, result_list, position + 1)

players = ["Dey", "Ruowen", "Josh", "Kinder", "Mario", "Rock", "LOL"]
show_team(players, 2)

print()

import copy
def show_team(names, team_size):
    help_show_team(names, team_size, [], 0)

def help_show_team(names, team_size, result_list, position):
    if len(result_list) == team_size:
        print(result_list)
        return
    if position >= len(names):
        return

    result_list_copy = copy.deepcopy(result_list)
    result_list_copy.append(names[position])
    help_show_team(names, team_size, result_list, position + 1)
    help_show_team(names, team_size, result_list_copy, position + 1)

   
players = ["Dey", "Ruowen", "Josh", "Kinder", "Mario", "Rock", "LOL"]
show_team(players, 2)
