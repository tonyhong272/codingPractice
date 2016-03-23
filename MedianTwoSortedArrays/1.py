class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            numL, numS, lenL, lenS = nums1, nums2, len(nums1), len(nums2)
        else:
            numL, numS, lenL, lenS = nums2, nums1, len(nums2), len(nums1)
        half_lens = (lenL + lenS + 1)/2
        pointerL = (lenL + 1) / 2 - 1

        if lenS == 0:
            if lenL % 2 == 1:
                return numL[pointerL]
            else:
                return numL[pointerL]*0.5 + numL[pointerL + 1]*0.5
            
        if lenS == 1:
            new_list = sorted(nums1+nums2)
            if len(new_list) %2 == 1:
                return new_list[len(new_list)/2]
            else:
                return 0.5 * new_list[len(new_list)/2 - 1] + 0.5 * new_list[len(new_list)/2]

        while True:
            pointerS = half_lens - pointerL - 2
            if pointerS < lenS -1 and numL[pointerL] > numS[pointerS+1] and pointerL >= 0:
                pointerL = pointerL - 1
            elif pointerL < lenL -1 and numS[pointerS] > numL[pointerL + 1] and pointerS >= 0:
                pointerL = pointerL + 1
            else:
#                print('final',pointerL, pointerS, numL)
                if (lenS + lenL) % 2 == 1:
                        if pointerS< 0:
                            return numL[pointerL]
                        elif pointerL< 0:
                            return numL[pointerS]
                        else:
                            return max(numL[pointerL], numS[pointerS])
                else:
                    if pointerS <0 and pointerL < lenL - 1:
                        return 0.5* ( numL[pointerL] + min(numS[0], numL[pointerL + 1]))
                    elif pointerS < 0 and pointerL == lenL - 1:
                        return 0.5* (numL[pointerL] + numS[0])
                    elif pointerL <0 and pointerS == lenS - 1:
                        return 0.5* (numS[pointerS] + numL[0])
                    elif pointerS >= lenS - 1:
                        return 0.5*max(numL[pointerL], numS[pointerS]) + 0.5*numL[pointerL+1]
                    else:
                        return 0.5*max(numL[pointerL], numS[pointerS]) + 0.5*min(numL[pointerL+1], numS[pointerS+1]) 
