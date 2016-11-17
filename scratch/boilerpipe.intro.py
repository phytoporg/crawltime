from boilerpipe.extract import Extractor
#URL='http://www.breitbart.com/'
URL='http://www.breitbart.com/california/2016/11/16/stop-bannon-trump-feeling-the-hate-los-angeles-protest/'

extractor = Extractor(extractor='ArticleExtractor', url=URL)

text = extractor.getText()
print text.encode('utf-8','replace')
