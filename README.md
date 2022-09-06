# CardGame

## Installation

Requires Python3.8 and docker
> python3 -m pip install -r requirements.txt

Also requires Geckodriver for Selenium : 

 - Download Geckodriver from https://github.com/mozilla/geckodriver/releases/tag/v0.31.0
 - Extract and add the geckodriver to your PATH

Requires a Redis server to handle the chat rooms

> cd cardgame/
> 
> sudo docker run -p 6379:6379 -d redis:5
> 
> python3 manage.py runserver

## Usage

Go to `127.0.0.0:8000/game/` and create a chat room. Using another 
tab in your browser, you can chat with yourself asynchronously.

## Testing

`python manage.py test`


## Roadmap

- User system : 
  - [x] Register and login users
  - [x] Enter rooms as a user
  - [ ] Add friends


- Room system : 
  - [x] See which user sent a message
  - [x] Timestamps in messages
  - [ ] Chat history when joining another room (time limited ?)
  - [ ] Room passwords
  - [ ] Matchmaking system


- Card system : 
  - [x] Cards with health / attack / description / name
  - [x] Deck system with multiple cards
  - [ ] Card modifiers


- Game : 
  - [ ] Turn based system
  - [ ] Players have and lose HP depending on cards


... and much more