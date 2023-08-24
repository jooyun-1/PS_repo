import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] sushi = new int[N];
        for (int i = 0; i < N; i++) {
            sushi[i] = Integer.parseInt(br.readLine());
        }

        int[] eat = new int[d + 1];  // Index 1-based for sushi types
        int count = 0;  // Number of distinct sushi types in the window
        int maxCnt = 0;

        // Initial window setup
        for (int i = 0; i < k; i++) {
            if (eat[sushi[i]] == 0) {
                count++;
            }
            eat[sushi[i]]++;
        }

        for (int right = k; right < N + k; right++) {
            int left = right - k;

            // Calculate the count of distinct sushi types
            maxCnt = Math.max(maxCnt, count + (eat[c] == 0 ? 1 : 0));

            // Remove the sushi at the left end of the window
            eat[sushi[left]]--;
            if (eat[sushi[left]] == 0) {
                count--;
            }

            // Add the sushi at the right end of the window
            int newSushi = sushi[right % N];
            if (eat[newSushi] == 0) {
                count++;
            }
            eat[newSushi]++;
        }

        System.out.println(maxCnt);
    }
}
