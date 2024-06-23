import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());

        int res = N % 5;
        int answer = 0;

        while (N >= 0) {
            if (N % 5 == 0) {
                answer += N / 5;
                System.out.println(answer);
                break;
            }
            N -= 3;
            answer += 1;
        }

        if (N < 0) {
            answer = -1;
            System.out.println(answer);
        }
    }
}