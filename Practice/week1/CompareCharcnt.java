package week1;

import java.util.Scanner;

public class CompareCharcnt {
    boolean solution(String s) {
        
        int p_cnt = 0;
        int y_cnt = 0;
        
        for(int i=0;i<s.length();i++){
            if(s.charAt(i) == 'p' || s.charAt(i) == 'P'){
                p_cnt++;
            }else if(s.charAt(i)== 'y' || s.charAt(i) == 'Y'){
                y_cnt++;
            }
        }
        if(p_cnt == y_cnt){
            return true;
        }else{
            return false;
        }
    }
    
    public static void main(String[] args) {
    	CompareCharcnt sol = new CompareCharcnt();
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		System.out.println(sol.solution(s));
	}
}
