import pprint

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
res2 = request.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.txt, 'html.parser')
soup2 = BeautifulSoup(res2.txt, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.score')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.score')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sort(hnlist, key = lambda k:k['votes'])


def create_custom_hn(links,subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx]
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(votes[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)
pprint.pprint(create_custom_hn(mega_links, mega_subtext))