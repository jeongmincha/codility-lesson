package com.codility.lesson02;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by JeongMinCha on 2016. 7. 16..
 */
public class OddOccurencesInArrayTest {

    OddOccurencesInArray array;

    @Before
    public void setUp() throws Exception {
        array = new OddOccurencesInArray();
    }

    @Test
    public void solution() throws Exception {
        int[] A = {9, 3, 9, 3, 9, 7, 9};
        assertEquals(7, array.solution(A));
    }

}