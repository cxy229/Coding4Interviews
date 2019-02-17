### 题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

### 思路1
str转化成list，替换空格，最后再join成str

### 思路2
统计空格数量，开辟数组，遍历填充
>原来str不能被修改内容
比如，下面代码会报错
```
new_s = 'a'*10
new_s[3] = 'b'
print (new_s)
```
output:
```
Traceback (most recent call last):
  File "2019-02-17-001", line 2, in <module>
    new_s[3] = 'b'
TypeError: 'str' object does not support item assignment
```
正确做法是：
```
new_s = ['a']*10
new_s[3] = 'b'
print (''.join(new_s))
```
output:
```
aaabaaaaaa
```
