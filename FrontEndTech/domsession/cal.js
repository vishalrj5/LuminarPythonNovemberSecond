



function displayBox(number){
    let txt=document.querySelector('#inputs');
    txt.value+=number;

}



function clearBox(){
    let txt=document.querySelector('#inputs').value="";
}


function calculate(){

    let expression=document.querySelector("#inputs");
    let result=eval(expression.value)
    expression.value=result;

}