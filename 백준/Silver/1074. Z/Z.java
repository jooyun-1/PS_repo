import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int cnt = 0;
        int size = (int) Math.pow(2, N);
        int quarterSize = size / 2;

        while (N != 0) {
            N--;

            if (r < quarterSize && c < quarterSize) {
                // 1사분면
            } else if (r < quarterSize && c >= quarterSize) {
                // 2사분면
                cnt += quarterSize * quarterSize;
                c -= quarterSize;
            } else if (r >= quarterSize && c < quarterSize) {
                // 3사분면
                cnt += 2 * quarterSize * quarterSize;
                r -= quarterSize;
            } else {
                // 4사분면
                cnt += 3 * quarterSize * quarterSize;
                r -= quarterSize;
                c -= quarterSize;
            }

            quarterSize /= 2;
        }

        System.out.println(cnt);
    }
}