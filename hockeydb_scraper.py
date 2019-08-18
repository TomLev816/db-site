import requests
from bs4 import BeautifulSoup
import time
url = 'https://www.nwhl.zone/stats/league_instance/46947?subseason=327151'

try:
    page = requests.get(url)
except:
    print("An error occured")

soup = BeautifulSoup(page.text, 'html.parser')
# soup = soup.encode("utf-8")

find_odd = soup.find_all(class_="odd")
find_even = soup.find_all(class_="even")

# print("find odd")
# print(find_odd)
# print("find even")
# print(find_even)
# import pdb; pdb.set_trace()


# print(find_even[2].find_all(class_=""))
# print(find_even[2].find_all(class_=""))


list_of_players = [find_odd, find_even]
player = 2

def print_players(list_of_players):
    for player in list_of_players:
        # print(player) 
        
        print('===========================================')
        print('Player Name:')
        print(player.find("a").contents[0])

        print('Team:')
        print(player.find(class_='teamName').contents[0])

        print('Jesery num:')
        print(player.find_all(class_="")[0].contents[0])

        print('GP:')
        print(player.find(class_="highlight").contents[0])

        print('Goals:')
        print(player.find_all(class_="")[4].contents[0])

        print('Assist:')
        print(player.find_all(class_="")[5].contents[0])

        print('Points:')
        print(player.find_all(class_="")[6].contents[0])

        print('SOG:')
        print(player.find_all(class_="")[7].contents[0])

print_players(find_odd)
print_players(find_even)

# print(len(find_even))
