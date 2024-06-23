
import java.io.*;
import java.util.*;

public class Main {
	static int n,m;
	static int[] arr;
	static boolean[] isSelected;
	static StringBuilder sb;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		sb = new StringBuilder();
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n+1];
		isSelected = new boolean[n+1];
		combination(1, 0);
		System.out.println(sb);
	}
	
	public static void combination(int start, int cnt) {
		if (cnt == m) {
			for (int k = 0; k < m; k++) {
				sb.append(arr[k]).append(" ");
			}
			sb.append("\n");
		} else {
			for (int i = start; i <= n; i++) {
				arr[cnt] = i;
				combination(i+1, cnt+1);
			}
		}
	}
}
