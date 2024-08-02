'''
Jayati Samar
Last edited: 07/31/2024
Associated with: CS6620: Cloud Computing - CI/CD Assignment
Objective: This file contains tests for use with the CI/CD Assignment.
'''
import pytest
import os
import boto3
import json
from rest_items import create_app




default_songs = [
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


@pytest.fixture()
def app():
	app = create_app()
	app.config.update({
	"TESTING": True,
	})
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
    # other setup can go here
	for song in default_songs():
		table.put_item(Item=song)
		s3.put_object(Bucket=S3_BUCKET,Key=f"{song['id']}.json", Body=json.dumps(song))

	yield app

    # clean up / reset resources here
	for song in default_songs():
		table.delete_item(Key={"id": song['id']})
		s3.delete_object(Bucket=S3_BUCKET, Key=f"{song['id']}.json")
	

@pytest.fixture()
def client(app):
	return app.test_client()


def test_get_songs(client):
	url = '/songs'
	response = client.get(url)
	assert response.status_code == 200

def test_get_specific_song(client):
	url = '/songs/1'
	response = client.get(url)
	assert response.status_code == 200
	
def test_get_nonexistent_song(client):
	url = '/songs/1200'
	response = client.get(url)
	assert response.status_code == 404

          
def test_add_song(client):
	new_song = {"id": 4,
		    "title":"Bethlehem Steel",
		    "artist":"Delta Rae",
		    "album":"After It All",
		    "release":"04-07-2017",
		    "spotify link":"https://open.spotify.com/track/0mwXgKxOrmSk2veQkLbWSJ?si=3b0d11732d134fda"
		   }
	url = '/songs'
	response = client.post(url,json=new_song)
	assert response.status_code == 201


def test_update_song(client):
	updated_song = {
		"id": 2,
        	"title":"Storm Song",
		"artist":"PHILDEL",
		"album":"The Disappearance of the Girl",
		"release":"02-04-2014",
		"spotify link":"https://open.spotify.com/track/5GTziJvDhtcCR6kCr6Ir8r?si=c3ef1d4ee015422a"
	}
	url = '/songs/2'
	response = client.put(url, json=updated_song)
	assert response.status_code == 200

def test_duplicate_song(client):
    duplicate_song = {
        "id": 1,
        "title": "Another Round",
        "artist": "Edie Brickell & Steve Martin",
        "album": "So Familiar",
        "release": "12-01-2015",
        "spotify link": "https://open.spotify.com/track/1HKz0H8Tzxol2ktt7Y4ww0?si=8064e9d8d3dc4a09"
    }
    url = '/songs'
    response = client.post(url, json=duplicate_song)
    assert response.status_code == 409

def test_delete_song(client):
	url = '/songs/2'
	response = client.delete(url)
	assert response.status_code == 200
