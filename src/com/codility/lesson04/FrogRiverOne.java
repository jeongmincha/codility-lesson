package com.codility.lesson04;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by JeongMinCha on 2016. 7. 21..
 */
public class FrogRiverOne {
    public int solution(int X, int[] A) {
        int idx;
        int count = 0;

        // K = value, V = index
        Map<Integer, Integer> map = new HashMap<>();

        for (idx = 0; idx < A.length; idx++) {
            if (!map.containsKey(A[idx])) {
                map.put(A[idx], ++count);
            }
            if (count == X) {
                break;
            }
        }

        return idx;
    }
}
