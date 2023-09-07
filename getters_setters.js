const food = {
  itemName: 'dosa',
    // accessor property(getter)
  get getitem() {
      return this.itemName;
  },
  //accessor property(setter)
      set changeitems (newitems){
          this.itemName =newitems;
  }
};
// accessing data property
console.log(food.itemName); 
// accessing getter methods
console.log(food.getitem)
// change(set) object property using a setter
food.changeitems = 'deserts';
console.log(food.itemName);