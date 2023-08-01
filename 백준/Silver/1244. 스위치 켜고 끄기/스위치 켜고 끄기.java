
import java.io.*;
import java.util.*;

/*
 * 남 : 스위치 번호가 자기가 받은 수의 배수이면 상태 바꿈
 * 여 : 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간의 상태 바꿈
 */
public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[n];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < arr.length; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		int num = Integer.parseInt(br.readLine()); //학생 수
		int[][] types = new int[num][2];
		for (int k = 0; k < num; k++) {
			st = new StringTokenizer(br.readLine());
			int gender = Integer.parseInt(st.nextToken());
			int number = Integer.parseInt(st.nextToken());
			if (gender == 1) {
				for (int j=0; j < n; j++) {
					if((j+1) % number == 0)
						arr[j] = arr[j] == 0? 1: 0;
				}
			} else if (gender == 2) {
				arr[number - 1] = arr[number - 1] == 0 ? 1 : 0;
				for(int j=1; j<n/2; j++) {
					if(number - 1 + j >= n || number - 1 - j < 0)
						break;
					if(arr[number - 1 - j] == arr[number - 1 + j]) {
						arr[number - 1 - j] = arr[number - 1 - j] == 0 ? 1 : 0;
						arr[number - 1 + j] = arr[number - 1 + j] == 0 ? 1 : 0;
					}
					else break;
				}		
		}
		}
		for(int i=0; i<n; i++) {
			System.out.print(arr[i] + " ");
			if((i+1) % 20 == 0)
				System.out.println();
		}
	}
}

