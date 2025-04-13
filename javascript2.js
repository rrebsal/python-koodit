//1
let number = [];

for (let i = 0; i < 5; i++) {
  number.push(Number(prompt("Enter number " + (i + 1) + ":")));
}

for (let i = number.length - 1; i >= 0; i--) {
  console.log(number[i]);
}

//2

let num = Number(prompt("Enter number of participants:"));
let names = [];

for (let i = 0; i < num; i++) {
  names.push(prompt("Enter name of participant " + (i + 1) + ":"));
}

names.sort();

document.write("<ol>");
for (let name of names) {
  document.write("<li>" + name + "</li>");
}
document.write("</ol>");

//3

let dogs = [];

for (let i = 0; i < 6; i++) {
  dogs.push(prompt("Enter name of dog " + (i + 1) + ":"));
}

dogs.sort().reverse();

document.write("<ul>");
for (let dog of dogs) {
  document.write("<li>" + dog + "</li>");
}
document.write("</ul>");
//4

let numbers = [];
let input;

do {
  input = Number(prompt("Enter a number (0 to stop):"));
  if (input !== 0) numbers.push(input);
} while (input !== 0);

numbers.sort((a, b) => b - a);

for (let number of numbers) {
  console.log(number);
}
//5

let numberss = [];
let inputs;
let duplicate = false;

while (!duplicate) {
  inputs = Number(prompt("Enter a number:"));
  if (numberss.includes(inputs)) {
    duplicate = true;
    alert("Number already entered!");
  } else {
    numbers.push(inputs);
  }
}

numberss.sort((a, b) => a - b);
for (let num of numberss) {
  console.log(num);
}

//6

function rollDie() {
  return Math.floor(Math.random() * 6) + 1;
}

document.write("<ul>");
let result;
do {
  result = rollDie();
  document.write("<li>" + result + "</li>");
} while (result !== 6);
document.write("</ul>");