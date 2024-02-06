// https://school.programmers.co.kr/learn/courses/30/lessons/178871
// 달리기 경주

import java.util.HashMap;
import java.util.Collection;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};
        HashMap<Integer, String> rankPlayer = new HashMap<Integer, String>();
        HashMap<String, Integer> playerRank = new HashMap<String, Integer>();
        for (int i = 0; i < players.length; i++) {
            rankPlayer.put(i, players[i]);
            playerRank.put(players[i], i);
        }
        
        
        for (String calling : callings) {
            int rank = playerRank.remove(calling);
            String player = rankPlayer.remove(rank);
            String frontPlayer = rankPlayer.get(rank - 1);
            rankPlayer.put(rank - 1, player);
            playerRank.put(player, rank - 1);
            rankPlayer.put(rank, frontPlayer);
            playerRank.put(frontPlayer, rank);
        }
        
        return rankPlayer.values().toArray(new String[0]);
    }
}
