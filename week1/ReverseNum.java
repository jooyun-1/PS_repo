package week1;

import java.util.Scanner;

public class ReverseNum {
    int[] solution(long n) {
        String s = Long.toString(n);
        int[] answer = new int[s.length()];
        int j = 0;
        for(int i=s.length()-1;i>=0;i--){            
            answer[j++] = Character.getNumericValue(s.charAt(i));
        }
        return answer;
    }
    
    public static void main(String[] args) {
    	ReverseNum sol = new ReverseNum();
		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
	}
}
