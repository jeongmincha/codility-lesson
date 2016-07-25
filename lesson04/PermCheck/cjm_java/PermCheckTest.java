package com.codility.lesson04;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by JeongMinCha on 2016. 7. 21..
 */
public class PermCheckTest {

    PermCheck permCheck;

    @Before
    public void setUp() throws Exception {
        permCheck = new PermCheck();
    }

    @Test
    public void permFail() throws Exception {
        int[] arr = {4,1,3};
        int answer = 0;
        assertEquals(answer, permCheck.solution(arr));
    }

    @Test
    public void permSuccess() throws Exception {
        int[] arr = {4,1,3,2};
        int answer = 1;
        assertEquals(answer, permCheck.solution(arr));
    }
}