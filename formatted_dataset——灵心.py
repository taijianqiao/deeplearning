
import json

# 讀取 JSON 檔案
with open("dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 轉換每個 conversation
for item in data:  # 遍歷每個對話
    formatted_text = "<|begin_of_text|>\n"
    for msg in item["conversations"]:
        role_tag = "<|start_header_id|>user<|end_header_id|>" if msg["from"] == "human" else "<|start_header_id|>assistant<|end_header_id|>"
        formatted_text += f"{role_tag}\n\n{msg['value']}<|eot_id|>\n"
    
    # 新增 text 欄位
    item["text"] = formatted_text

# 儲存為 JSON 檔案
with open("formatted_dataset.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

