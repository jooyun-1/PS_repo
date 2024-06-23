import java.util.*;
import java.io.*;

public class Main {
	static int[][] board;
	static int[] dice;
	static int[] commands;
	public static void main(String[] args) throws IOException {
		 BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st;
		 st = new StringTokenizer(br.readLine());
		 int N = Integer.parseInt(st.nextToken());
		 int M = Integer.parseInt(st.nextToken());
		 int x = Integer.parseInt(st.nextToken());
		 int y = Integer.parseInt(st.nextToken());
		 int K = Integer.parseInt(st.nextToken());
		 board = new int[N][M];
		 dice = new int[6];
		 int[] dx = new int[] {0,0,-1,1};
		 int[] dy = new int[] {1,-1,0,0};
		 
		 for (int n = 0; n < N; n++) {
			 int col = 0;
			 st = new StringTokenizer(br.readLine());
			 for (int m = 0; m < M; m++) {
				 board[n][m] = Integer.parseInt(st.nextToken());
			 }
		 }
		 
		 commands = new int[K];
		 int nx = x;
		 int ny = y;
		 
		 st = new StringTokenizer(br.readLine());
		 for (int i=0;i<K;i++) {
			 commands[i] = Integer.parseInt(st.nextToken());
		 }
		 for (int i=0; i<commands.length;i++) {
			 nx += dx[commands[i]-1];
			 ny += dy[commands[i]-1];
			 if (nx < 0 || nx >= N || ny < 0 || ny >= M) {
				 nx -= dx[commands[i]-1];
				 ny -= dy[commands[i]-1];
				 continue;
			 }
			 move(commands[i]);
			 if (board[nx][ny] == 0) {
				 board[nx][ny] = dice[5];
			 } else {
				 dice[5] = board[nx][ny];
				 board[nx][ny] = 0;
			 }
//			 System.out.println(dice[1] +" " + dice[2] +" " + dice[3] +" " + dice[4] +" "+ dice[5]);
			 System.out.println(dice[0]);
		 }
		 
		 
	}
	
	public static void move(int n) {
		int a = dice[0];
		int b = dice[1];
		int c = dice[2];
		int d = dice[3];
		int e = dice[4];
		int f = dice[5];
		if (n == 1) {
			dice[0] = d;
			dice[1] = b;
			dice[2] = a;
			dice[3] = f;
			dice[4] = e;
			dice[5] = c;
		} else if (n == 2) {
			dice[0] = c;
			dice[1] = b;
			dice[2] = f;
			dice[3] = a;
			dice[4] = e;
			dice[5] = d;
		} else if (n == 3) {
			dice[0] = e;
			dice[1] = a;
			dice[2] = c;
			dice[3] = d;
			dice[4] = f;
			dice[5] = b;
		} else if (n == 4) {
			dice[0] = b;
			dice[1] = f;
			dice[2] = c;
			dice[3] = d;
			dice[4] = a;
			dice[5] = e;
		}
	}
}