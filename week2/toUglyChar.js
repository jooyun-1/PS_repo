function solution(s) {
    var answer = '';
    var arr = s.split(' ');

    for(var i=0;i<arr.length;i++){
        var len = arr[i].length;
        for(var j=0;j<len;j++){
             if(j % 2 == 0){
                 answer += arr[i][j].toUpperCase();
             }else{
                answer += arr[i][j].toLowerCase();
             }
        }
        if(i < arr.length - 1){
        answer += ' ';
        }
    }
    return answer;
}
console.log(solution("try hello world"));
