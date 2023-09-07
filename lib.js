//building a library catalog system.
 constructor:
class book {
  constructor(title, author, year) {
    this.title=title;
    this.author=author;
    this.year=year;
  }
}
const book1 = new book('The Little Book of Common Sense Investing ','Jack Bogle',1997);
const book2 = new book('How to Make Money in Stocks','William J',2000);
const book3 = new book('One Up On Wall Street', 'Peter Lynch.',2009);

const displaybook_info =(book) =>
{console.log(`title:${book.title}`);
console.log(`author:${book.author}`);
console.log(`year:${book.year}`);}
displaybook_info(book3);

Create a emp constructor function that initializes emp objects with properties like name and an array to store their grades_performance:
function emp(name){
  this.name = name;
  this.grade = [];
}
const emp1 = new_emp('nikhil');
const emp2 = new_emp('teja');
const emp3 = new_emp('nishanth');

const calculate_avg_grade =(emp)=>{
  const totalgrades = emp.grades.
}

constructor function
function calculator(){
  this.result=0;
  this.add = (num)=>{
    this.result +=num;
  };
  this.subract = (num)=>{this.result -=num;
  };
  this.multiply =(num)=>{this.result *=num;
  };
  this . divide =(num)=>{if(num!==0){this.result/=num;}else
  {console.log("error:zero division error");}
};
}    
create a sample calculator object
const mycalculator =  first_calculator();
mycalculator.add(10);
mycalculator.subract(5);
mycalculator.multiply(2);
mycalculator.divide(0);
console.log("result:",mycalculator.result);

const person = {
  name: 'Sam',
  age: 30,
  using function as a value
  greet: function() { console.log('hello') }
}

person.greet();  
console.log(person.age);