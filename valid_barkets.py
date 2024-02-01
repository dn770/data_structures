from stack import Stack


def valid_barkets(s):
    brkt_dict = {"(": ")", "[": "]", "{": "}"}
    brkt_stack = Stack()
    if not len(s) % 2 == 0:
        return False
    for brk in s:
        if brk in brkt_dict:
            brkt_stack.push(brk)
        elif brkt_stack.is_empty():
            return False
        elif not brk == brkt_dict[brkt_stack.pop()]:
            return False
    return brkt_stack.is_empty()

print(valid_barkets("([{}])"))