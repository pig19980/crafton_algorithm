got = input()


def ERROR():
    print(0)
    exit()


class Stack:
    def __init__(self):
        self.arr = []

    def len(self):
        return len(self.arr)

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        if self.len() == 0:
            ERROR()
        ret = self.arr[-1]
        self.arr.pop()
        return ret

    def top(self):
        if self.len() == 0:
            ERROR()
        return self.arr[-1]


stack = Stack()

for c in got:
    # print(c)
    if c == ")":
        if stack.len() == 0:
            ERROR()
        p = stack.pop()
        if p == "(":
            stack.push(2)
        elif type(p) == int:
            val = p
            while type(stack.top()) == int:
                val += stack.top()
                stack.pop()
            if stack.top() != "(":
                ERROR()
            stack.pop()
            stack.push(val * 2)
        else:
            ERROR()

    elif c == "]":
        if stack.len() == 0:
            ERROR()
        p = stack.top()
        stack.pop()
        if p == "[":
            stack.push(3)
        elif type(p) == int:
            val = p
            while type(stack.top()) == int:
                val += stack.top()
                stack.pop()
                if stack.len() == 0:
                    ERROR()
            if stack.top() != "[":
                ERROR()
            stack.pop()
            stack.push(val * 3)
        else:
            ERROR()

    else:
        stack.push(c)

    # print(stack)

sum = 0
for elem in stack.arr:
    if type(elem) != int:
        ERROR()
    sum += elem
print(sum)
