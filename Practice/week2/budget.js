function solution(d, budget) {
    var answer = 0;
    d.sort(function(a,b){
        return a-b;
          });
    let sum = 0;
    for(let i=0;i<d.length;i++){
        sum += d[i];
        if(sum <= budget){
            answer++;
        }else{
          break;
        }
    }
    return answer;
}
console.log(solution([1,3,2,5,4],9));