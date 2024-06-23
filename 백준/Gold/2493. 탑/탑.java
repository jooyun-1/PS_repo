import java.io.*;
import java.util.*;

/*
 * 일직선에 N개의 높이로 서로 다른 탑을 차례로 세우고 송신기 설치
 * 송신기 : 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사
 * 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신 가능
 *  
 */
//9 9 7 7 4
//0 0 2 2 4
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder sb = new StringBuilder();
		Stack<Integer> stack = new Stack<>();
		Stack<Integer> index = new Stack<>();
		
		int n = Integer.parseInt(st.nextToken());  //탑의 개수
		int k = 0;
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < n; i++) {
			k = Integer.parseInt(st.nextToken());
			while (true) {
				if (!stack.empty()) {
					int top = stack.peek();
					if (top > k) {
						System.out.print(index.peek() + " ");
						stack.push(k);
						index.push(i+1);
						break;
					} else { 
						stack.pop();
						index.pop();

					}
				} else { 
					System.out.print("0 ");
					stack.push(k);
					index.push(i+1);
					break;
		}
		
	}
		}
	}
}