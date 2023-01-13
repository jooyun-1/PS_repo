package week1;

import java.util.Scanner;

public class IntegerSqrt {
    long solution(long n) {
        long answer = 0;
        int x = (int)Math.sqrt(n);
        if(Math.pow(x,2) == n){
            answer = (long)Math.pow(x+1,2);
        }else{
            answer = -1;
        }
        return answer;
    }
    
    public static void main(String[] args) {
    	IntegerSqrt sol = new IntegerSqrt();
		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		System.out.println(sol.solution(n));
	}
}
