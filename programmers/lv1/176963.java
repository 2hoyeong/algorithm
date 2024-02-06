// https://school.programmers.co.kr/learn/courses/30/lessons/176963
// 추억 점수

import java.util.HashMap;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photos) {
        int[] answer = new int[photos.length];
        HashMap<String, Integer> nameYearning = new HashMap<String, Integer>();
        for (int i = 0; i < name.length; i++) {
            nameYearning.put(name[i], yearning[i]);
        }
        
        for (int i = 0; i < photos.length; i++) {
            String[] photo = photos[i];
            for (String people : photo) {
                if (nameYearning.containsKey(people)) {
                    answer[i] += nameYearning.get(people);
                }
            }
        }
        return answer;
    }
}
