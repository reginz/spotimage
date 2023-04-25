from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

def get_playlist_from_image(image):
    # Dummy function to return a Spotify playlist link
    return "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image = request.files["image"]
        playlist_link = get_playlist_from_image(image)
        return redirect(playlist_link)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
