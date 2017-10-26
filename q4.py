s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

s = s.split(" ")

num = [1, 5, 6, 7, 8, 9, 15, 16, 19]

dic = {}

for a in s:
    tmp = s.index(a)
    if tmp in num:
        dic.update({tmp:a[:1]})
    else:
        dic.update({tmp:a[:2]})

print(dic)
