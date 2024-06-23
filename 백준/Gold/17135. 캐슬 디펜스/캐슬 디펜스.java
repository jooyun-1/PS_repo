import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int N, M, D;
    static int[][] board;
    static ArrayList<int[]> archerCombinations;
    static int[] dx = {0, -1, 0};
    static int[] dy = {-1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

        board = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        archerCombinations = new ArrayList<>();
        getArcherCombinations(0, 0, new int[3]);
        
        int answer = 0;
        for (int[] arrow : archerCombinations) {
            answer = Math.max(answer, attack(arrow));
        }

        System.out.println(answer);
    }

    static void getArcherCombinations(int index, int start, int[] selected) {
        if (index == 3) {
            archerCombinations.add(selected.clone());
            return;
        }

        for (int i = start; i < M; i++) {
            selected[index] = i;
            getArcherCombinations(index + 1, i + 1, selected);
        }
    }

    static int attack(int[] arrow) {
        int[][] temp = new int[N][M];
        int[][] attacked = new int[N][M]; // 공격당한 배열
        int result = 0;

        for (int i = 0; i < N; i++) {
            System.arraycopy(board[i], 0, temp[i], 0, M);
        }

        for (int i = N - 1; i >= 0; i--) {
            ArrayList<int[]> arr = new ArrayList<>(); // 모든 궁수가 다 화살을 쏘고 동시에 죽이기 위한 배열
            for (int a : arrow) {
                boolean[][] visited = new boolean[N][M];
                ArrayList<int[]> deq = new ArrayList<>();
                deq.add(new int[]{i, a, 1}); // 행, 열, distance

                while (!deq.isEmpty()) {
                    int[] current = deq.remove(0);
                    int x = current[0];
                    int y = current[1];
                    int d = current[2];

                    if (temp[x][y] == 1) { // 해당 값이 1
                        arr.add(new int[]{x, y});
                        if (attacked[x][y] == 0) { // 처음 공격 받았으면
                            attacked[x][y] = 1; // 1로 설정
                            result += 1;
                        }
                        break;
                    }
                    if (d < D) { // 사정거리 안
                        for (int k = 0; k < 3; k++) { // 좌, 상, 우 순으로 bfs 탐색(제일 왼쪽부터 죽임)
                            int nx = x + dx[k];
                            int ny = y + dy[k];
                            if (0 <= nx && nx < N && 0 <= ny && ny < M && !visited[nx][ny]) {
                                visited[nx][ny] = true;
                                deq.add(new int[]{nx, ny, d + 1});
                            }
                        }
                    }
                }
            }
            for (int[] coords : arr) {
                temp[coords[0]][coords[1]] = 0; // 동시에 죽임
            }
        }
        return result;
    }
}