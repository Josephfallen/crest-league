from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_standings():
    conn = sqlite3.connect('standings.db')
    c = conn.cursor()
    c.execute("SELECT team, points FROM standings ORDER BY points DESC, team ASC")
    standings = c.fetchall()
    conn.close()
    return standings

@app.route('/')
def index():
    standings = get_standings()
    
    # Identify the top 8 teams
    top_8 = standings[:8]
    
    # Divide the remaining teams into four pools
    num_per_pool = 9
    remaining_teams = standings[8:]
    pools = [remaining_teams[i:i+num_per_pool] for i in range(0, len(remaining_teams), num_per_pool)]
    
    # Distribute the top 8 evenly across all pools
    for i, team in enumerate(top_8):
        pools[i % len(pools)].insert(0, team)
    
    # Sort each pool in number order based on points
    for pool in pools:
        pool.sort(key=lambda x: x[1], reverse=True)
    
    return render_template('index.html', pools=pools)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
