
import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int[] arr = new int[n+1];
		int[] sums = new int[n+1];
		arr[0] = 0;
		for (int i = 1; i <= n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			sums[i] += arr[i]+sums[i-1];
//			System.out.println(sums[i]);
		}
		for (int k = 0; k < m; k++) {
			st = new StringTokenizer(br.readLine());
//			int sum = 0;
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			System.out.println(sums[b]-sums[a-1]);
//			for (int i = a; i <= b; i++) {
//				sum += arr[i];
//			}

		}

	}
}
