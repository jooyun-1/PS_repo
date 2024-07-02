import java.util.*;

class Solution {
    static int[] chosen;
    static List<int[]> list;
    static HashMap<Integer,Integer> map;
    
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        int sum = 0;
        map = new HashMap<>();
        for (int i : tangerine) {
            map.put(i, map.getOrDefault(i,0) + 1);
        }
        List<Integer> keyList = new ArrayList<>(map.keySet());
        keyList.sort((k1,k2) -> map.get(k2) - map.get(k1));
        
        for (Integer n : keyList) {
            if (k <= 0) {
                break;
            }

            answer++;
            k -= map.get(n);
        }
        return answer;
    }
    
    
}