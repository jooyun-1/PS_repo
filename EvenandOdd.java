package week1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class EvenandOdd {
	public static String answer = "";
	String solution(int num) {
	    
	    
	    if(num % 2 ==0){
	        answer = "Even";
	    }else{
	        answer = "Odd";
	    }
	    
	    return answer;
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		EvenandOdd evenAndOdd = new EvenandOdd();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		answer = evenAndOdd.solution(num);
		System.out.println(answer);
	}
	

}



