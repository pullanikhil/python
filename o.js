
/*object creation
let emp ={eid: 101,dep: "incometax"} 
let emp1 ={eid: 102,dep:"accounts_officer"}
var emp2 ={eid: 103,dep:"hr"}
//here emp is an object that stores values such as strings and numbers 
console.log(emp.eid,emp.dep)
// nested objects is nothing but object within a object
 const investor = {
  name:"jun_jun_wala",
  age: 75,
  greet:function(){return ("good investor");},
  investment: {
    tata_motors: 1500,
    tata_steel:2900,}
 }//
 console.log(investor.investment,investor.greet)

let person = {
  name:'nikhil',
  age:25,
  place:'banglore',
  company:'senseblue'
};
//acesseing property
console.log(person["name"],person["age"],person["place"],person["company"]);

//nested objects
let players = {
  name:"teja",
  age:21,
  sports:{
    football:"outdoorgame",
    cricket:"outdoorgame",
    swimming:"indoorgame"
}
}
//acesseing the properties of players object 
console.log(players.sports);
//acesseing the properties of sports object
console.log(sports.cricket);

/*const player1 ={
  name:'vikram',
  age: 27,
  games: "cricket",
  //using function as a value
  //greet:function(){console.log("cricket player")}

}*/

const cars =
{
  hero:"honda",
  //acess property of setter
 set changename(newname){
  this.hero = newname;
 }
};
console.log(cars.hero);//honda
// change(set) object property using a setter
cars.changename = "toyota";
console.log(cars.hero);//toyota






