#5.制作三国演义小说threekindoms.txt的词云图，
#要求词云图中重点突出人名，
# 且不包含非语义词语、统一人物的名字，
# 如下图所示，逐步优化词云图。
#去除单字
#去除非语义词语
import jieba
import wordcloud
from collections import Counter
# 读取文本并分词
with open("threekingdoms.txt", "r", encoding="utf-8") as f:
    text = f.read()
words = jieba.lcut(text)
# 定义非语义词语（停止词），可根据需要补充
stopwords = set("的 了 是 在 我 有 和 就 不 人 都 一 一个 上 也 很 到 说 要 去 你 会 着 没有 看 好 自己 这 他 她 它 们 那 里 什么 怎么 如何 因为 所以 但是 如果 虽然 而且 或者 之 与 及 等".split())
# 过滤：去掉单字词、非语义词语、非人名（这里简单保留所有长度>=2且不在停止词中的词）
valid_words = []
for w in words:
    if len(w) >= 2 and w not in stopwords:
        valid_words.append(w)
# 如果需要更精确地突出人名，可以维护一个专门的人名词典（如包含主要人物），这里暂以高频词代替
# 统计词频
word_freq = Counter(valid_words)
# 取前100个高频词（可根据需要调整）
top_words = [word for word, _ in word_freq.most_common(100)]
# 生成词云时，将词语用空格连接
text_for_wc = ' '.join(top_words)
# 配置词云
w = wordcloud.WordCloud(width=1000, height=700,
                        background_color="white",
                        font_path="simhei.ttf",  # 如果中文显示乱码，需指定中文字体路径
                        collocations=False)      # 避免词云自动组合多词
w.generate(text_for_wc)
w.to_file("threekingdoms.png")
