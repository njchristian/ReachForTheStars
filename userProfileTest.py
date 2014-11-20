#!/usr/bin/env python
from mrjob.job import MRJob
import re
import simplejson as json
import math
class CountWords(MRJob):

    def mapper(self,key,line):
        profiles = ["Xly4Bgx-ABt2MDEUXgEcXg", "MQ_HhZWWoPyPP1J5qWlypg", "0Zv9HyEs4IMyMW2AspJDYg", "2ecLeSa--N70YeKtQGWsug",
                "wDmXREigSPJX5iHa0PQygg", "_D1zyYMjll4almoGZjBmkA", "9LIZHEHMw2fmwOL25aVw6w", "CKSxuoWOqiZmXR6EAAKgEA", 
                "zdPRXhhJNCiCOgWQwoPlpg", "h3g-GaEFQFzczJiXzIOdaw", "3G34yhhtqed2ASeGfiqS1A", "Ft3BBqjm_ZRcQQ9UAtoJ_g", 
                "YLDNoMCv5lyWKJFqvHfEbA", "69_O4PnPowyjNYlT9BgWZA", "w9FobM_vIS2TH0xU7NPPJA", "uLyqe-WdvTR3eaM3mgoqpw", 
                "airuooZt5UTkFBsVAnMlkQ", "xTWoTGTmm6DUB7bKfOrW9g", "-PS9rTYQPl4R1OceVXfoWQ", "sM3gqadLq4KtCd7BR35nQQ", 
                "nnnV7CGk72vpGLNvaBvvrA", "YVyzM5JuquEGmSxWrlXzeg", "iAUOGnPA0tZJ0SZdbT7q_g", "ONu4VpPJ0P_ZmAP7oOaybA", 
                "mD1uXKXoCgxfpf9wz_1utA", "o7W3M6obikoL9pG81L1J6A", "LYcklDWjV4J5laAQMzakcg" ]
        jso = json.loads(line)
        uid = jso['user_id']
        if uid not in profiles:
            return
        text=jso['text']
        stars = int(jso['stars'])
        for word in re.findall(r'\w+',text.lower()):
            yield [word, uid], stars
    def reducer(self, wordAndId, stars):
        res = []
        res.append(0)
        res.append(0)
        res.append(0)
        res.append(0)
        res.append(0)
        for star in stars:
            res[star-1] = res[star-1] + 1
        yield wordAndId, res
    def steps(self):
        return [self.mr(mapper = self.mapper, reducer = self.reducer)]
if __name__ == '__main__':
    CountWords.run()