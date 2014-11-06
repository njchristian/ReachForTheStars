#!/usr/bin/env python
from mrjob.job import MRJob
import re
import simplejson as json
import math
class CountWords(MRJob):

    def mapper(self,key,line):
        jso = json.loads(line)
        if jso['user_id'] != '7FkIBEPZ_I5xWLU_dahnnQ':
            return
        text=jso['text']
        for word in re.findall(r'\w+',text.lower()):
            yield word, 1
    def reducer(self, word, counts):
        yield word, sum(counts)
    def steps(self):
        return [self.mr(mapper = self.mapper, reducer = self.reducer)]
if __name__ == '__main__':
    CountWords.run()