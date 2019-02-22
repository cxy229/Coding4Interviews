### 题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

### 思路1
循环exponent次，每次乘以base。  
时间复杂度：O(exponent)

### 思路2（best)
仅需循环次数：
<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\left&space;\lceil&space;\sqrt{exponent}&space;\right&space;\rceil" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\left&space;\lceil&space;\sqrt{exponent}&space;\right&space;\rceil" title="\left \lceil \sqrt{exponent} \right \rceil" /></a>  
比如：`3^5 = (3^4)*3 = ((3^2)^2)*3`  
用思路1需要循环5次，用思路2仅需循环3次。
