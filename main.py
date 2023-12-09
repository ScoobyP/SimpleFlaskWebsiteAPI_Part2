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
        return render_template('homepage.html', record=teamrecord, teams=ipl_teams)
    else:
        return render_template('homepage.html', message='Please select a team', teams=ipl_teams)


if __name__ == '__main__':
    website.run(debug=True, port=5003)