package com.codility.lesson02;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by JeongMinCha on 2016. 7. 10..
 */
public class CyclicRotation {
    public int[] solution(int[] A, int K) {
        int[] solution = new int[A.length];
        List<Integer> newList = new ArrayList<Integer>();

        for (int elem : A) {
            newList.add(elem);
        }
        for (int idx = 1; idx <= K; idx++) {
            newList.add(0, A[A.length - idx]);
        }

        for (int idx = 0; idx < A.length; idx++) {
            solution[idx] = newList.get(idx);
        }
        return solution;
    }
}
