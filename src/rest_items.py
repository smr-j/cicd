'''
Jayati Samar
Last edited: 08/1/2024
CS6620: Cloud Computing - CI/CD Assignment
Objective: This file sets up a simple CI/CD workflow.
'''
from flask import Flask, request, jsonify
import boto3
import os
import json

def create_app():
	app = Flask(__name__)
	return app
	
app = create_app()

# DynamoDB table and S3 bucket configuration 
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID','default')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY','secret')
aws_region = os.environ.get('AWS_DEFAULT_REGION','us-east-1')
dynamodb = boto3.resource('dynamodb', 
                          endpoint_url='http://localstack:4566',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=aws_region)
s3 = boto3.client('s3', 
                  endpoint_url='http://localstack:4566',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=aws_region)

DYNAMODB_TABLE = os.environ.get('DYNAMODB_TABLE', 'SongTable')
table = dynamodb.Table(DYNAMODB_TABLE)
S3_BUCKET = os.environ.get('S3_BUCKET', 'song_bucket')


# Create test data in the form of a song catalog.
songs = [
    {
        "id": 1,
        "title": "Another Round",
        "artist": "Edie Brickell & Steve Martin",
        "album": "So Familiar",
        "release": "12-01-2015",
        "spotify link": "https://open.spotify.com/track/1HKz0H8Tzxol2ktt7Y4ww0?si=8064e9d8d3dc4a09"
    },
    {
        "id": 2,
        "title": "Pressure",
        "artist": "Billy Joel",
        "album": "The Nylon Curtain",
        "release": "06-23-1982",
        "spotify link": "https://open.spotify.com/track/3LqvmDtXWXjF7fg8mh8iZh?si=3742df9928c44f3c"
    },
    {
        "id": 3,
        "title": "Golden Dandelions",
        "artist": "Barns Courtney",
        "album": "The Attractions of Youth",
        "release": "09-29-2017",
        "spotify link": "https://open.spotify.com/track/78ZsfJB762SXFfLK96mBmC?si=df7ff6d61f5c4105"
    }
]

def initializer():
    for song in songs:
        # Add song to DynamoDB
        table.put_item(Item=song)

        # Create and add song file to S3
        file_content = json.dumps(song)
        file_name = f"{song['id']}.json"
        s3.put_object(Bucket=S3_BUCKET, Key=file_name, Body=file_content)

# Initialize the database and S3 with the songs
initializer()


@app.route('/songs', methods=['GET'])
def get_songs():
    response = table.scan()
    return jsonify(response['Items']),200

@app.route('/songs', methods=['POST'])
def add_song():
    new_song = request.get_json()
    
	# Song added in DynamoDB
    table.put_item(Item=new_song)
    
    # Song file created and added in S3
    file_content = json.dumps(new_song)
    file_name = f"{new_song['id']}.json"
    s3.put_object(Bucket=S3_BUCKET,Key=file_name,Body=file_content)
    
    return jsonify(new_song), 201

@app.route('/songs/<int:id>', methods=['PUT'])
def update_song(id):
    song_id = {"ID":id}
    if id < len(songs):
        updated_song = request.json
        # Update song in DynamoDB
        table.update_item(Key=song_id,UpdateExpression="set title=title,artist=artist,album=album,release=release,spotify_link=link",
                          ExpressionAttributeValues={'title': updated_song['title'],
                                                     'artist':updated_song['artist'],
                                                     'album':updated_song['album'],
                                                     'release':updated_song['release'],
                                                     'link':updated_song['spotify link']},
                                                     ReturnValues="UPDATED_NEW")
        # Update song file in S3
        file_name = f"{id}.json"
        updated_file_content = json.dumps(updated_song)
        s3.put_object(Bucket=S3_BUCKET,Key=file_name,Body=updated_file_content)
        return jsonify(updated_song), 200
    else:
        return "Song was not found.", 404


@app.route("/songs/<int:id>", methods=["DELETE"])
def delete_song(id):
    song_id = {"ID":id}
    if id < len(songs):
        response = table.delete_item(Key=song_id,ReturnValues="ALL_OLD")
        deleted_song = response.get('Attributes', None)
        return jsonify(deleted_song), 200
    else:
        return "Song was not found", 404

if __name__ == '__main__':
    app.run()
