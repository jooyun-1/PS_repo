var x = prompt();
var answer = true;
var x_string = x.toString();
var arr = new Array();
var sum = 0;
 for(var i=0;i<x_string.length;i++){
    arr[i] = Number(x_string.charAt(i));
    sum += arr[i];
}
if(x % sum == 0){
    answer = true;
}else{
    answer = false;
}    

console.log(answer);