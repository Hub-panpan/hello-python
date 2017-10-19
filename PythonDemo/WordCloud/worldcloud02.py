
#wordcloud生成中文词云

from wordcloud import WordCloud
import codecs
import jieba.finalseg
#import jieba.analyse as analyse
from scipy.misc import imread
import os
from os import path
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


# 绘制词云
def draw_wordcloud():
    #读入一个txt文件
    comment_text = open('test2.txt','r').read()
    #结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
    cut_text = " ".join(jieba.cut(comment_text))
    d = path.dirname(__file__) # 当前文件文件夹所在目录
    color_mask = imread("bj.jpg") # 读取背景图片
    cloud = WordCloud(
        #设置字体，不指定就会出现乱码
        font_path="mzd.ttf",
        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色
        background_color='white',
        #词云形状
        mask=color_mask,
        #允许最大词汇
        max_words=2000,
        #最大号字体
        max_font_size=40
    )
    word_cloud = cloud.generate(cut_text) # 产生词云
    word_cloud.to_file("pjl_cloud5.jpg") #保存图片
    #  显示词云图片
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()



if __name__ == '__main__':

    draw_wordcloud()