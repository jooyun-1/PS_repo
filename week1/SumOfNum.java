package week1;

import java.util.Scanner;

public class SumOfNum {
	int solution(int n) {
        String s = Integer.toString(n);
        int[] arr = new int[s.length()];
        int answer = 0;
        for(int i=0;i<s.length();i++){
            arr[i] = Character.getNumericValue(s.charAt(i));
            answer += arr[i];
        }
        return answer;
    }
    
    public static void main(String[] args) {
    	SumOfNum sol = new SumOfNum();
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println(sol.solution(n));
	}
}
