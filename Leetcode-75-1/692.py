class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # return answer sorted by frequency from highest to lowest
        # words sorted lexicographically
        # k is the number of words to return
        # two conflicting words: sort with lexicographical order
        word_dict = {
            word: words.count(word) for word in words
        }
        word_list = list(word_dict.keys()) #sorted list of words without duplicates
        word_list.sort(key=lambda x: (-word_dict[x], x))
        return word_list[:k]
    
