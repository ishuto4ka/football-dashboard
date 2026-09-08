ronaldo = {
    'name': 'Ronaldo',
    'minutes': 90,
    'distance': 10500,
    'max_speed': 36.9,
    'sprints': 12
}
messi = {
    'name': 'Messi',
    'minutes': 85,
    'distance': 1250,
    'max_speed': 34.1,
    'sprints': 4
}
mbappe = {
    'name': 'Mbappe',
    'minutes': 111,
    'distance': 16500,
    'max_speed': 38.3,
    'sprints': 67
}
players = [ronaldo, messi, mbappe] 

def check_load(player):
    if player['distance'] > 10000:
        return 'High'
    else:
        return 'Low'

def check_speed(players):
    fastest = players[0]
    for player in players:
        if player['max_speed'] > fastest['max_speed']:
            fastest = player
    return fastest
fastest = check_speed(players)
print(f'{fastest['name']} with {fastest['max_speed']} km/h is the fastest player.')