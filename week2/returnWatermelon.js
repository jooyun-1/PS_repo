function solution(n) {
    var answer = '';
    var arr = new Array();
    for(var i=0;i<n;i++){
        if(i % 2 == 0){
            arr.push("수");
        }else{
            arr.push("박");
        }
    }
    answer = arr.join('');
    return answer;
}
console.log(solution(3));
console.log(solution(4));