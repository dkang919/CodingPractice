#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 10:15:54 2023

@author: dongwookang
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        k = set(nums1)

        ans = set()
        for j in nums2:
            if j in k:
                ans.add(j)

        return ans
    
    
    
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        return set(nums1).intersection(set(nums2))