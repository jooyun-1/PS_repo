import java.io.*;
import java.util.*;

/*
 *1.
 * 신맛 : S, 쓴맛 : B
 * 신맛 : 사용한 재료의 신맛의 곱, 쓴 맛 : 합
 * 신맛 - 쓴맛 차이 가장 작게
 * 2. 
 * 
 * 3. 재료 적어도 하나 사용
 */
public class Main {
	static int[] arr;
	static int[] arr2;
	static int n;
	static boolean[] isSelected;
	static int min = Integer.MAX_VALUE;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		arr = new int[n];
		arr2 = new int[n];
		isSelected = new boolean[n];
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			arr[i]  = Integer.parseInt(st.nextToken());
			arr2[i] = Integer.parseInt(st.nextToken());

		}
		subSet(0,1,0);
		System.out.println(min);
	}

	public static void subSet(int cnt, int sum,  int sum2) {
		if (cnt == n) {
			int falseCnt = 0;
			for(int i=0;i<n;i++) {
				if(isSelected[i]) continue;
				falseCnt++;
			}
			if(falseCnt == n) return;
			min = Math.min(min, Math.abs(sum - sum2));
			return;
		}
		
		isSelected[cnt] = true;
		subSet(cnt+1,sum*arr[cnt],sum2+arr2[cnt] );
		isSelected[cnt] = false;
		subSet(cnt+1,sum,sum2);
	}
}