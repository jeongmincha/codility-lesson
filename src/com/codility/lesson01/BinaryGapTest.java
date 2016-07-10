package com.codility.lesson01;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by JeongMinCha on 2016. 7. 10..
 */
public class BinaryGapTest {

    BinaryGap binaryGap;

    @Before
    public void setUp() throws Exception {
        binaryGap = new BinaryGap();
    }

    @Test
    public void solution() throws Exception {
        // 1001
        assertEquals(binaryGap.solution(9), 2);
        // 1000010001
        assertEquals(binaryGap.solution(529), 4);
        // 10100
        assertEquals(binaryGap.solution(20), 1);
        // 1111
        assertEquals(binaryGap.solution(15), 0);
    }
}