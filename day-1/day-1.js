// Day 1 - https://adventofcode.com/2022/day/1

// Leer input de input-1.txt
// Leer los grupos de números separados por \n\n
// Cada grupo es un "elfo" que tiene que sumar los números
// Debemos registrar la suma de cada elfo -> "calorías" -> int
// Hallamos la suma máxima de calorías -> int

// Parte 1: leer input
let input = "";
const fs = require('fs');

fs.readFile('input-1.txt', (err, data) => {
    if (err) throw err;
    input = data.toString().split('\n\n');
    // console.log(input);  // comprobamos el txt

    // Parte 2: procesar input -> sumamos cada grupo y lo guardamos en una lista
    let calorias = [];
    for (let grupo of input) {
        calorias.push(grupo.split().reduce((sum, x) => sum + parseInt(x), 0));
    }

    // Parte 3: hallamos la suma máxima de calorías
    let maximo = Math.max(...calorias);
    console.log("Máximo: " + maximo);    // máximo de la lista

    // Segunda parte - hallamos las 3 máximas calorías y la suma de ellas
    let topThree = calorias.sort((a, b) => b - a).slice(0, 3);
    console.log("Top 3: " + topThree); // lista con los 3 máximos
    let sum = topThree.reduce((sum, x) => sum + x, 0);
    console.log("Máximo de top 3: " + sum); // suma de los 3 máximos
});

// TODO: revisar por qué el máximo global no lo encuentra bien, coloca 65573 en vez de 70764
