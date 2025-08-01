// -------- const -------------
const chessboard = document.getElementById("chessboard");



// The chessboard color
const chessboardColor = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
];

startGame();

// All the logic to initialize a game
function startGame(){
    createGame();
    createChessboard();
    initializePieces();
}



// A function to create the chessboard tiles
function createChessboard() {
    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            let tile = document.createElement("div");

            tile.classList.add("tile");

            tile.dataset.row = row;
            tile.dataset.col = col;

            tile.style.backgroundColor = chessboardColor[row][col] ? "#D18B47" : "#FFCE9E";

            let pieceImg = document.createElement("img");
            pieceImg.classList.add("piece-img");

            tile.appendChild(pieceImg);

            tile.addEventListener("click", () => tileClick(row, col));

            chessboard.appendChild(tile);
        }
    }
}


function createGame() {
    fetch("/new-game");
}


// Function that initializes all the chessboard pieces
async function initializePieces(){
    const board = await getChessboard();

    for(let row = 0; row <8; row++){
        for(let col = 0; col <8; col++){
            
            let pieceImg = document.querySelector(`[data-row='${row}'][data-col='${col}']`).firstElementChild;

            if (board[row][col] == 0){
                pieceImg.src = "";
                continue;
            }

            pieceImg.src = `static/img/${board[row][col]}.png`;
            
        }
    }

    // alert(JSON.stringify(pieces));
}

async function showPosibleMoves(){
    
    const posibleMoves = await getPosibleMoves();

    // Goes through all the chessboard marking the posible moves
    for(let row = 0; row < 8; row++){
        for(let col = 0; col < 8; col++){
            let tile = document.querySelector(`[data-row='${row}'][data-col='${col}']`);
            if (posibleMoves[row][col] == 1){
                tile.style.backgroundColor = "green";
            } else {
                tile.style.backgroundColor = chessboardColor[row][col] ? "#D18B47" : "#FFCE9E";
            }
        }
    }
}

async function getChessboard(){
    // await pauses the function until the fetch is resolved
    const result = await fetch("/get-board");

    // await is used because result.json() returns a promise, the await waits to the promise being resolved
    const board = await result.json();

    return board;
}

async function getPosibleMoves(){
    const result = await fetch("/get-posible-moves");

    const posibleMoves = await result.json();

    return posibleMoves;
}


function tileClick(row, col) {
    // alert(`${row} ${col}`);
    fetch(`/clic?row=${row}&col=${col}`);
}




// Polling the server for updates
setInterval(async () => {
    initializePieces();
    showPosibleMoves();
    //let posibleMoves = await getPosibleMoves();
}, 200);