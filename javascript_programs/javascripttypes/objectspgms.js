var employee={
    eid:1001,
    name:"ajay",
    desig:"developer",
    salary:25000,

}


console.log(employee["name"]);
console.log(employee.salary);
if("exp" in employee==false){
    employee["exp"]=2
}
console.log(employee);