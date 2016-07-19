package com.codility.lesson03;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Created by JeongMinCha on 2016. 7. 20..
 */
public class TapeEquilibrium {
    public int solution(int[] A) {
        List<Integer> diff = new ArrayList<>();
        int sum = sigma(0, A.length, A);

        for (int i = 0; i < A.length-1; i++) {
            int aSum = sigma(0, i+1, A);
            int bSum = sum - aSum;
            diff.add(Math.abs(aSum - bSum));
        }

        return Collections.min(diff);
    }

    private int sigma(int start, int end, int[] A) {
        int sum = 0;
        for (int idx = start; idx < end; idx++) {
            sum += A[idx];
        }
        return sum;
    }
}
