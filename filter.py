import sys
import wordCount
from operator import itemgetter

class Filter(object):

    @classmethod 
    def get_all_words(self, input_file):
        job = wordCount.CountWords()
        total_words = []
        with open(input_file) as sourcefile:
            for line in sourcefile:
                word, count = job.parse_output_line(line)
                total_words.append((str(word), count))
        return total_words
        
    @classmethod 
    def get_negative_words(self, input_file):
        negative_words = []
        with open(input_file) as sourcefile:
            for line in sourcefile:
                word = str(line).strip()
                negative_words.append(word)
        return negative_words
        
    @classmethod 
    def get_positive_words(self, input_file):
        positive_words = []
        with open(input_file) as sourcefile:
            for line in sourcefile:
                word = str(line).strip()
                positive_words.append(word)
        return positive_words
        
    def update_total_words(self):
        updated_list = []
        for pair in self.total_words:           
            if (pair[0] in self.positive_words or pair[0] in self.negative_words):
                updated_list.append(pair)
        self.total_words = updated_list
        
    def __init__(self):
        self.total_words = self.get_all_words('review_word_count.txt')
        self.negative_words = self.get_negative_words('negative_words.txt')
        self.positive_words = self.get_positive_words('positive_words.txt')
        
        
if __name__ == '__main__':
    filter = Filter()
    print "Total words from reviews: " + str(len(filter.total_words))
    print "Positive words: " + str(len(filter.positive_words))
    print "Negative words: " + str(len(filter.negative_words))
    filter.update_total_words()
    print "After filter: " + str(len(filter.total_words))