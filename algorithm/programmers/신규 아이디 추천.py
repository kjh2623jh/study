def solution(new_id):
    txt = '~!@#$%^&*()=+[{]}:?,<>/'
    new_id = new_id.lower()

    def txtreplace(id):
        id = [x for x in id if x not in txt]
        return ''.join(id)
    new_id = txtreplace(new_id)

    def del_dot(txt):
        result = ''
        result+=txt[0]
        for i in range(1, len(txt)):
            if result[-1] != txt[i]:
                result+=txt[i]
            elif txt[i] != '.':
                result +=txt[i]
        return result
    new_id = del_dot(new_id)

    def del_dot2(txt):
        result = list(txt)
        if result[0] == '.': del result[0]
        if result != []:
            if result[-1] == '.': del result[-1]
        return ''.join(result)

    if new_id != '':
        new_id = del_dot2(new_id)

    if len(new_id) > 15: new_id = ''.join(list(new_id)[:15])

    if new_id != '':
        new_id = del_dot2(new_id)

    def filltxt(id, txt):
        while len(id) < 3:
            id+=txt
        return id
    if new_id == '': new_id = filltxt(new_id, 'a')

    if len(new_id) < 3: new_id = filltxt(new_id, new_id[-1])

    return new_id

'''
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
'''

# 100점