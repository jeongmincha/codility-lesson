package com.codility.lesson04;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by JeongMinCha on 2016. 7. 21..
 */
public class FrogRiverOneTest {

    FrogRiverOne frogRiverOne;

    @Before
    public void setUp() throws Exception {
        frogRiverOne = new FrogRiverOne();
    }

    @Test
    public void solution() throws Exception {
        int[] arr = {1,3,1,4,2,3,5,4};
        int answer = 6;
        assertEquals(answer, frogRiverOne.solution(5, arr));
    }

    @Test
    public void neverAcross() throws Exception {
        int[] arr = {5, 4, 3, 2, 5, 4};
        int answer = -1;
        assertEquals(answer, frogRiverOne.solution(5, arr));
    }

    @Test
    public void neverAcrossSingleElement() throws Exception {
        int[] arr = {5};
        int answer = -1;
        assertEquals(answer, frogRiverOne.solution(5, arr));
    }
}