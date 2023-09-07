
 var array1=["maruti","honda","skoda","mahindra","kia"]
 var array2=["hero","yamaha","enfield"]
 console.log("The array 1 is: ",array1,"\nThe 3rd element of array1 is : ",array1[2],"\nThe index of honda in array1 is:",array1.indexOf('honda'),"\npop element ",array1.pop(),"\npush element",array1.push("7"),"\n array 1",array1)

for(let i = 3;i!=5;++i)
{
  console.log("for Loop:",i)
}







 /*var even_numbers=4;
 while(even_numbers <=40)
 {
   console.log("While loop : ",even_numbers)
   even_numbers%2==0;
   even_numbers+=2;
 }*/

 let odd_numbers = 1;
 do
 {
  console.log("do while The odd numbers are : ",odd_numbers)
  odd_numbers = odd_numbers+2;
 }while(odd_numbers<=30)
//map 
 const values = [25,36,49,64];
 console.log(values.map(Math.sqrt));

age =25
if(age>20)
{
  console.log("person is elgible to drink alchol")
}
else
{
console.log("not elgible to drink alchol")
}



console.log(array1.pop())
console.log(array1.shift())
console.log(array2.unshift("thar"))
console.log(array1.push("bmw"))

let array3=array1
array1=array2
array2=array3
console.log(array1)
console.log(array2)

let cars= ["BMW","AUDI","BENZ","Ferrari","BENTLY","LAMBORGINI"]
console.log("The slice of cars is :",cars.slice(2,5))


var x;
for(x=0;x<=5;x++)
console.log(x);

//let even_numbers for if condition
for(let e=0;e<=20;e++){
  if(e % 2 === 0){
 console.log(e);}}
// condition for while statement 
 currenthour = 7;
if(currenthour>=5&& currenthour<=12)
{
  console.log("good morning!");
}
else if(currenthour>12&& currenthour<17)
{
  console.log("good afternoon!");
}
else if (currenthour>17 && currenthour<21)
{console.log("good evening!");}
else{console.log("good night");
}
console.log(currenthour)

const numbers = [2,3,4,5,6,7];
const even_numbers =numbers.filter(function(number){return number %2   === 0;});
console.log(even_numbers);
//constructor function
class person {
  constructor(name, age, mailid) {
    this.name = name;
    this.age = age;
    this.mailid = mailid;
    this.greet = function () {
      if (this.name === "nikhil") {
        return "hi";
      }
      else {
        return "hello";

      }
    };
  }
}

  // create objects
  const p1 = new person("nikhil",25,"pnikhil2809@gmail.com");
  const p2 = new person("rakesh",28,"rakesh0405@gmail.com");
  const p3 = new person()
// acesses properties
console.log(p1.name,p1.age,p1.mailid,p1.greet());
console.log(p2.name,p2.age,p2.mailid,p2.greet());