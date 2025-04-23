"""

THIS IS A TWO STACK PROBLEM

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""
import sys


class min_stack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)


    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1]


    def getMin(self):
        """
        :rtype: int
        """
        temp = sys.maxsize
        for num in self.stack:
            if num < temp:
                temp = num

        return temp



obj = min_stack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.getMin() # return -3
obj.pop()
print(obj.top())    # return 0
print(obj.getMin()) # return -2

"""
But There's Another Issue:
Your getMin() is not O(1) — it loops through the entire stack every time 😬
The problem requires O(1) time for every operation, including getMin().
Upgrade to Two-Stack Solution (O(1) getMin): Uses an extra stack (min_stack) to track the current min at each level.

How min_stack works:
Whenever you push(val), you compare val to the current min:
If val is smaller or equal, it becomes the new min → push it to min_stack
Otherwise, don’t push it to min_stack
When you pop(), if the popped value is also the current min (min_stack[-1]), then pop it from min_stack too.

arr[-1] => The last element of a list 
Operation	stack	        min_stack	min_stack[-1]
push(5)	    [5]	            [5]	            5
push(3)	    [5, 3]	        [5, 3]	        3
push(7)	    [5, 3, 7]	    [5, 3]	        3
push(2)	    [5, 3, 7, 2]	[5, 3, 2]	    2

min_stack[-1] = 2  ← this is the current minimum
"""


class min_stack_using_two_stack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = [] # tracks the min value in the stack at [-1]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]: # first time add or add when val is less than min
            self.min_stack.append(val)



    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

obj_min_stack_using_two_stack = min_stack_using_two_stack()
obj_min_stack_using_two_stack.push(-2)
obj_min_stack_using_two_stack.push(0)
obj_min_stack_using_two_stack.push(-3)
obj_min_stack_using_two_stack.getMin() # return -3
obj_min_stack_using_two_stack.pop()
print(obj_min_stack_using_two_stack.top())    # return 0
print(obj_min_stack_using_two_stack.getMin()) # return -2
