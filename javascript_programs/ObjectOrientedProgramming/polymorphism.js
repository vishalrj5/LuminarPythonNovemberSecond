// method overloading
// class MyMaths{
//     add(){
//         console.log("no arg method")
//     }
//     add(num1,num2){
//         console.log("two arg method")
//     }
//     }

// var obj=new MyMaths()
// obj.add(10,20)
// obj.add()

// method over riding
class Parent{
    phone(){
        console.log("inside Parent phone method")
    }
}
class Child extends Parent{
    phone(){
        console.log("inside child phone method")
    }
}

var c=new Child()
c.phone()