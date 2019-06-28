import  random

class Poem:
    def __init__(self, name, time, poet, content):
        self.name = name
        self.time = time
        self.poet = poet
        self.content = content
        self.index1_list = len(content)
        self.index2_list = []
        for i in range(len(content)):
            self.index2_list.append(len(content[i]))

    def random_generate(self):
        index1 = random.randint(0, len(self.content) - 1)
        index2 = random.randint(0, self.index2_list[index1] - 1)
        sentence = ""
        for i in range(self.index2_list[index2]):
            if (i == index2):
                sentence = sentence + "______________"
            else:
                sentence = sentence + self.content[index1][i]
            if (i == self.index2_list[index2] - 1):
                sentence = sentence + "。"
            else:
                sentence = sentence + "，"
        sentence = sentence + " （" + self.time + "•" + self.poet + " 《" + self.name +"》）"
        return sentence
    
file = open("poem.txt", "r", encoding = 'utf-8')
o_content = file.read()
#poem = Poem("月下独酌", "唐", "李白", [["花间一壶酒", "独酌无相亲"], ["举杯邀明月", "对影成三人"], ["月既不解饮", "影徒随我身"], ["暂伴月将影", "行乐须及春"], ["我歌月徘徊", "我舞影零乱"], ["醒时同交欢", "醉后各分散"], ["永结无情游", "相期邈云汉"]])
#print(poem.random_generate())
file.close()
print(o_content[104])
