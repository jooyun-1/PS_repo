import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();		
		for (int i = 0; i < T; i++) {

			boolean flag = true;
			String s = br.readLine();
			Stack<Character> stack = new Stack<>();
			
			for (int a = 0; a < s.length(); a++) {
				if (s.charAt(a) == '(') {
					stack.add(s.charAt(a));
				}else {
					if (stack.size() != 0) {
						stack.pop();
					} else {

						flag = false;
						break;
					}
				}
			}
			if (flag == true && stack.size() == 0) {
				sb.append("YES").append("\n");
			} else {
				sb.append("NO").append("\n");
			}

		}
		System.out.print(sb);
	}
}
