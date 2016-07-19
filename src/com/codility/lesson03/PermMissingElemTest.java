package com.codility.lesson03;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by JeongMinCha on 2016. 7. 20..
 */
public class PermMissingElemTest {

    PermMissingElem permMissingElem;

    @Before
    public void setUp() throws Exception {
        permMissingElem = new PermMissingElem();
    }

    @Test
    public void solution() throws Exception {
        int[] A = {2, 3, 1, 5};
        int answer = 4;
        assertEquals(answer, permMissingElem.solution(A));
    }

}