from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image 

quran_words = open('quran.txt', 'r').read()
stopwords = set(STOPWORDS)
quran_wc = WordCloud(background_color = 'white', stopwords = stopwords)

stopwords.add('ye')
stopwords.add('lo') 
stopwords.add('hath')
stopwords.add('unto')
stopwords.add('verily')
stopwords.add('will')
stopwords.add('say')
stopwords.add('said')
stopwords.add('thee')
stopwords.add('thou')
stopwords.add('thy')
stopwords.add('thereof')
stopwords.add('let')
stopwords.add('among')
stopwords.add('therein')
stopwords.add('two')
stopwords.add('surely')
stopwords.add('nay')
stopwords.add('sura')
stopwords.add('us')
stopwords.add('know')
stopwords.add('go')
stopwords.add('may')
stopwords.add('upon')
stopwords.add('AL')
stopwords.add('thus')
stopwords.add('art')
stopwords.add('whose')
stopwords.add('whosoever')
stopwords.add('hast')
stopwords.add('till')
stopwords.add('naught')
stopwords.add('whereof')
stopwords.add('therefor')
stopwords.add('maketh')
stopwords.add('yet')
stopwords.add('whoso')
stopwords.add('even')
stopwords.add('though')

# re-generate the word cloud
quran_wc.generate(quran_words)

# display the cloud
fig = plt.figure()
fig.set_figwidth(14) # set width
fig.set_figheight(18) # set height

plt.imshow(quran_wc, interpolation='bilinear')
plt.axis('off')
plt.show()

mosque = np.array(Image.open('mosque2.jpg'))

quran_wc = WordCloud(background_color='white', mask=mosque, stopwords=stopwords)

# generate the word cloud
quran_wc.generate(quran_words)

# display the word cloud
fig = plt.figure()
fig.set_figwidth(14) # set width
fig.set_figheight(18) # set height

plt.imshow(quran_wc, interpolation='bilinear')
plt.axis('off')
plt.show()
