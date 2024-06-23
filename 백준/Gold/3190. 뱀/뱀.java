import java.util.*;
import java.io.*;

public class Main {
	static int[][] board;
	static int[] dx,dy;
	static int dir;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine()); // 보드 크기
		board = new int[N][N];
		int K = Integer.parseInt(br.readLine()); // 사과 개수
		StringTokenizer st;
		for (int i=0; i < K; i++) {
			st = new StringTokenizer(br.readLine());
			int r = Integer.parseInt(st.nextToken()) - 1;
			int c = Integer.parseInt(st.nextToken()) - 1;
			board[r][c] = 2; // 사과 위치
		}
		
		int L = Integer.parseInt(br.readLine()); // 방향 전환 개수
		Map<Integer,String> map = new HashMap<>();
		for (int i=0; i < L; i++) {
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			String s = st.nextToken().trim();
			map.put(n,s);
		}
		dx = new int[] {0,1,0,-1};
		dy = new int[] {1,0,-1,0};
		dir = 0;
		Deque<int[]> que = new LinkedList<>();
		int nx = 0;
		int ny = 0;
		int cnt = 0;
		board[nx][ny] = 1;
		que.add(new int[] {0,0});
		while(true) {
			cnt += 1;
			nx += dx[dir];
			ny += dy[dir];
			if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
				break;
			}
			if (board[nx][ny] == 2) {
				board[nx][ny] = 1;
				que.add(new int[] {nx,ny});
				if (map.containsKey(cnt)) {
					getDir(map.get(cnt));
				}
			} else if (board[nx][ny] == 0) {
				board[nx][ny] = 1;
				que.add(new int[] {nx,ny});
				int[] temp = que.pop();
				board[temp[0]][temp[1]] = 0;
				if (map.containsKey(cnt)) {
					getDir(map.get(cnt));
				}

			} else {
				break;
			}
		}
		System.out.println(cnt);
	}
	public static void getDir(String s) {
		if (s.equals("L")) {
			if (dir -1 < 0) {
				dir = 3;
			} else {
			dir = (dir-1) % 4;
			}
		} else {
			dir = (dir+1) % 4;
		}
	}
}