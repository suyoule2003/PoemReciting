import random

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
        for i in range(self.index2_list[index1]):
            if (i == index2):
                sentence = sentence + "______________"
            else:
                sentence = sentence + self.content[index1][i]
            if (i == self.index2_list[index1] - 1):
                sentence = sentence + "。"
            else:
                sentence = sentence + "，"
        sentence = sentence + " （" + self.time + "•" + self.poet + " 《" + self.name +"》）"
        return sentence
