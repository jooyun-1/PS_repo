import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int L = scanner.nextInt();

        int[] fruits = new int[N];
        for (int i = 0; i < N; i++) {
            fruits[i] = scanner.nextInt();
        }

        Arrays.sort(fruits);

        for (int f : fruits) {
            if (f <= L) {
                L++;
            }
        }

        System.out.println(L);
    }
}