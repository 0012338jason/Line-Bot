import requests
import re
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

playerpage = [] 
nameList = [] 
Rank = {} 
imformation = {} 

u = "https://www.atptour.com/en/rankings/singles?rankRange=1-100&rankDate=2022-12-12"

source = requests.get(u, headers=headers).text
objSoup = BeautifulSoup(source, "html.parser")
names = objSoup.find_all("span", class_="player-cell-wrapper")
# player's name
for name in names:
    nameList.append(name.text.lstrip().rstrip())

for name in names:
    pattern = "/en/players/(.*)/overview"
    txt = re.search(pattern, str(name))
    playerpage.append(txt.groups()[0][-4:])


for i in range(100):
    Rank[nameList[i]] = i + 1
    imformation[nameList[i]] = playerpage[i]


def changeformat(string):
    return str(string).lower().replace(" ", "-")

def getplayerinformation(name, web):
    url = (
        "https://www.atptour.com/en/players/"
        + str(name)
        + "/"
        + str(web)
        + "/player-activity"
    )
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    }
    source = requests.get(url, headers=headers).text
    objSoup = BeautifulSoup(source, "html.parser")
    names = objSoup.find_all("div", class_="table-big-value")
    objSoup2 = BeautifulSoup(source, "html.parser")
    names2 = objSoup2.find_all("div", class_="table-value")
    
    playerinformation = {}

    playerinformation["Age"] = names[0].text.rstrip().lstrip()[0:2]
    playerinformation["Height"] = names[3].text.rstrip().lstrip()[-6:-3]
    playerinformation["Weight"] = names[2].text.rstrip().lstrip()[7:11]
    playerinformation["Birthday"] = names[0].text.rstrip().lstrip()[-11:-1]
    playerinformation["Birthplace"] = names2[0].text.rstrip().lstrip()
    playerinformation["Turn Pro"] = names[1].text.rstrip().lstrip()[0:4]
    playerinformation["Plays"] = names2[1].text.rstrip().lstrip()
    playerinformation["Coach"] = names2[2].text.lstrip().rstrip()
    return playerinformation

def getheadtoheadinfomation(string):
    player = string.split(' vs ')
    url = (
        "https://www.atptour.com/en/players/atp-head-2-head/"
        + changeformat(string)
        + "/" + str(imformation[player[0].title()])
        + "/" + str(imformation[player[1].title()])
    )
    source = requests.get(url, headers=headers).text
    objSoup = BeautifulSoup(source, "html.parser")
    wins = objSoup.find_all("div", class_="players-head-rank")
    return player[0] + " " + wins[0].text.lstrip().rstrip() + "  vs  " + wins[1].text.lstrip().rstrip() + " " + player[1]


def gettournamentinformation(month):
    url = (
        "https://www.atptour.com/en/tournaments"
    )
    source = requests.get(url, headers=headers).text
    objSoup = BeautifulSoup(source, "html.parser")
    tournaments = objSoup.find_all("td", class_="title-content")
    data = {}

    for i in range(1, 13):
        data[i] = []
    for t in tournaments:
        tour_name = t.find("a", class_="tourney-title")
        location = t.find("span", class_="tourney-location")
        date = t.find("span", class_="tourney-dates")
        data[int(date.text.lstrip().rstrip()[-5:-3])].append(
            "Date:  " + date.text.lstrip().rstrip() + '\nTour Name:  ' + tour_name.text.lstrip().rstrip() + '\nLocation:  ' + location.text.lstrip().rstrip()
        )
    return "\n\n".join(data[int(month)])



