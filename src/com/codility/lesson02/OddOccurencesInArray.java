package com.codility.lesson02;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by JeongMinCha on 2016. 7. 16..
 */
public class OddOccurencesInArray {
    public int solution(int[] A) {
        Map<Integer,Integer> counts = new HashMap<>();
        for (int elem: A) {
            if (counts.containsKey(elem)) {
                counts.put(elem, counts.get(elem)+1);
            } else {
                counts.put(elem, 1);
            }
        }
        for (int key: counts.keySet()) {
            if (counts.get(key) % 2 != 0) {
                return key;
            }
        }
        return 0;
    }
}
