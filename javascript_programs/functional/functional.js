// core lang (java)

//  lambda functio





var arr=[6,5,4,2,11,12]
arr.map(num=>num**2).forEach(num=>console.log("Internal",num)) //internal iteration

for(let num of arr){//external
    console.log("External",num)
}
// arr.sort((num1,num2)=>num1<num2?-1:1)
// console.log(arr)

//rtos
//real operating system
//c

var total=arr.reduce((o1,o2)=>o1+o2)
console.log(total)
