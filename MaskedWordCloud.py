from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from matplotlib.pyplot import figure
figure(num=None, figsize=(14, 10), dpi=80, facecolor='w', edgecolor='k')
text = ""
with open("C:/Users/avakk/Downloads/hello.txt", encoding='utf-8') as f: #Path to Text File
    text = ''.join(f.readlines())

custom_mask = np.array(Image.open("C:/Users/avakk/Downloads/testt.jpg")) #Path to Vector Image
wc = WordCloud(min_font_size=2, max_font_size=30, background_color="white", mask=custom_mask)
wc.generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()