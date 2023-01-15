function solution(arr) {
    var answer = [];
    arr.splice(arr.indexOf(Math.min(...arr)),1);
    if(arr.length < 1){
        arr = [-1];
    }
    answer = arr;
    return answer;
}
console.log(solution([4,3,2,1]));