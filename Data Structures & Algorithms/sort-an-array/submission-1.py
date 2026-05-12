class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def msort(num_list: List[int]):
            if len(num_list) <= 1:
                return num_list
            
            m = len(num_list) // 2
            left = msort(num_list[0:m])
            right = msort(num_list[m:len(num_list)])

            l, r, i = 0, 0, 0
            merged = [0] * (len(left) + len(right))

            while l < len(left) and r < len(right):
                if left[l] >= right[r]:
                    merged[i] = right[r]
                    r += 1
                else:
                    merged[i] = left[l]
                    l += 1
                i += 1
            
            while l < len(left):
                merged[i] = left[l]
                l += 1
                i += 1
            
            while r < len(right):
                merged[i] = right[r]
                r += 1
                i += 1
            return merged

        return msort(nums)
