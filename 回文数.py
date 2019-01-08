# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
def isPalindrome(x):
    li = list(str(x))
    if li[0] == '-':
        return False
    else:
        new = [i for i in li]
        new.reverse()
        print(new,li)
        if new == li:
            return True
        else:
            return False

print(isPalindrome(10))
print(isPalindrome(131))
print(isPalindrome(-121))
print(isPalindrome(8888))
print(isPalindrome(9000))
