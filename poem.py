from module import Poem

file = open("poem.txt", "r", encoding = "utf-8")
original_content = file.read()
#poem = Poem("月下独酌", "唐", "李白", [["花间一壶酒", "独酌无相亲"], ["举杯邀明月", "对影成三人"], ["月既不解饮", "影徒随我身"], ["暂伴月将影", "行乐须及春"], ["我歌月徘徊", "我舞影零乱"], ["醒时同交欢", "醉后各分散"], ["永结无情游", "相期邈云汉"]])
#print(poem.random_generate())
file.close()

poem_pointer = []
for i in range(len(original_content)):
    if original_content[i] == "[":
        for j in range(i + 1, len(original_content)):
            if original_content[j] == "]":
                poem_pointer.append([i + 2, j - 2])
                break
poem = []
for i in range(len(poem_pointer)):
    for j in range(poem_pointer[i][0], poem_pointer[i][1] + 1):
        if original_content[j] == "\n":
            poem_name_pointer = [poem_pointer[i][0], j - 1]
            break
    poem_name = original_content[poem_name_pointer[0]:poem_name_pointer[1] + 1]
    for j in range(poem_name_pointer[1] + 2, poem_pointer[i][1] + 1):
        if original_content[j] == "\n":
            poem_time_pointer = [poem_name_pointer[1] + 2, j - 1]
            break
    poem_time = original_content[poem_time_pointer[0]:poem_time_pointer[1] + 1]
    for j in range(poem_time_pointer[1] + 2, poem_pointer[i][1] + 1):
        if original_content[j] == "\n":
            poem_poet_pointer = [poem_time_pointer[1] + 2, j - 1]
            break
    poem_poet = original_content[poem_poet_pointer[0]:poem_poet_pointer[1] + 1]
    content = []
    content_front_pointer = poem_poet_pointer[1] + 2
    for j in range(poem_poet_pointer[1] + 2,poem_pointer[i][1] + 1):
        if original_content[j] == "。":
            content_last_pointer = j
            sentence = []
            sentence_front_pointer = content_front_pointer
            for k in range(content_front_pointer, content_last_pointer + 1):
                if original_content[k] == "，" or original_content[k] == "。":
                    sentence_last_pointer = k - 1
                    sentence.append(original_content[sentence_front_pointer:sentence_last_pointer + 1])
                    sentence_front_pointer = sentence_last_pointer + 2
            content.append(sentence)
            content_front_pointer = content_last_pointer + 2
    poem.append(Poem(poem_name, poem_time, poem_poet, content))
for i in range(len(poem)):
    print(poem[i].random_generate())
input("")
