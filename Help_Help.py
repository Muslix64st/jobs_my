import requests
from plotly.offline import offline
from plotly.offline.offline import _plot_html

url = 'https://api.github.com/search/repositories?q=Languge&python=&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(F"status code: {r.status_code}")

response_dict = r.json(encoding=utf-8)

repo_dicts = response_dict['items']
repo_names, star = [], []
print(f" repositories returned: {len(repo_dicts)}")
print("\nSelected information about each repository:")

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    star.append(repo_dict['stargazers_count'])

data = [ {
        'type': 'bar',
        'x': repo_names,
        'y': star,
        'marker': {'color': 'rgb(60, 100, 150)',
                   'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
                  },
        'opacity': 0.6,
        }]
my_layout = {
             'title': 'Most-starred Python Projects on Github',
              'xaxis': {'title': 'repository'},
              'yaxis': {'title': 'stars'},

            }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')


