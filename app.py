import os
import sqlite3
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv

app = Flask(__name__)
app.config['DEBUG'] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

load_dotenv

TMDB_API_KEY = os.environ.get("TMDB_API_KEY")

#SQLite database
conn = sqlite3.connect("movie.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS movie (daytime TEXT NOT NULL, mood TEXT NOT NULL)")
cursor.execute("INSERT INTO movie (daytime, mood) VALUES ('test','test' )")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mood", methods = ["GET", "POST"])
def mood():
    if request.method == "GET":
        return render_template("mood.html")
    else:
        daytime_db = request.form.get("daytime")
        cursor.execute("UPDATE movie SET daytime = ?", [daytime_db])
        conn.commit()
        return render_template("mood.html", daytime = daytime_db)

@app.route("/loading", methods = ["GET", "POST"])
def loading():
    if request.method == "GET":
        return render_template("loading.html")
    else:
        mood_db = request.form.get("mood")
        cursor.execute("UPDATE movie SET mood = ?", [mood_db])

        cursor.execute("SELECT daytime FROM movie")

        daytime_db = cursor.fetchone()[0]


        conn.commit()
        return render_template("loading.html", mood = mood_db, daytime = daytime_db)
    
@app.route("/movies", methods = ["GET", "POST"])
def movies():
    if request.method == "GET":
        mood_db = request.form.get("mood")
        cursor.execute("UPDATE movie SET mood = ?", [mood_db])
        conn.commit()
        return render_template("movies.html")
      
    else:
        # Load data
        mood_db = request.form.get("mood")
        if mood_db:
            cursor.execute("UPDATE movie SET mood = ?", [mood_db])
        cursor.execute("SELECT daytime FROM movie")
        daytime_db = cursor.fetchone()[0]
        
        cursor.execute("SELECT mood FROM movie")
        mood_db = cursor.fetchone()[0]
        conn.commit()

        # Get back, next:
        button_id = request.form.get("button-id")
        i_str = request.form.get("i", "") 

        try:
            i = int(i_str)
        except ValueError:
            i = 0

                    
        if button_id == "next":
            i = i + 1
        elif button_id == "back":
            i = i - 1
       

        # Library of genres:
        genreslib = {
            28: "Action",
            12: "Adventure",
            16: "Animation",
            35: "Comedy",
            80: "Crime",
            99: "Documentary",
            18: "Drama",
            10751: "Family",
            14: "Fantasy",
            36: "History",
            27: "Horror",
            10402: "Music",
            9648: "Mystery",
            10749: "Romance",
            878: "Science Fiction",
            10770: "TV Movie",
            53: "Thriller",
            10752: "War",
            37: "Western"
        }

        cursor.execute("SELECT daytime FROM movie")
        daytime_db = cursor.fetchone()[0]
        cursor.execute("SELECT mood FROM movie")
        mood_db = cursor.fetchone()[0]
        conn.commit()
        
        if daytime_db == "🌤 MORNING":
            if mood_db == "😁 HAPPY":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=14,35")          
 
            if mood_db == "😌 RELAXED":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=12,35")
                      
            if mood_db == "🤧 SICK":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=16,35")
                      
            if mood_db == "🥰 ROMANTIC":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=10749,35")
              
            if mood_db == "😥 SAD":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=18,35")
               
            if mood_db == "😡 ANGRY":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=28,35")
             
            if mood_db == "😙 CHILL":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=10402,35")
               
            if mood_db == "😂 HUMOROUS":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=9648,35")
            
            title_db = response.json()['results'][i]['original_title']
            date_db = response.json()['results'][i]['release_date']
            poster_db = response.json()['results'][i]['poster_path']
            genresid_db = response.json()['results'][i]['genre_ids']
            description_db = response.json()['results'][i]['overview']

            genres = [genreslib[id] for id in genresid_db]

            length_db = len(response.json()['results'])



        if daytime_db == "☀️ NOON":
            if mood_db == "😁 HAPPY":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=14,28")               
 
            if mood_db == "😌 RELAXED":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=12,28")
                          
            if mood_db == "🤧 SICK":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=16,28")           
            
            if mood_db == "🥰 ROMANTIC":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=10749,28")            

            if mood_db == "😥 SAD":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=18,28")            

            if mood_db == "😡 ANGRY":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=28,28")
               
            if mood_db == "😙 CHILL":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=10402,28")           

            if mood_db == "😂 HUMOROUS":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=9648,28")
            
            title_db = response.json()['results'][i]['original_title']
            date_db = response.json()['results'][i]['release_date']
            poster_db = response.json()['results'][i]['poster_path']
            genresid_db = response.json()['results'][i]['genre_ids']
            description_db = response.json()['results'][i]['overview']

            genres = [genreslib[id] for id in genresid_db]

            length_db = len(response.json()['results'])



        if daytime_db == "🌙 NIGHT":
            if mood_db == "😁 HAPPY":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=14,53")
 
            if mood_db == "😌 RELAXED":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=12,53")
                
            if mood_db == "🤧 SICK":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=16,53")
            
            if mood_db == "🥰 ROMANTIC":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=10749,53")
               
            if mood_db == "😥 SAD":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=18,53")

            if mood_db == "😡 ANGRY":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=28,53")

            if mood_db == "😙 CHILL":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=10402,53")
                
            if mood_db == "😂 HUMOROUS":
                response = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=9648,53")
            title_db = response.json()['results'][i]['original_title']
            date_db = response.json()['results'][i]['release_date']
            poster_db = response.json()['results'][i]['poster_path']
            genresid_db = response.json()['results'][i]['genre_ids']
            description_db = response.json()['results'][i]['overview']

            genres = [genreslib[id] for id in genresid_db]

            length_db = len(response.json()['results'])
            

        return render_template("movies.html", mood = mood_db, daytime = daytime_db, title = title_db, genres = genres, poster = poster_db, date = date_db, description = description_db, i_val = i, length = length_db)
    

if __name__ == "__main__":
    app.run(port=8000, debug=True)