from module import Poem

file = open("poem.txt", "r", encoding = 'utf-8')
original_content = file.read()
#poem = Poem("月下独酌", "唐", "李白", [["花间一壶酒", "独酌无相亲"], ["举杯邀明月", "对影成三人"], ["月既不解饮", "影徒随我身"], ["暂伴月将影", "行乐须及春"], ["我歌月徘徊", "我舞影零乱"], ["醒时同交欢", "醉后各分散"], ["永结无情游", "相期邈云汉"]])
#print(poem.random_generate())
file.close()

