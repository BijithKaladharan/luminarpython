class parent{
    m1(){
        console.log("inside parent")
    }
}
class subchild extends parent{
    m2(){
        console.log("inside subchild method")

    }
}
class child extends subchild{
    m3(){
        console.log("inside child")
    }

}
var c=new child();
c.m1()
c.m2()
c.m3()