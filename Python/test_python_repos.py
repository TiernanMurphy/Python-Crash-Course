import requests
import unittest

# Make an API call, store response, check success
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
assert r.status_code == 200

response_dict = r.json()

# Verify total repositories greater than 2,000,000
assert response_dict['total_count'] > 2_000_000

# Verify returned repositories equals 30
repo_dicts = response_dict['items']
assert len(repo_dicts) == 30

# Check first repository
first_name = repo_dicts[0]['name']
assert first_name == "free-programming-books"
