import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int L = Integer.parseInt(input[0]);
        int C = Integer.parseInt(input[1]);

        String[] arr = br.readLine().split(" ");
        Arrays.sort(arr); // Sort the input array

        List<String> combi = new ArrayList<>();
        generateCombinations(arr, L, 0, "", combi);

        List<String> answer = new ArrayList<>();
        for (String com : combi) {
            int vowelCount = 0;
            for (char c : com.toCharArray()) {
                if (isVowel(c)) {
                    vowelCount++;
                }
            }
            if (vowelCount >= 1 && L - vowelCount >= 2) {
                answer.add(com);
            }
        }

        for (String ans : answer) {
            System.out.println(ans);
        }
    }

    private static void generateCombinations(String[] arr, int length, int index, String current, List<String> result) {
        if (length == 0) {
            result.add(current);
            return;
        }
        if (index >= arr.length) {
            return;
        }
        generateCombinations(arr, length - 1, index + 1, current + arr[index], result);
        generateCombinations(arr, length, index + 1, current, result);
    }

    private static boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}