import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        HashMap<String,Integer> map = new HashMap<>();
        for (int i=0; i < want.length; i++) {
            map.put(want[i], number[i]);
        }
        
        for (int i=0; i < discount.length-9; i++) {
            HashMap<String,Integer> map2 = new HashMap<>();
            boolean flag = true;
            for (int j=0; j < 10; j++) {
                map2.put(discount[i+j], map2.getOrDefault(discount[i+j],0) + 1);            
            }
            // System.out.println(map.get(discount[i]));
            for (String k : map2.keySet()) {
                if (map2.get(k) != map.get(k)) {
                    flag = false;
                    break;
                }
            }
            
            if (flag) {
                answer++;
            }
        }
        return answer;
    }
}
