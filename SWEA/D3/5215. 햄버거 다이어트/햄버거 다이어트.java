
import java.io.*;
import java.util.*;

public class Solution {
	static int[][] arr;
	static int answer, N, L;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int t =1; t <= T; t++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			L = Integer.parseInt(st.nextToken());
			arr = new int[N][2];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				arr[i][0] = Integer.parseInt(st.nextToken());
				arr[i][1] = Integer.parseInt(st.nextToken());
			}
			
			answer = 0;
			subSet(0, 0, 0);
			System.out.println("#" + t + " " + answer);
		}
	}
	
	public static void subSet(int index, int score, int calorie) {
		if (calorie > L) return;
		if (calorie <= L) {
			answer = Math.max(answer, score);
		}
		if (index == N) return;
		
		subSet(index + 1, score + arr[index][0], calorie + arr[index][1]);
		subSet(index + 1, score, calorie);
	}
}
