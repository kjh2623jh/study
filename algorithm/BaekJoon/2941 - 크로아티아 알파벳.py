# https://www.acmicpc.net/problem/2941

"""
č 	c=
ć 	c-
dž 	dz=
đ 	d-
lj 	lj
nj 	nj
š 	s=
ž 	z=
"""

word = input()
for w in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    word = word.replace(w, "0")
print(len(word))