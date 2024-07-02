    // answer = 0
    // length = len(elements)
    // sums = set()
    // elements = elements * 2
    // for i in range(length) :
    //     for j in range(length) :
    //         sums.add(sum(elements[j:j+i+1]))
    // answer = len(sums)
    // return answer
import java.util.*;

class Solution {
    public int solution(int[] elements) {
        int answer = 0;
        int length = elements.length;
        HashSet<Integer> sums = new HashSet<>();
        int[] extendedElements = new int[length * 2];

        for (int i = 0; i < length; i++) {
            extendedElements[i] = elements[i];
            extendedElements[i + length] = elements[i];
        }
        
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                int sum = 0;
                for (int k = j; k < j + i + 1; k++) {
                    sum += extendedElements[k];
                }
                sums.add(sum);
            }
        }
        answer = sums.size();
        return answer;
    }
}