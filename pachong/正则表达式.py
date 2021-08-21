import re

res = re.match('hello', 'hello world')
print(res)  # 对象
print(res.group())
r = re.match('[1-9]?[0-9]', '0')
print(r)
print(r.group())


'''
 .      单个字符   回车换行除外  \n
[]      匹配[]中的字符
\d      匹配数字
\D      非数字
\s      匹配空格，tab
\S      非空格
\w      匹配单词字符 a-z A-Z 0-9 _
\W      匹配非单词字符 a-z A-Z 0-9


  *     0次或无数次，可有可无
  +     1次或无数次，至少1次
  ？    1次或0次，判断有或没有
｛m｝   出现m次
｛m,n｝ 出现m-n次

^ 匹配开头
$ 匹配结尾       s$ s结尾

| 或

（）  分组   化一个区域单独匹配  算数中差不多

\num    引用 数字匹配  例  r = re.match(r'<([a-zA-Z]{4})>\w*</\1>','<html>hh</html>') 匹配第一个（）中匹配到的

（？p<name>规则）  分组起别名
（？P=name）




'''
# r = re.match(r'[A-Za-z]\w{3,19}@(qq|12|136).com', 'hell_l@qq.com')
# r = re.match('[a-zA-Z]\\w{3,19}@(qq|12|136)\\.com', 'hell_l@qq.com')
# print(r.group())
# print(r.group())
# print(r.group(1))
r = re.match(r'[a-zA-Z]\w{3,19}@(qq|126|163)\.com', 'hello@qq,com')   # 字符串里点写成了逗号
# r = re.match(r'[a-zA-Z]\w{3,19}@(qq|126|136)\.com', 'hell_l@qq.com')
print(r)
# print(r.group())    #哪 有问题？
# print(r.group())
