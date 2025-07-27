from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from game.game import chessboard
from app_config import templates

router = APIRouter()

@router.get("/get-board")
def get_board():
    return chessboard