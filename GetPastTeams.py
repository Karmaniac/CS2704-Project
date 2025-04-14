import requests
import json

startingYear = 2013
listOfID = ["44151f7a-0f24-11e2-8525-18a905767e44",
            "4416272f-0f24-11e2-8525-18a905767e44",
            "4417b7d7-0f24-11e2-8525-18a905767e44",
            "4417b7d7-0f24-11e2-8525-18a905767e44",
            "4417eede-0f24-11e2-8525-18a905767e44",
            "441660ea-0f24-11e2-8525-18a905767e44",
            "4417d3cb-0f24-11e2-8525-18a905767e44",
            "4417d3cb-0f24-11e2-8525-18a905767e44",
            "4415ce44-0f24-11e2-8525-18a905767e44",
            "42376e1c-6da8-461e-9443-cfcf0a9fcc4d",
            "4418464d-0f24-11e2-8525-18a905767e44"]


def get_posts(teamID, year):
    url = "https://api.sportradar.com/nhl/trial/v7/en/seasons/" + str(year) + "/REG/standings.json?api_key="
    headers = {"accept": "application/json"}
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None



for teamID in listOfID:
  json_data = get_posts(teamID, startingYear)
  startingYear = startingYear + 1

  conferences = json_data["conferences"]
  for conference in conferences:
    divisions = conference["divisions"]
    for division in divisions:
      for team in division["teams"]:
        if team["id"] == teamID:
          wantedData = [startingYear - 1, team["name"], team["win_pct"], team["powerplay_pct"], team["penalty_killing_pct"], team["points_pct"], team["rank"]["division"], team["rank"]["conference"]]
          print(wantedData)
