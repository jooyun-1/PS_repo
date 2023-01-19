function solution(n) {
    var answer = 0;
    let temp = n.toString(3);
    answer = temp.split('').reverse().join('');
    
    return parseInt(answer,3);
}

console.log(solution(45));