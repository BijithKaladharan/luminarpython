//method overloading
// class mymaths{
//     add(){
//         console.log("no arg method")
//     }
//     add(num1,num2){
//         console.log("two arg method")
//     }
// }

// var obj=new mymaths()
// obj.add(10,20);
// obj.add();

//method overriding
class parent{
    phone(){
        console.log("inside parent phone method")
    }
}
class child extend parent{
    phone(){
        console.log("inside child phone method")
    }
}
var c=new child()
c.phone()
