import jsonpath

data = {'key1': {'key2': {'key3': {'key4': {'key5': {'key6': {'key7': 'python'}}}}}}}
#  提取数据
result = data['key1']['key2']['key3']['key4']['key5']['key6']['key7']
print(result)
print(jsonpath.jsonpath(data, '$.key1'))  # 取从根节点第一个值
# [{'key2': {'key3': {'key4': {'key5': {'key6': {'key7': 'python'}}}}}}]
print(jsonpath.jsonpath(data, '$.key1.key2.key3.key4.key5.key6.key7'))
print(jsonpath.jsonpath(data, '$..key7'))

# Traceback (most recent call last):     注意写的文件名 import jsonpath  不能一样
#   File "D:/python/pachong/jsonpath.py", line 1, in <module>
#     import jsonpath
#   File "D:\python\pachong\jsonpath.py", line 8, in <module>
#     print(jsonpath.jsonpath(data, '$.key1'))  # 取从根节点第一个值
# TypeError: 'module' object is not callable
