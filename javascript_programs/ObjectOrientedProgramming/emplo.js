class Parent{
    m1(){
        console.log("inside parent")
    }
}
class subChild extends Parent{

        m2(){
            console.log("inside subchild")
        }
}
class child extends Subchild{

    m3(){
        console.log("inside child")
    }
}

var c=new Child();
c.m1();
c.m2()
c.m3()

// Bank application
// method overloading , method overriding
// dom