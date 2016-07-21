package com.codility.lesson04;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by JeongMinCha on 2016. 7. 21..
 */
public class PermCheck {
    public int solution(int[] A) {
        // K = value, V = count
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < A.length; i++) {
            if (!map.containsKey(A[i])) {
                map.put(A[i], 1);
            } else {
                return 0;   // The same element appears again!
            }
        }

        for (int idx = 1; idx <= A.length; idx++) {
            if (!map.containsKey(idx)) {
                return 0;   // 'idx' is missing
            }
        }

        return 1;
    }
}
