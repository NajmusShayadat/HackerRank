class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, c):
        self.stack.append(c)

    def enqueueCharacter(self, c):
        self.queue.append(c)

    def popCharacter(self):
        ch1 = self.stack.pop()
        return ch1

    def dequeueCharacter(self):
        ch2 = self.queue.pop(0)
        return ch2


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
deque the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
