#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 

@author: dongwookang
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        common = set(nums1).intersection(set(nums2))

        ans = []

        for item in nums1:
            if item in common:
                if item in nums2:
                    ans.append(item)
                    nums2.remove(item)

        return ans


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d1 = {}
        d2 = {}

        for i in nums1:
            d1[i] = d1.get(i, 0) + 1

        for i in nums2:
            d2[i] = d2.get(i, 0) + 1
    
        intersection = []

        for i in d1.keys():
            if i in d2.keys():
                intersection += [i] * min(d1[i], d2[i])
        
        return intersection