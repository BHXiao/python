import hashlib

str0 = 'shdfkahsdfk'

md5 = hashlib.md5()
md5.update(str0.encode())  #  转译
result = md5.hexdigest()
result1 = md5.hexdigest()   #  hexdigest 十六进制   摘要
print(result, result1)


