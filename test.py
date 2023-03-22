import re

with open('./README.md','r',encoding='utf-8')as f:
    full_text = f.read()

result = re.findall(r'(\n目标地址: .*?)\n描述:', full_text,re.S)
for r in result:
    full_text = full_text.replace(r,'')
with open('./README.md','w',encoding='utf-8')as f:
    f.write(full_text)