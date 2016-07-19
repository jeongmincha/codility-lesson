package com.codility.lesson03;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by JeongMinCha on 2016. 7. 20..
 */
public class PermMissingElem {
    public int solution(int[] A) {
        int[] mask = new int[A.length + 2];
        for (int i = 1; i <= A.length + 1; i++) {
            mask[i] = i;
        }
        for (int i = 0; i < A.length; i++) {
            mask[A[i]] = 0;
        }
        for (int i = 1; i <= A.length + 1; i++) {
            if (mask[i] != 0) {
                return i;
            }
        }
        return 0;
    }
}
