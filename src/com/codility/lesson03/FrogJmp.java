package com.codility.lesson03;

/**
 * Created by JeongMinCha on 2016. 7. 20..
 */
public class FrogJmp {
    public int solution(int X, int Y, int D) {
        int jmp = 0;
        int distance = X;
        while (distance < Y) {
            distance += D;
            jmp++;
        }
        return jmp;
    }
}
