from flask import Flask, render_template, send_from_directory
import sqlite3
import os

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/html/<path:filename>')
def serve_html(filename):
    return send_from_directory('static/html', filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('static/js', filename)

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('static/css', filename)

@app.route('/img/<path:filename>')
def serve_img(filename):
    return send_from_directory('static/img', filename)

@app.route('/favicon.ico')
def serve_favicon():
    return send_from_directory('static/img/html', 'icon.ico')

# Function to fetch non-restricted videos for a user
def get_non_restricted_videos(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Fetch non-restricted videos for the specified user
    cursor.execute("SELECT video FROM PTs WHERE user = ? AND restrictedVideo = 0", (username,))

    videos = cursor.fetchall()
    conn.close()
    return videos

# Route to display videos for a user
@app.route('/user_videos/<username>')
def user_videos(username):
    videos = get_non_restricted_videos(username)
    return render_template('videos.html', username=username, videos=videos)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def blogHome():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/post.html')
def post():
    return render_template('post.html')

@app.route('/user_video')
def user_video():
    return render_template('user_video.html')


if __name__ == '__main__':
    app.run(debug=True)