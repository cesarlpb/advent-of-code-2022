// Day 2 - https://adventofcode.com/2022/day/2

// X Determinar ganador, empate o perdida
// X Usando nuestra elección y el resultado -> puntuación
// X Vamos sumando las puntuaciones

// Leer del input del txt
let input = "";
const fs = require('fs');

fs.readFile('input-2.txt', 'utf8', (err, data) => {
  if (err) throw err;
  input = data.split('\n');

  // Opcional: quitar espacios en blanco
  for (let i = 0; i < input.length; i++) {
    input[i] = input[i].replace(" ", "");
  }

  // Parte 1 - función que determina ganador, empate o perdida y retorna puntos
  const puntos = [];
  // Oponente -> A: piedra, B: papel, C: tijeras
  const oponenteDict = { A: "piedra", B: "papel", C: "tijeras" };
  // Elección -> X: piedra, Y: papel, Z: tijeras
  const eleccionDict = { X: "piedra", Y: "papel", Z: "tijeras" };

  // Lógica de juego
  // Piedra vence a Tijeras, Tijeras vence a Papel y Papel vence a Piedra
  // Si el oponente es igual a la elección, es un empate
  function juego(oponente, nosotros) {
    const eleccionOponente = oponenteDict.oponente; // A, B o C
    const eleccionNuestra = eleccionDict.nosotros; // X, Y o Z
    // Caso de empate -> índice 1 en puntos_resultado
    if (eleccionOponente == eleccionNuestra) {
      return 1;
    }
    // Caso de perder -> índice 0 en puntos_resultado
    // Rehacer esto comparando dos listas
    else if (
      (eleccionOponente == "piedra" && eleccionNuestra == "tijeras") ||
      (eleccionOponente == "tijeras" && eleccionNuestra == "papel") ||
      (eleccionOponente == "papel" && eleccionNuestra == "piedra")
    ) {
      return 0; // perder -> índice 0 en puntos_resultado
    }
    // Caso de ganar -> índice 2 en puntos_resultado
    else {
      return 2;
    }
  }

  // Test de test.txt
  // Sabemos que test.txt tiene datos que suman 15 según las reglas de puntos del juego
  // A Y papel=2 2+6 = 8
  // B X piedra=1 1+0 = 1
  // C Z tijeras=3 3+3 = 6
  // Total = 15
  const nuestrasElecciones = [];
  const eleccion = { X: "piedra", Y: "papel", Z: "tijeras" };
  for (const partida of input) {
  const oponente = partida[0]; // A, B o C
  const nosotros = partida[1]; // X, Y o Z
  nuestrasElecciones.push(nosotros);
  puntos.push(juego(oponente, nosotros));
  // puntos_forma_elegida = { "piedra": 1, "papel": 2, "tijeras": 3 }
  // puntos_resultado = { 0: 0, 1: 3, 2: 6 }
  }
  
  // puntos esta correcto
  // sum(puntos) == 15
  const puntosTotal = puntos.reduce((a, b) => a + b, 0);
  console.log(puntosTotal);
  });

// TODO: El número que calcula no es correcto, revisar.
  // Calcula un 2500 en vez de 14060 (en el caso 2)