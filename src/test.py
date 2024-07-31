'''
Jayati Samar
Last edited: 07/13/2024
Associated with: CS6620: Cloud Computing - REST API Assignment
Objective: This file contains tests for use with the REST API Assignment.
'''
import pytest
from rest import create_app

@pytest.fixture()
def app():
	app = create_app()
	app.config.update({
	"TESTING": True,
	})

    # other setup can go here

	yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
	return app.test_client()


def test_get_songs(client):
	url = '/songs'
	response = client.get(url)
	assert response.status_code == 200
          
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

def test_delete_song(client):
	url = '/songs/2'
	response = client.delete(url)
	assert response.status_code == 200
