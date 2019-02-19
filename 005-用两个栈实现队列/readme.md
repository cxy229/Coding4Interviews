### 题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

### 思路1
- push时，直接push进stack1
- pop时，从stack2中pop，如果stack2为空，就先把stack1中的元素依次存入stack2中，再pop。
