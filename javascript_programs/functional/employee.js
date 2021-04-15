var employee=[
    {eid:100,names:"ajay",salary:2500,exp:2},
    {
        eid:101,names:"vijay",salary:2300,exp:2},
    {
        eid:102,names:"jjay",salary:2600,exp:2
    },
    {
        eid:103,names:"xjay",salary:2400,exp:2
    },
    {
        eid:104,names:"bjay",salary:2700,exp:2
    },
]

//employee.forEach(emp=>console.log(emp.names))


//convert all employee  name into uppercase
// print employeee according with their salary
// dom
// ajax
// django

//toUpperCase()
// var XD=[]
// for(z in employee){
//     XD.push(employee[z].names)
// }

// console.log(XD)
// for(i in XD){
    
//     console.log(XD[i].toUpperCase())

// }

//Print employee according to their salary
// var sal=[]
// function compare(a,b) {
//     var salaryA = new salary(a.salary);
//   var salaryB = new salary(b.salary);
//   if (salaryA > salaryB)
//     return -1;
//   if (salaryA < salaryB)
//     return 1;
//   return 0;
// }

// employee[0].sort(compare);
// console.log(employee);


//filtering employees who have salary >2500

// var emp=employee.filter(o=>o.salary>2500)
// console.log(emp)

// var maxsal=employee.map(obj=>obj.salary).reduce((o1,o2)=>o1>o2?o1:o2)
// console.log(maxsal)


employee.sort((o1,o2)=>o1.salary>o2.salary?-1:1).forEach(o => console.log(o.names))




// implmnt all qstion using js


// arrow fn
// map
// filter
// reduce
// sort