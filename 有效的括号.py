'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:
[((({)))]
输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
'''
({}[[]()])

def isValid(s):
    valid = {'(': ')', '{': '}', '[': ']'}
    left = list(valid.keys())
    n = 0
    s = list(s)
    for x in s:
        if x in left:
            try:
                s.index(valid[x])
                if valid[x] == 1:
                    return True
                else:
                    n += 1
                    print(n)
                    print(s[1:s.index(valid[x])])
                    return isValid(s[1:s.index(valid[x])])
            except ValueError:
                # print(1)
                return False
        else:
            # print(2)
            return False


print(isValid('[((()))]'))
