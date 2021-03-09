input = "abba"
last = len(input)-1
first=0



def is_palindrome(string):
    if len(string)<1:
        return True
    last = len(string)-1
    if string[last]==string[0]:
        return is_palindrome(string[1:last-1])
    else:
        return False
    


print(is_palindrome(input))