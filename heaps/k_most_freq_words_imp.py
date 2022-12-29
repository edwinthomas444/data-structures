'''Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.'''


import heapq

class custom(object):
    def __init__(self,word,freq):
        self.word = word
        self.freq = freq

    # to compare objects first by frequency then by the word length in lexicographical order
    # but as we have to remove elements from the min heap, which are least important
    # the order of importance is given by alphabetical then the -ve or frequency 
    # so leastleast freqency word will be removed first, and if same freq, reverse chronological order removed first
    # used by heapq when comparing objects
    def __lt__(self, other):
        if self.freq == other.freq:
            if self.word<=other.word:
                return False
            else:
                return True
        else:
            return self.freq <= other.freq

def display(heap):
    for obj in heap:
        print(obj.word, obj.freq)

class Solution(object):
    # nlogk solution using priority queues/ heaps with custom compare element functions
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word,0) + 1
        
        heap = []
        for word, freq in list(word_freq.items()):
            word_obj = custom(word, freq)
            heapq.heappush(heap, word_obj)
            
            # maintain atmost k elements in the heap at any point of time
            # so complexity would be nlogk instead of nlogn
            while len(heap)>k:
                heapq.heappop(heap)
        
        ans = []
        while heap:
            ans.append(heapq.heappop(heap).word)
        return ans[::-1]
        
    # nlogn solution
    def topKFrequent_soln2(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word,0) + 1
        
        sorted_freq = [x[0] for x in sorted(list(word_freq.items()),key=lambda x: (-x[1],x[0]))[:k]]
        
        
        return sorted_freq