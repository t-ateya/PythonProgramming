import json
from pathlib import Path

"""
movies = [
    {"id": 1, "title": "Termintor", "year": 1994},
    {"id": 2, "title": "Kindergarten Cop", "year": 1997},
    {"id": 3, "title": "Great Hunter", "year": 1990},
    {"id": 4, "title": "Escalator", "year": 2010},
    {"id": 5, "title": "Great Love", "year": 2020},

]

data = json.dumps(movies)
Path("movies.json").write_text(data)
"""
data = Path("./movies.json").read_text()
movies = json.loads(data)
print("first: ", movies[0]["title"])
print("last: ", movies[-1])
