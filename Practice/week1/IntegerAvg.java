package week1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class IntegerAvg {
	double solution(int[] arr) {
        double sum = 0;

        for(int i=0; i<arr.length; i++){
            sum += arr[i];
            System.out.println(arr[i]);
        }
        double answer = 0;
        answer = sum / arr.length;

        return answer;
    }
	
	public static void main(String[] args) throws IOException {
		IntegerAvg integerAvg = new IntegerAvg();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), ",");

		int[] arr = new int[st.countTokens()];
		for(int a=0;a<arr.length;a++) {
			arr[a] = Integer.parseInt(st.nextToken());
		}
		System.out.println(integerAvg.solution(arr));
	}
}
