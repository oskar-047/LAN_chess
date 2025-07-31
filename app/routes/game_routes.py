from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app_config import templates
from game.game import create_new_game, get_game_board, tile_clicked, get_game_posible_moves

router = APIRouter()

@router.get("/get-board")
def get_board():
    return get_game_board()

@router.get("/get-posible-moves")
def get_posible_moves():
    return get_game_posible_moves()

# Endpoint to create a new game and return the board
@router.get("/new-game")
def new_game():
    create_new_game()
    return Response(status_code=204)

@router.get("/clic")
def tile_clic(row: int, col: int):
    tile_clicked(row, col)
    return Response(status_code=204)


# Endpoint activated when the user clics a tile
#@router.get("/user-click/{x}/{y}")