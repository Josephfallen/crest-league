from flask import Flask, render_template
import sqlite3
import random

app = Flask(__name__)

# Function to get standings from the database
def get_standings():
    conn = sqlite3.connect('standings.db')
    c = conn.cursor()
    c.execute("SELECT team, points FROM standings ORDER BY points DESC, team ASC")
    standings = c.fetchall()
    conn.close()
    return standings

# Function to distribute top teams evenly among pools
def distribute_top_teams(standings, num_pools):
    top_teams = standings[:8]
    remaining_teams = standings[8:]

    pools = [[] for _ in range(num_pools)]
    for i, team in enumerate(top_teams):
        pools[i % num_pools].append(team)

    return pools, remaining_teams

# Function to distribute top 20 randomly among 2 pools
def distribute_top_20_randomly(standings):
    top_20 = standings[:20]
    random.shuffle(top_20)

    pool1 = top_20[:10]
    pool2 = top_20[10:]

    return pool1, pool2

# Function to render the index page
def render_index():
    standings = get_standings()
    pools, remaining_teams = distribute_top_teams(standings, 4)
    
    # Add remaining teams to pools
    for i, team in enumerate(remaining_teams):
        pools[i % len(pools)].append(team)
    
    # Sort each pool in number order based on points
    for pool in pools:
        pool.sort(key=lambda x: x[1], reverse=True)
    
    return render_template('index.html', pools=pools)

# Function to render the top 20 page
def render_top20():
    standings = get_standings()
    pool1, pool2 = distribute_top_20_randomly(standings)
    
    return render_template('top20.html', pool1=pool1, pool2=pool2)

# Route for the index page
@app.route('/')
def index():
    return render_index()

# Route for the top 20 page
@app.route('/top20')
def top20():
    return render_top20()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
