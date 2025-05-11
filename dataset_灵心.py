import json
# with open("data/SoulChatCorpus-sft-multi-Turn.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
# dataset = []
# for item in data:
#     conversations = []
#     for msg in item["messages"]:
#         conversations.append({"from": "human" if msg["role"] == "user" else "gpt", "value": msg["content"]})
#     dataset.append({"conversations": conversations})

# with open("dataset.json", "w", encoding="utf-8") as f:
#     json.dump(dataset, f, indent=2, ensure_ascii=False)

with open("/mnt/workspace/formatted_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data[0])
    print(len(data))

# {'conversations': [{'from': 'human', 'value': '最近感觉很焦虑，不知道如何缓解。'}, {'from': 'gpt', 'value': '我明白你的感受。首先，要知道焦虑是一种正常的情绪。但是，当它影响到你的生活质量时，就需要采取行动了。'}, {'from': 'human', 'value': '可是我总觉得自己做什么都不够好，很害怕失败。'}, {'from': 'gpt', 'value': '这可能是完美主义导致的。完美主义者总是把难度设置得很高，并在失败时很难接受自己。其实，你是一个有自尊和价值的人，无论成败。'}, {'from': 'human', 'value': '但是我总是无法集中注意力，会经常拖延。'}, {'from': 'gpt', 'value': '拖延是一种很常见的自我保护机制，但长期下来对心理健康负面影响很大。你可以尝试分段任务，每段任务完成后休息片刻，然后继续下一个任务。'}, {'from': 'human', 'value': '但是每天都很疲惫，很难找到动力去改变。'}, {'from': 'gpt', 'value': '情绪低落，疲惫和动力不足是相互作用的。你可以尝试建立自己的日常规划，合理分配时间，保证充足的睡眠和营养，以此建立更加健康的自己。'}, {'from': 'human', 'value': '其实我很害怕自己无法排解焦虑情绪。'}, {'from': 'gpt', 'value': '我会一直在这里支持你，并分享一些我的应对技巧。你可以与朋友交流，寻求专业帮助，做一些自己感兴趣的事情，放松身心。'}, {'from': 'human', 'value': '我会尝试这些方法，谢谢你的支持和理解。'}, {'from': 'gpt', 'value': '不要忘记，焦虑并不是终点，而是一个可以克服的过程。你是勇敢的，你可以做到。任何时候，都欢迎你来和我交流。'}]}