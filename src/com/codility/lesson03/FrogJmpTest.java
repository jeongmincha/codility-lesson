package com.codility.lesson03;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by JeongMinCha on 2016. 7. 20..
 */
public class FrogJmpTest {

    FrogJmp frogJmp;

    @Before
    public void setUp() throws Exception {
        frogJmp = new FrogJmp();
    }

    @Test
    public void solution() throws Exception {
        int answer = 3;
        assertEquals(answer, frogJmp.solution(10, 85, 30));
    }

}