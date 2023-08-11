import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int[][] city = new int[N][N];
        List<int[]> home = new ArrayList<>();
        List<int[]> chicken = new ArrayList<>();

        for (int n = 0; n < N; n++) {
            for (int j = 0; j < N; j++) {
                city[n][j] = scanner.nextInt();
                if (city[n][j] == 1) {
                    home.add(new int[]{n, j});
                } else if (city[n][j] == 2) {
                    chicken.add(new int[]{n, j});
                }
            }
        }

        generateCombinations(chicken, new ArrayList<>(), M, 0, home);

        System.out.println(answer);
    }

    private static void generateCombinations(List<int[]> arr, List<int[]> current, int r, int index, List<int[]> home) {
        if (current.size() == r) {
            int total = 0;
            for (int[] h : home) {
                int dist = Integer.MAX_VALUE;
                for (int[] c : current) {
                    dist = Math.min(dist, Math.abs(h[0] - c[0]) + Math.abs(h[1] - c[1]));
                }
                total += dist;
            }
            answer = Math.min(answer, total);
            return;
        }

        if (index == arr.size()) {
            return;
        }

      
        current.add(arr.get(index));
        generateCombinations(arr, current, r, index + 1, home);
        current.remove(arr.get(index));

        
        generateCombinations(arr, current, r, index + 1, home);
    }
}