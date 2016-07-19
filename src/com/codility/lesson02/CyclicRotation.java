package com.codility.lesson02;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by JeongMinCha on 2016. 7. 10..
 */
public class CyclicRotation {
    public int[] solution(int[] A, int K) {
        int k = K;
        if (k == 0 || A.length <= 1) {
            return A;
        }

        while (k > A.length) {
            k -= A.length;
        }
        if (k == A.length) {
            return A;
        }

        int[] solution = new int[A.length];
        List<Integer> newList = new ArrayList<Integer>();

        for (int elem : A) {
            newList.add(elem);
        }
        for (int idx = 1; idx <= k; idx++) {
            newList.add(0, A[A.length - idx]);
        }

        for (int idx = 0; idx < A.length; idx++) {
            solution[idx] = newList.get(idx);
        }
        return solution;
    }
}
