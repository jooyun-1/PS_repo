function solution(price, money, count) {
    var answer = -1;
    var sum = 0;
    var after_price = 0;
    
    for(var i=1;i<=count;i++){
        sum += price*i;
    }
    if(money - sum >0){
        answer = 0;
    }else{
        answer = sum - money;
    }
    return answer;
}
console.log(solution(3,20,4));