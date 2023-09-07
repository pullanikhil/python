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