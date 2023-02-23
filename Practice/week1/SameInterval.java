package week1;

import java.util.Scanner;

public class SameInterval {
	long[] solution(int x, int n) {
        long[] answer = new long[n];
        for(int i=0;i<n;i++){
            if(i == 0){
                answer[i] = x;
            }else{
            answer[i] += answer[i-1] + x;
            }
        }
        return answer;
    }
	
	public static void main(String[] args) {
		SameInterval sol = new SameInterval();
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int n = sc.nextInt();
		System.out.println(sol.solution(x, n));
	}
}
