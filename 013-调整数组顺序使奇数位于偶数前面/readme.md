### 题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

### 思路1：新建数组
新建两个数组，遍历array，奇数放入第一个数组，偶数放入第二个数组  
将两个新数组合并，返回  
时间复杂度：O(n)
空间复杂度：O(n)

### 思路2: 类似冒泡排序
类似冒泡排序，每次把一个奇数调整到前面。  
时间复杂度：O(n^2)
空间复杂度：O(1)

### 思路3：双向链表
