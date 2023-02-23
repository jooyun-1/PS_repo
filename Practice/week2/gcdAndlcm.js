function solution(n, m) {
    var answer = [];
    var gcd = cal_gcd(n,m);
    var lcm = m * n / gcd;
    return [gcd, lcm];
}

function cal_gcd(a,b){
    if(b == 0) return a;
    return a > b ? cal_gcd(b, a % b) : cal_gcd(a, b % a);
}
console.log(solution(2,5));
