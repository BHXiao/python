import re

# name2 = str(name)
# r = re.findall("[\u4e00-\u9fa5]", "['我们、是不一样的']")
r = re.match(".*?[我们]", "['我们、是不一样的']")
# w = r.group()
print(r.group())   # ['我
r = re.match(".*[我们]", "['我们、是不我们一样的']")
print(r.group())
# r = re.findall('[我们]*', '我们、是我不我们一样的')
# r = re.findall("[\u4e00-\u9fa5]{2,5}", "['我们、是不一样的']")
r = re.search("[\u4e00-\u9fa5]{2,5}", "['我们、是不一样的']")
print(r.group())
# with open(r.group()+'.txt', 'w', encoding='utf-8') as f:
#     f.write(r.group())
