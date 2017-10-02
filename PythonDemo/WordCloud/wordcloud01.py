# -*- coding: utf-8 -*-

#!/usr/bin/env python
"""
Image-colored wordcloud
=======================

You can color a word-cloud by using an image-based coloring strategy
implemented in ImageColorGenerator. It uses the average color of the region
occupied by the word in a source image. You can combine this with masking -
pure-white will be interpreted as 'don't occupy' by the WordCloud object when
passed as mask.
If you want white as a legal color, you can just pass a different image to
"mask", but make sure the image shapes line up.
你可以使用基于图像的颜色策略来为文字云上色
在ImageColorGenerator中实现。它使用了该区域的平均颜色
在源图像中被这个词占据。你可以把它和掩蔽-
纯白色将被文字云对象解释为“不占用”
通过面具。
如果你想要白色作为合法颜色，你可以通过不同的图像
“蒙版”，但要确保图像的形状是一致的。
http://www.cnblogs.com/MnCu8261/p/5483657.html 关于os
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00140767171357714f87a053a824ffd811d98a83b58ec13000
实际上他是用来操作图片的 例如切片、旋转、滤镜、输出文字、调色板等一应俱全
"""

from os import path
# os.path.dirname(path)    #返回该路径的父目录
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'test.txt')).read()
#os.path.join(path,name)
#连接目录与文件名或目录 结果为path/name
# read the mask / color image taken from
# http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
alice_coloring = np.array(Image.open(path.join(d, "bj.jpg")))

# 设置停用词
stopwords = set(STOPWORDS)
stopwords.add("navigation")

# 你可以通过 mask 参数 来设置词云形状
wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
# generate word cloud'generate 可以对全部文本进行自动分词,但是他对中文支持不好
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(alice_coloring)

# show
# 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()
wc.to_file('sy1.png')
#将生成的实验图保存
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
# 我们还可以直接在构造函数中直接给颜色
# 通过这种方式词云将会按照给定的图片颜色布局生成字体颜色策略
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
wc.to_file('sy2.png')

plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()