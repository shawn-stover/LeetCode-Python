class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set the last index to the two arrays - 1
        last = m + n -1
        
        # Merge in Reverse Order
        while m > 0 and n > 0:
            # Check if m is shorter than n
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                # Move index to merge in reverse order
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                # Move index to merge in reverse order
                n -= 1
        # Fill nums1 with leftover nums2 Elements
        while n > 0:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1