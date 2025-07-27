# LAN Chess (PROJECT IN PROGRESS)

## Description
A personal project: a two-player chess game playable over LAN.  
Created to learn how to structure a professional project and explore WebSocket integration along with backend/frontend interaction concepts.


## Features

- Playable over LAN
- Uses websocket for synchronization

## Tech Stack

- Python (FastAPI)
- HTML, CSS, JavaScript
- WebSocket (LAN)
- Jinja2 for frontend templates

## Installation

```bash
git clone https://github.com/oskar-047/LAN_chess.git
cd LAN_chess
# setup environment
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0
```
