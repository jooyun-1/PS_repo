

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static boolean[] isSelected;
	static int[] arr;
	static int n, m;
	static StringBuilder sb;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		sb = new StringBuilder();
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		isSelected = new boolean[n+1];
		arr = new int[n+1];
		permutation(0);
		System.out.println(sb);
	}
	
	public static void permutation(int cnt) {
		if (cnt == m) {
			for (int k = 0; k < m; k++) {
				sb.append(arr[k]).append(" ");
//				System.out.print(arr[k] + " ");
				
			}
			sb.append("\n");
		} else {
			for (int i = 1; i <= n; i++) {
				if(isSelected[i]) continue;
				arr[cnt] = i;
				isSelected[i] = true;
				permutation(cnt + 1);
				isSelected[i] = false;
			}
		}
	}
}
