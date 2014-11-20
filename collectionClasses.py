#!/usr/bin/env python
from mrjob.job import MRJob
import re
import simplejson as json
import math
class CountWords(MRJob):

    def mapper(self,key,line):
        jso = json.loads(line)
        uid = jso['user_id']
        text=jso['text']
        stars = int(jso['stars'])
        for word in re.findall(r'\w+',text.lower()):
            yield [word], stars
    def reducer(self, word, stars):
        res = []
        res.append(0)
        res.append(0)
        res.append(0)
        res.append(0)
        res.append(0)
        for star in stars:
            res[star-1] = res[star-1] + 1
        yield word, res
    def steps(self):
        return [self.mr(mapper = self.mapper, reducer = self.reducer)]
if __name__ == '__main__':
    CountWords.run()