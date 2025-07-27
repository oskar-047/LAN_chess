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

            tile.addEventListener("click", () => tileClick(row, col));

            chessboard.appendChild(tile);
        }
    }
}


// Function that initializes all the chessboard pieces
async function initializePieces(){
    const pieces = await fetchChessboard();
    alert(JSON.stringify(pieces));
}


async function fetchChessboard(){
    // await pauses the function until the fetch is resolved
    const result = await fetch("/get-board");

    // await is used because result.json() returns a promise, the await waits to the promise being resolved
    const board = await result.json();

    return board;
}


function tileClick(row, col) {
    alert(`${row} ${col}`);
}