package com.codility.lesson04;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by JeongMinCha on 2016. 7. 21..
 */
public class FrogRiverOne {
    public int solution(int X, int[] A) {
        boolean accrossFlag = false;

        int idx;
        int leaf_num = 0;

        // K = value, V = index
        Map<Integer, Integer> map = new HashMap<>();

        for (idx = 0; idx < A.length; idx++) {
            if (!map.containsKey(A[idx])) {
                map.put(A[idx], ++leaf_num);
            }
            if (leaf_num == X) {
                accrossFlag = true;
                break;
            }
        }

        if (accrossFlag) {
            return idx;
        } else {
            return -1;
        }
    }
}
