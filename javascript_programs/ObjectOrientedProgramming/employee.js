class employee{
    constructor(id,name,salary,desig){
        this.id=id;
        this.name=name;
        this.salary=salary;
        this.desig=desig;
    }
    printPerson=()=>{
        console.log(this.id);
        console.log(this.name);
        console.log(this.salary);
        console.log(this.desig);
    }
}

var obj1=new employee(001,"XD",20000,"Developer");
obj1.printPerson();