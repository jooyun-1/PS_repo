function solution(n, arr1, arr2) {
    var answer = [];
    //arr1, arr2 => 2진법
    // 1 -> #, 0 -> ' '
    //or연산? (arr1, arr2)
    let biArr1 = [];
    let biArr2 = [];
    for(let j=0;j<arr2.length;j++){
        let tempArr = [];
        let x = arr2[j].toString(2);
        for(let m=0;m<n-x.length;m++){
            tempArr.push('0');
        }
        tempArr.push(x);
        biArr2.push(tempArr.join(''));
    }
    for(let k=0;k<arr1.length;k++){
        let tempArr = [];
        let x = arr1[k].toString(2);
        for(let i=0;i<n-x.length;i++){
            tempArr.push('0');
        }
        tempArr.push(x);
        biArr1.push(tempArr.join(''));
    }
    
    for(let a=0;a<n;a++){
        let str = '';
        for(let b=0;b<n;b++){
            if(biArr1[a][b] === '0' && biArr2[a][b] === '0'){
                str += ' ';
            }else{
                str += '#';
            }
        }
        answer.push(str);
    }
    return answer;
}