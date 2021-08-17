import re
from TurkishStemmer import TurkishStemmer
turkStem = TurkishStemmer()

url = "https://www.intaslar.com/kategori/tuy"
words_list = re.compile(r'[\:/?=\-&.,_@%!$0123456789()&*+\[\]]+', re.UNICODE).split(url)
drop_words = set(['', 'http', 'https', 'www', 'com', '\t', 'm', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'n',
                      'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
[turkStem.stem(word.lower()) for word in words_list if word.lower() not in drop_words]