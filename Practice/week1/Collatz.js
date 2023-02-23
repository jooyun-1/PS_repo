var answer = 0;
var num = prompt("input: ");
if(num == 1){
    answer = 0;
}
while(true){
if(num == 1){
    break;
}else if(answer > 500){
    answer = -1;
    break;
}else if(num % 2 == 0){
    num /= 2;
    answer++;        
}else{
    num = num * 3 + 1;
    answer++;
}
}
console.log(answer);