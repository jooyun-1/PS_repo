package week1;

import java.util.Scanner;

public class DivisorSum {
	int solution(int n) {
        int answer = 0;
        for(int i=1;i<=n;i++){
            if(n%i==0){
                answer += i;
            }
        }
        return answer;
    }
	
	public static void main(String[] args) {
		DivisorSum ds = new DivisorSum();
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println(ds.solution(n));
	}
}
