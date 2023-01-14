var answer = 0;
var n = prompt("enter");
var n_string = n.toString();
var arr = new Array();
for(var i=0;i<n_string.length;i++){
    arr[i] = Number(n_string.charAt(i));
}
arr.sort(function(a,b){
    return b-a;         
});
answer = Number(arr.join(""));
alert(answer);