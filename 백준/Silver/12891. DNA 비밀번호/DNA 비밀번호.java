import java.io.*;
import java.util.*;

/*
 * 1.
 * 모든 문자열의 문자가 A, C, G, T
 * 문자의 개수가 특정 개수 이상이어야 함
 * 
 * 
 */
public class Main {
	static int p,s;
	static char[] str;
	static int[] checkArr;
	static int[] arr;
	static int answer = 0;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		boolean flag = true;
		s = Integer.parseInt(st.nextToken());
		p = Integer.parseInt(st.nextToken());
		
		str = br.readLine().toCharArray();
		st = new StringTokenizer(br.readLine());
		checkArr = new int[4];
		arr = new int[4];
		for (int i = 0; i < 4; i++) {
			checkArr[i] = Integer.parseInt(st.nextToken());
		}
		for (int i = 0; i < p; i++) {
			if (str[i] == 'A') {
				arr[0] += 1;
			} else if (str[i] == 'C') {
				arr[1] += 1;
			} else if (str[i] ==  'G') {
				arr[2] += 1;
			} else if(str[i] == 'T') {
				arr[3] += 1;
			}
		}
		
		for (int i = 0; i < 4 ; i++) {
			if (arr[i] < checkArr[i]) {
				flag = false;
				break;
			}
			
		}
		if (flag == true) {
			answer += 1;
		}
		int index = 0;

		for (int j = p; j < s; j++) { // 부분문자열의 끝을 나타내는 위치
			index = j - p; // 이전 부분문자열의 시작을 나타내는 위치
			flag = true;
			// 이전 부분문자열의 시작 문자 제외
			if (str[index]=='A') arr[0]--;
			if (str[index]=='C') arr[1]--;
			if (str[index]=='G') arr[2]--;
			if (str[index]=='T') arr[3]--;
			
			// 이전 부분문자열의 끝에서 1문자 추가
			if (str[j]=='A') arr[0]++;
			if (str[j]=='C') arr[1]++;
			if (str[j]=='G') arr[2]++;
			if (str[j]=='T') arr[3]++;
			
			for (int i = 0; i < 4 ; i++) {
				if (arr[i] < checkArr[i]) {
					flag = false;
					break;
				}
			}
			if (flag == true) {
				answer += 1;
			}
		}

		System.out.println(answer);

	}
}