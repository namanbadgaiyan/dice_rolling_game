import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    players = input('enter the number of players(2-4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Invalid number of players. Please enter a number between 2 and 4.')
    else:
        print('Invalid, try again')
        
max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player_inx in range(players):
        print('\nplayer number',player_inx+1,"turn has just started!")
        print('your total score is: ',player_score[player_inx], '\n')
        
        current_score = 0
        
        while True:
            should_roll = input('do u wanna roll(y): ')
            if should_roll.lower() != 'y':
                break
            
            value = roll()
            if value == 1:
                print('you rolled 1! turn over!')
                current_score = 0
                break
            else:
                print('you rolled',value)
                current_score += value
                
            print('your score is: ',current_score)
            
        player_score[player_inx] += current_score
        print('your total score is: ',player_score[player_inx])
        
max_score = max(player_score)
winning_inx = player_score.index(max_score)
print('player number', winning_inx+1, ' with the score of: ', max_score)