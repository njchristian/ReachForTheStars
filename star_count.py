#!/user/bin/env python
from mrjob.job import MRJob
from operator import itemgetter
import re
import simplejson as json

class Processor(MRJob):
    def mapper_1(self, key, line):
        line = json.loads(line)
        stars = line['stars']
        yield stars, 1

    def reducer_1(self, key_pair, counts):
        yield key_pair, sum(counts)


    def steps(self):
        return [ self.mr(mapper = self.mapper_1, reducer = self.reducer_1) ]

if __name__ == '__main__':
    Processor.run()

