

let input = prompt("Ingrese un número");
let a = Number(input);

if (isNaN(a)) {
    alert("El valor ingresado no es un número");
}
else if (a < 0 && a %2 === 0) {
    alert("El número es negativo y par");
}
else if (a > 0 && a % 2 !== 0) {
    alert("El número es positivo y par");
}
else {
    alert("El número es cero");
}