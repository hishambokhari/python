var firstName = prompt("Hello and Welcome. please enter your first name: ");
var lastName = prompt("Last Name: ");
var age = prompt("What is your age?");
var height = prompt("What is your height?");
var petName = prompt("What is your pets name?");

var nameCond = null
var ageCond = null
var heightCond = null
var petCond = null

if (firstName[0] === lastName[0]){
  nameCond = true;
} else {
  nameCond = false;
}

if (age > 20 && age < 30) {
  ageCond = true;
} else {
  ageCond = false;
}

if (height > 170){
  heightCond = true;
} else {
  heightCond = false;
}

if (petName[petName.length-1] === "y"){
  petCond = true;
} else {
  petCond = false;
}

if (nameCond && heightCond && ageCond && petCond){
  console.log("Welcome Comrade! You have passed the spy test")

} else {
  console.log("Nothing to see here!")
}