import sqlite3
game_db = sqlite3.connect(r'C:\Users\rishi\OneDrive\Desktop\Python Fantasy Cricket\cricketdata.db')
game_cursor = game_db.cursor()

def getPoints(team):
    ''' '''
    points = 0
    for g in team:
        for p in g:
            points += getVal(p[0])
    return points

def getVal(player):
    query = 'SELECT Value FROM Stats WHERE player_name = ?'
    game_cursor.execute(query, (player,))
    val =  game_cursor.fetchone()
    return val[0] 

def getTeamScore(match, team):
    ''' to evaluate the total team score'''
    ##############################
    #### EXECUTING QUERIES #######
    ##############################

    q = 'SELECT match_id, player_name, deliveries_faced, total_runs_scored, sixes, fours FROM Match, Teams, '
    queries = [
        q + 'batsmen WHERE Match.player_name = batsmen.player_name AND Teams.Name = batsmen.team_name AND Match.match_id = ? AND Teams.Name = ?',
        q + 'bowlers WHERE Match.player_name = bowlers.player_name AND Teams.Name = bowlers.team_name AND Match.match_id = ? AND Teams.Name = ?',
        q + 'all_rounder WHERE Match.player_name = all_rounder.player_name AND Teams.Name = all_rounder.team_name AND Match.match_id = ? AND Teams.Name = ?',
        q + 'wicket_keeper WHERE Match.player_name = wicket_keeper.player_name AND Teams.Name = wicket_keeper.team_name AND Match.match_id = ? AND Teams.Name = ?'
    ]
    players = {}

    for query in queries:
        game_cursor.execute(query, (match, team))
        result = game_cursor.fetchall()
        for res in result:
            player_name = res[0]
            performance_data = res[1:]
            players[player_name] = performance_data

    print(players)

    team_score = 0
    player_score = {}
    for name,scores in players.items():
        score = getPlayerScore(score)
        team_score += score
        player_score[name] = score
    player_score.insert(0,team_score)
    return player_score

def getPlayerScore(p):
    runs = p[0]
    faced = p[1]
    fours = p[2]
    sixes = p[3]
    bowled = p[4]
    maiden = p[5]
    given = p[6]
    wkts = p[7]
    catches = p[8]
    stumping = p[9]
    runout = p[10]
    score = runs/2 +fours + sixes * 2 + maiden * 4 + 10 * (wkts + catches + stumping + runout)
    if faced > 0:
        strike_rate = runs/faced * 100
    else:
        strike_rate = 0
    if bowled > 0:
        eco_rate = 6 * given/bowled
    else:
        eco_rate = 0
    if strike_rate > 100:
        score += 4
    elif strike_rate >= 80:
        score += 2
    if eco_rate < 2:
        score += 10
    elif eco_rate < 3.5:
        score += 7
    elif eco_rate < 4.5:
        score += 4
    if runs > 100:
        score += 10
    elif runs > 50:
        score += 5
    if wkts >= 5:
        score+=10
    elif wkts >= 3:
        score+=5

    return int(score)
