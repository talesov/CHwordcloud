import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt  #绘制图像的模块
import jieba.analyse as anls  # 关键词提取
from imageio import imread
import re
import os
from collections import Counter
 
'''功能描述：
   1、读取文本
   2、分词
   3、加载停用词表
   4、去停用词
   5、提取关键词2种方法
   6、画词云展示
'''
print(os.getcwd()) #获取当前工作目录路径
##########################################
#词云遮罩
maskpic = imread("D:/workspace/python/词云/pic/sg.bmp")#词云的模板图片，与代码在同一文件夹中，格式随便
#文本路径
textpath="D:/workspace/python/词云/quick.txt"
#停词表路径
stoppath='D:/workspace/python/词云/chineseStopWords.txt'
#字体路径
fontpath="C:/Windows/Fonts/simfang.ttf"
#文件名字
resname="test.jpg"
#保存路径
respath="D:/workspace/python/词云/out/"+resname
##########################################

#1、读取文本
text = open(textpath, 'r', encoding='utf-8').read()
#加载停用词表
stopwords = [line.strip() for line in open(stoppath).readlines()]  # list类型
#分词未去停用词
text_split = jieba.cut(text)  # 未去掉停用词的分词结果   list类型
 
#去掉停用词的分词结果  list类型
text_split_no = []
for word in text_split:
    if word not in stopwords:
        text_split_no.append(word)
#print(text_split_no)
 
text_split_no_str =' '.join(text_split_no)  #list类型分为str

length=len(text_split_no)#获取处理过的词语长度
topKV=int(length)#关键词数 
print('关键词数: ',topKV)

#基于tf-idf提取关键词
print("基于TF-IDF提取关键词结果：")
keywords = []
for x, w in anls.extract_tags(text_split_no_str, topK=topKV, withWeight=True):
    keywords.append(x)   #前20关键词组成的list
keywords = ' '.join(keywords)   #转为str
print(keywords)
 
 
#画词云

#词云的一系列设置，尺寸，背景颜色，字体和词的数量
w = WordCloud(
    width = 1000, height = 700,
    background_color = "white",
    #设置字体，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
    font_path=fontpath,
    #设置了背景，宽高
    #mask = maskpic, ##############################遮罩
    max_words=10000
    )
w.generate(keywords)   #keywords为字符串类型
w.to_file(respath)#词云保存的名称和格式
plt.imshow(w, interpolation="bilinear")
plt.axis("off")
plt.show()


 
 