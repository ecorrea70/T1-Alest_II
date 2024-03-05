const fs = require("fs");

const filePath = "teste.txt";

fs.readFile(filePath, "utf-8", (error, data) => {
  if (error) {
    console.error("Erro ao ler o arquivo:", error.message);
    return;
  }
  console.log("Conteúdo do arquivo:", data);
});
