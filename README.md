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

## Contents

- Async chat rooms

## Roadmap

- User system : 
  - Register and login users
  - Enter rooms as a user


- Chat system : 
  - See which user sent a message
  - Chat history when joining another room (time limited ?)
  - Timestamps in messages


- Card system : 
  - TBD