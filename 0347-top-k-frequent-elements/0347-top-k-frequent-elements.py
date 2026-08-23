class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
         
        freq = {}
        heap = []
        result = []

        for i in nums:
            freq[i] = freq.get(i,0)+1

        for key,value in freq.items():
            heapq.heappush(heap,(value,key))

            if len(heap)>k:
                heapq.heappop(heap)

        for key,value in heap:
            result.append(value)
            heapq.heapify(result)

        return result