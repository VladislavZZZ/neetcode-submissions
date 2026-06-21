class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        min_arr, max_arr = [nums1, nums2] if len(nums1) < len(nums2) else [nums2, nums1]
        is_odd=(len(nums1)+len(nums2))%2 == 1
        median_ind = (len(nums1)+len(nums2))//2
        l, r = 0, len(min_arr)-1
        while True:
            m_min=(l+r)//2
            m_max = median_ind -m_min -2
            minl, minr =min_arr[m_min] if m_min>=0 else float("-infinity"), min_arr[m_min+1] if m_min+1 < len(min_arr) else float("infinity")
            maxl, maxr = max_arr[m_max] if m_max>=0 else float("-infinity"), max_arr[m_max+1] if m_max+1 < len(max_arr) else float("infinity")
            if (minl > maxr):
                r=m_min-1
            elif (maxl > minr):
                l=m_min+1
            else:
                if is_odd:
                   return min(maxr,minr) 
                return (min(maxr, minr)+max(maxl, minl))/2