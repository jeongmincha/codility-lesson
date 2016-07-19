package com.codility.lesson03;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by JeongMinCha on 2016. 7. 20..
 */
public class TapeEquilibriumTest {

    TapeEquilibrium tapeEquilibrium;

    @Before
    public void setUp() throws Exception {
        tapeEquilibrium = new TapeEquilibrium();
    }

    @Test
    public void solution() throws Exception {
        int[] arr = {3, 1, 2, 4, 3};
        int answer = 3;
        assertEquals(answer, tapeEquilibrium.solution(arr));
    }

}