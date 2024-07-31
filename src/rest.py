'''
Jayati Samar
Last edited: 07/13/2024
CS6620: Cloud Computing - REST API Assignment
Objective: This file sets up a simple REST API.
'''
from flask import Flask, request, jsonify

def create_app():
	app = Flask(__name__)
	return app
	
app = create_app()

# Create test data in the form of a song catalog.
songs = [
    {
        "id": 1,
        "title":"Another Round",
        "artist":"Edie Brickell & Steve Martin",
        "album":"So Familiar",
        "release":"12-01-2015",
        "spotify link":"https://open.spotify.com/track/1HKz0H8Tzxol2ktt7Y4ww0?si=8064e9d8d3dc4a09"
    },
    {
        "id": 2,
        "title":"Pressure",
        "artist":"Billy Joel",
        "album":"The Nylon Curtain",
        "release":"06-23-1982",
        "spotify link":"https://open.spotify.com/track/3LqvmDtXWXjF7fg8mh8iZh?si=3742df9928c44f3c"
    },
	{
        "id": 3,
        "title":"Golden Dandelions",
        "artist":"Barns Courtney",
        "album":"The Attractions of Youth",
        "release":"09-29-2017",
        "spotify link":"https://open.spotify.com/track/78ZsfJB762SXFfLK96mBmC?si=df7ff6d61f5c4105"
	}	
]

@app.route('/songs', methods=['GET'])
def get_songs():
    return jsonify(songs), 200

@app.route('/songs', methods=['POST'])
def add_song():
    new_song = request.get_json()
    songs.append(new_song)
    return jsonify(new_song), 201

@app.route('/songs/<int:id>', methods=['PUT'])
def update_song(id):
    if id < len(songs):
        updated_song = request.json
        songs[id] = updated_song
        return jsonify(updated_song), 200
    else:
        return "Song was not found.", 404


@app.route("/songs/<int:id>", methods=["DELETE"])
def delete_song(id):
    if id < len(songs):
        deleted_song = songs.pop(id)
        return jsonify(deleted_song), 200
    else:
        return "Song was not found", 404

if __name__ == '__main__':
    app.run()
