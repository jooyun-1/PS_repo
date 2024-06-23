
import java.io.*;
import java.util.*;
/*
 * 1. 후위 표기식과 각 피연산자 값 주어질 때, 계산
 * ABC*+DE/- => A + B*C - D/E
 * 
 *[A,B,C] -> [A,B*C] -> [A+B*C, D, E] D/E
 * 2. 
 * 3. 피연산자 (A~Z) 길이 < 100
 */
public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine()); // 피연산자 개수
		char[] operator = {'*', '/', '+', '-' };
		String s = br.readLine();
		Map <Character, Integer> map = new HashMap<>();
		Stack<Double> stack = new Stack<>();

		for (int i = 0; i < n ; i++) {
			map.put((char) ('A' + i), Integer.parseInt(br.readLine()));
		}
		double temp = 0;
		for (int x = 0; x < s.length(); x++) {;
			if (s.charAt(x) == '*') {
				double a = stack.pop();
				double b = stack.pop();
				temp = b * a;
				stack.push(temp);
			} else if (s.charAt(x) == '/') {
				double a = stack.pop();
				double b = stack.pop();
				temp = b / a;
				stack.push(temp);
			} else if (s.charAt(x) == '+') {
				double a = stack.pop();
				double b = stack.pop();
				temp = b + a;
				stack.push(temp);		
			} else if (s.charAt(x) == '-') {
				double a = stack.pop();
				double b = stack.pop();
				temp = b - a;
				stack.push(temp);		
			} else {
				stack.push((double)map.get(s.charAt(x)));
			}
		}
		System.out.printf("%.2f", stack.peek());;
	}
}
