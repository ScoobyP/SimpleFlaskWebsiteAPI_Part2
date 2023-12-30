from flask import Flask, render_template, request

import requests

website = Flask(__name__)


@website.route('/')
def page_1():
    all_team_names = requests.get('http://127.0.0.1:5002/api/teams')
    ipl_teams = all_team_names.json()['Teams']
    return render_template('homepage.html', teams=ipl_teams)


@website.route('/team_record', methods=['get'])
def page_2():
    all_team_names = requests.get('http://127.0.0.1:5002/api/teams')
    ipl_teams = all_team_names.json()['Teams']

    team1 = request.args.get('ipl_team_name')
    if team1:
        record = requests.get(f'http://127.0.0.1:5002/api/team_record?team={team1}')
        teamrecord = record.json()['Team Record']

        return render_template('homepage.html', record=teamrecord, teams=ipl_teams, team1=team1)
    else:
        return render_template('homepage.html', message='Please select a team', teams=ipl_teams)


@website.route('/all_batsmen')
def page_3():
    all_names = requests.get('http://127.0.0.1:5002/api/batsmen')
    batter_name = all_names.json()['Batsman']
    return render_template('Batsman.html', batter_names=batter_name)


@website.route('/batsman_record', methods=['get'])
def page_4():
    all_names = requests.get('http://127.0.0.1:5002/api/batsmen')
    batter_name = all_names.json()['Batsman']

    batsman1 = request.args.get('batter_name')
    if batsman1:
        season_record = requests.get(f'http://127.0.0.1:5002/api/batsman_record?batter={batsman1}')
        bats_rec1 = season_record.json()["Batsman Record"]

        against_record = requests.get(f'http://127.0.0.1:5002/api/batsman_against_record?batter={batsman1}')
        bats_rec2 = against_record.json()["Batsman Against Record"]

        pom_record = requests.get(f'http://127.0.0.1:5002/api/POM_record?pom={batsman1}')
        bats_rec3 = pom_record.json()["Player of Match Record"]

        if bats_rec1 or bats_rec2:
            if bats_rec3:
                return render_template('Batsman.html', batter_rec=bats_rec1, against_rec=bats_rec2, pom_rec=bats_rec3, batter_names=batter_name, batsman1=batsman1)
            else:
                return render_template('Batsman.html', batter_rec=bats_rec1, against_rec=bats_rec2, batter_names=batter_name, batsman1=batsman1, pmessage='No Record to Show')
        else:
            return render_template('Batsman.html', batter_names=batter_name, message='No Record To Show', batsman1=batsman1)
    else:
        return render_template('Batsman.html', batter_names=batter_name, message='Please select a Batsman')


@website.route('/download')
def page_5():
    return render_template('downloadpage.html')


@website.route('/pom', methods=['get'])
def page_6():
    all_names= requests.get('http://127.0.0.1:5002/api/POM_names')
    player_names = all_names.json()['POM Names']
    return render_template('playerofmatch.html', player_name = player_names)


@website.route('/pom_record', methods=['get'])
def page_7():
    all_names = requests.get('http://127.0.0.1:5002/api/POM_names')
    player_names = all_names.json()['POM Names']

    player1 = request.args.get('pom_name')
    if player1:
        record = requests.get(f'http://127.0.0.1:5002/api/POM_record?pom={player1}')
        player_rec = record.json()['Player of Match Record']

        if player_rec:
            return render_template('playerofmatch.html', player_name=player_names, player_rec=player_rec, player1=player1)
        else:
            return render_template('playerofmatch.html', player_name=player_names, message='No Record To Show')
    else:
        return render_template('playerofmatch.html', player_name = player_names, message='Please Select a Player')

@website.route('/all_bowlers')
def page_9():
    all_names = requests.get('http://127.0.0.1:5002/api/bowlers')
    bowler_names = all_names.json()['Bowlers']
    return render_template('Bowlers.html', bowler_name=bowler_names)


@website.route('/bowler_record', methods=['get'])
def page_10():
    all_names = requests.get('http://127.0.0.1:5002/api/bowlers')
    bowler_names = all_names.json()['Bowlers']

    bowler1 = request.args.get('bowler_name')
    if bowler1:
        season_record = requests.get(f'http://127.0.0.1:5002/api/bowling_rec?bowler={bowler1}')
        bowler_rec1 = season_record.json()["Bowler Record by Season"]

        pom_record = requests.get(f'http://127.0.0.1:5002/api/POM_record?pom={bowler1}')
        bats_rec3 = pom_record.json()["Player of Match Record"]

        if bowler_rec1:# or bowler_rec2:
            if bats_rec3:
                return render_template('Bowlers.html', season_rec=bowler_rec1, pom_rec=bats_rec3, bowler_name=bowler_names, bowler1=bowler1)
            else:
                return render_template('Bowlers.html', season_rec=bowler_rec1,bowler_name=bowler_names, bowler1=bowler1, pmessage='No Record to Show')
    else:
        return render_template('Bowlers.html', bowler_name=bowler_names, message='Please Select a Bowler')


if __name__ == '__main__':
    website.run(debug=True, port=5003)
