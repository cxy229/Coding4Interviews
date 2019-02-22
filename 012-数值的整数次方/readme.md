### 题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

### 思路1
循环exponent次，每次乘以base。
时间复杂度：O(exponent)

### 思路2（best)
仅需循环$$\left \lceil \sqrt{exponent} \right \rceil$$次。
