import requests
from operator import itemgetter
from plotly import offline

# Step 1: Get the full list of top story IDs
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
submission_ids = r.json()

submission_dicts = []

# Step 2: Fetch details for all top stories (or a large subset)
for submission_id in submission_ids[:500]:  # you can adjust this number
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(item_url)
    story = r.json()

    if story is None:  # skip deleted/missing stories
        continue

    submission_dict = {
        'title': story.get('title', 'No title'),
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': story.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)

# Step 3: Sort all stories by number of comments
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Step 4: Keep only the top 30 most active
top_30 = submission_dicts[:30]

# Step 5: Prepare data for Plotly
titles = [d['title'] for d in top_30]
labels = [
    f"<a href='{d['hn_link']}'>{(d['title'][:50] + '...') if len(d['title']) > 50 else d['title']}</a>"
    for d in top_30
]
comments = [d['comments'] for d in top_30]

data = [{
    'type': 'bar',
    'x': comments,       # number of comments
    'y': labels,         # article titles
    'orientation': 'h',  # horizontal bars
    'hovertext': titles, # full titles on hover
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.7,
}]

my_layout = {
    'title': {'text': '30 Most Active Hacker News Discussions', 'font': {'size': 28}},
    'xaxis': {'title': '# of Comments', 'tickfont': {'size': 14}},
    'yaxis': {'title': 'Articles', 'tickfont': {'size': 12}},
    'margin': {'l': 250},  # make space for long labels
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_most_active.html')
