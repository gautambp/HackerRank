# @author: Gautam Patel
# Problem Description URL: https://www.hackerrank.com/challenges/validating-email-addresses-with-a-filter-/problem
def fun(s):
    # return True if s is a valid email, else return False
    sp = s.split('@')
    if len(sp) == 2:
        u = sp[0]
        sp = sp[1].split('.')
        if len(u) > 0 and len(sp) == 2:
            w = sp[0]
            e = sp[1]
            if len(w) > 0 and len(e) > 0 and len(e) <= 3:
                if all([i.isalnum() for i in w]):
                    if all([i.isalnum() or i=='_' or i=='-' for i in u]):
                        return True
    return False

