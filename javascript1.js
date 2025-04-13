//1-2
console.log("I'm printing to console!")
prompt("Type your name.");
alert("Hello, " + prompt + "!");
//3
let num1 = Number(prompt("Enter first number:"));
let num2 = Number(prompt("Enter second number:"));
let num3 = Number(prompt("Enter third number:"));

let summ = num1 + num2 + num3;
let product = num1 * num2 * num3;
let average = summ / 3;

document.write("Sum: "+ summ + "<br>");
document.write("Product: " + product + "<br>");
document.write("Average: " + average.toFixed(2));
//4
let name = prompt("Enter your name:");
let houseNumber = Math.floor(Math.random() * 4);

let house;
if (houseNumber === 0) house = "Gryffindor";
else if (houseNumber === 1) house = "Slytherin";
else if (houseNumber === 2) house = "Hufflepuff";
else house = "Ravenclaw";

document.write(name + ", you are " + house + ".");
//5
let year = Number(prompt("Enter a year:"));
let isLeap = false;

if (year % 4 === 0) {
  if (year % 100 !== 0 || year % 400 === 0) {
    isLeap = true;
  }
}

if (isLeap) {
  document.write(year + " is a leap year.");
} else {
  document.write(year + " is not a leap year.");
}
//6
if (confirm("Should I calculate the square root?")) {
  let num = Number(prompt("Enter a number:"));
  if (num < 0) {
    document.write("The square root of a negative number is not defined");
  } else {
    let sqrt = Math.sqrt(num);
    document.write("The square root of " + num + " is " + sqrt.toFixed(2));
  }
} else {
  document.write("The square root is not calculated.");
}
//7
let rolls = Number(prompt("How many dice rolls?"));
let sum = 0;

for (let i = 0; i < rolls; i++) {
  let roll = Math.floor(Math.random() * 6) + 1;
  sum += roll;
}

document.write("The sum of dice rolls is: " + sum);