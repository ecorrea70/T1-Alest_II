const fs = require("fs");

const filePath = "casos-de-teste/teste.txt";
const initial_char = "-";
let currentX = 0;
let currentY = 0;
let counter = 0;
const data = fs.readFileSync(filePath, "utf-8");
const rows = data.split("\n");

function findInitialLine(initial_char) {
  for (let indexRow = 0; indexRow < rows.length; indexRow++) {
    const row = rows[indexRow];

    if (row.charAt(0) === initial_char) {
      console.log(`Caractere inicial encontrado na linha ${indexRow + 1}`);
      currentX = indexRow;
      break;
    }
  }
}

findInitialLine(initial_char);

function moveLeft() {
  if (currentY > 0) {
    currentY--;
  }
}

function moveRight() {
  if (currentY < rows[currentX].length - 1) {
    currentY++;
  }
}

function moveUp() {
  if (currentX > 0) {
    currentX--;
  }
}

function moveDown() {
  if (currentX < rows.length - 1) {
    currentX++;
  }
}

while (rows[currentX][currentY] !== "#") {
  const currentChar = rows[currentX][currentY];

  switch (currentChar) {
    case "-":
      moveRight();
      break;

    default:
      if (!isNaN(Number(currentChar))) {
        counter += Number(currentChar);
      }
      moveRight();
      break;
  }
}

console.log(
  `Encontrou o caractere '#' na linha ${currentX + 1}, coluna ${currentY + 1}`
);
console.log(counter);
