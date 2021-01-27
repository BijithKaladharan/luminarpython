var employee={
    eid:101,
    name:"ajay",
    design:"developer",
    salary:2300
}
// console.log(employee)

console.log(employee["name"]);
console.log(employee.salary);
console.log(employee.name);
if("exp" in employee==false){
    employee["exp"]=2
}
console.log(employee)