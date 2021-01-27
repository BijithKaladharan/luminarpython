class person{

    constructor(age,name){
        this.age=age;
        this.name=name;
}

printperson=()=>{
    console.log(this.name);
    console.log(this.age)
}
}
//instance variable initialization
//__init__()
//

var obj1=new person(25,"ajay")
obj1.printperson()