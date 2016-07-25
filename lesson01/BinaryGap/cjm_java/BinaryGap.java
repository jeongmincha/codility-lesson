package com.codility.lesson01;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by JeongMinCha on 2016. 7. 10..
 */
public class BinaryGap {
    public int solution(int N) {
        int num = N;
        List<Boolean> binaryArray = new ArrayList<>();

        while (num != 0) {
            binaryArray.add(0, (num % 2) != 0);
            num /= 2;
        }

        int gap = 0, maxGap = 0;
        for (Boolean bit : binaryArray) {
            if (bit.equals(true)) {
                if (maxGap < gap) {
                    maxGap = gap;
                }
                gap = 0;
            } else {
                gap ++;
            }
        }
        return maxGap;
    }
}
