function solution(phone_number) {
    var answer = '';
    var arr = new Array();
    arr = phone_number.split("");
    for(var i=0;i<arr.length-4;i++){
            arr[i] = '*';
    }
    answer = arr.join('');
    return answer;
}
console.log(solution(prompt("input: ")));