class Person{
    
    constructor(age,name){
        this.age=age;
        this.name=name;
    }
    printPerson=()=>{
        console.log(this.name);
        console.log(this.age);
    }
}
// instance variable
// _init_()
var obj1=new Person(25,"ajay")
obj1.printPerson()


