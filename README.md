# CardGame

## Installation

Requires Python3.8 and docker
> python3 -m pip install -r requirements.txt
> 
> cd cardgame/
> 
> sudo docker run -p 6379:6379 -d redis:5
> 
> python3 manage.py runserver

## Usage

Go to `127.0.0.0:8000/game/` and create a chat room. Using another 
tab in your browser, you can chat with yourself asynchronously.

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