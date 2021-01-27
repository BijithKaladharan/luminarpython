class emp{

    constructor(id,name,age){
        this.id=id;
        this.name=name;
        this.age=age;
    }
    printemployee=()=>{
        console.log(this.id);
        console.log(this.name);
        console.log(this.age);
    
    }
}

var obj=new emp(1001,"ajay",14)
obj.printemployee()