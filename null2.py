import requests
import json
import re
from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

API_URL = 'https://api.jikan.moe/v4/anime'
print(API_URL)

#time clean and convert
def cleaned_duration(duration_str):
    if not duration_str:
        return None

    stripped_duration = duration_str.lower().strip()
    for string in ("per ep", "per episode", "per eps", "per", "each", "episodes", "episode", "~"):
        stripped_duration = stripped_duration.replace(string, " ")
    cleaned = " ".join(stripped_duration.split())
    print('--------cleaned:', cleaned)

    hour_search = re.search(r'(\d+)\s*(?:h|hr|hrs|hour|hours)\b', cleaned)
    minute_search  = re.search(r'(\d+)\s*(?:m|min|mins|minute|minutes)\b', cleaned)
    print('--------hour_search:', hour_search)
    print('--------minute_search:', minute_search)
    if hour_search or minute_search:
        hours = int(hour_search.group(1)) if hour_search else 0
        minutes = int(minute_search.group(1)) if minute_search else 0
        print('--------hours:', hours)
        print('--------minutes:', minutes)

        total_minutes = hours * 60 + minutes
        print('--------total_minutes:', total_minutes)
        return total_minutes

#logic for how long itll take to finish
def estimate_time(anime):
    mode = request.form.get('mode')
    if mode == 'time-available'

    else:

    

#later:  Rate Limit (Jikan API has no authentication but but has rate limit of 3 requests per second) ################################## Highly doubt to go over that but you never know

currently_watching = []

#NOTE - HOME PAGE ROUTE - ###########################################################################################################
@app.route('/', methods=["GET", "POST"])
def home():
    global currently_watching

    if request.method == "GET":
        query = request.args.get('name')
        print ('------Search query:', query)

        if query:
            queryJson = requests.get(API_URL, params={'q': query}).json()

            anime_suggestions = []
            for anime in queryJson.get('data', []):
                anime_info = {
                    'title': anime.get("title"),
                    'image': anime.get("images", {}).get("jpg", {}).get("image_url"), 
                    'type': anime.get("type"),
                    'episodes': anime.get("episodes"),
                    'duration': anime.get("duration"),
                    'MALurl': anime.get("url"),
                    'status': anime.get("status"),
                    'year': anime.get("year") or anime.get("aired", {}).get("prop", {}).get("from", {}).get("year"),
                    'genres': [g.get("name") for g in anime.get("genres", [])],
                    'demographics': (anime.get("demographics") or [{}])[0].get("name")
                }
                anime_suggestions.append(anime_info)
            
            return render_template('index.html', anime_suggestions=anime_suggestions)
            #passed onto SUGGESTED ANIME/#query-suggestions
            
        else:
            defaultQuery = 'Search for an Anime!'
            return render_template('index.html', currently_watching=currently_watching, defaultQuery=defaultQuery)

    else:
        if query-suggestions-indiv:
            duration_minute = cleaned_duration(request.form.get('duration1'))
            print('------duration_minute:', duration_minute)

            anime_info = {
                'title': request.form.get('title1'),
                'image': request.form.get('image1'),
                'type': request.form.get('type1'),
                'episodes': request.form.get('episodes1'),
                'duration': request.form.get('duration1'),
                'MALurl': request.form.get('MALurl1'),
                'status': request.form.get('status1')
                'year': request.form.get('year1'),
                'genres': request.form.get('genres').split(', '),
                'demographics': request.form.get('demographics1')
            }
            print(anime_info)

            currently_watching.append(anime_info)
            print(currently_watching)
            return redirect(url_for('home'))

# TODO watched-anime #################################################################################################################

# TODO just-finished #################################################################################################################

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5006)