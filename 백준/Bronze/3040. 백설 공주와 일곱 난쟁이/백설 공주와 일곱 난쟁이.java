import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[9];

        for (int i = 0; i < 9; i++) {
            arr[i] = scanner.nextInt();
        }

        for (int i = 0; i < 8; i++) {
            for (int j = i + 1; j < 9; j++) {
                int sum = 0;
                for (int k = 0; k < 9; k++) {
                    if (k != i && k != j) {
                        sum += arr[k];
                    }
                }
                if (sum == 100) {
                    for (int k = 0; k < 9; k++) {
                        if (k != i && k != j) {
                            System.out.println(arr[k]);
                        }
                    }
                    return;
                }
            }
        }
    }
}