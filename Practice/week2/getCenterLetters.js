function solution(s) {
    var answer = '';
    var len = s.length;
    var arr = new Array();
    arr = s.split('');
    if(len % 2 == 0){
        answer =  arr[len/2 - 1] + arr[len/2]
    }else{       
        answer = arr[Math.floor(len/2)];
    }
    return answer;
}
console.log(solution(prompt("input: ")));