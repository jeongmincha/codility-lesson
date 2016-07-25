package com.codility.lesson02;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by JeongMinCha on 2016. 7. 10..
 */
public class CyclicRotationTest {

    CyclicRotation cyclicRotation;

    @Before
    public void setUp() throws Exception {
        cyclicRotation = new CyclicRotation();
    }

    @Test
    public void solution() throws Exception {
        // expected answer
        int[] A = {3, 8, 9, 7, 6};
        int K = 3;
        int[] expected = cyclicRotation.solution(A, K);

        // actual answer
        int[] actual = {9, 7, 6, 3, 8};
        assertArrayEquals(expected, actual);
    }
}