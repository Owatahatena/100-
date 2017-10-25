s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

s = s.replace(",",'')
s= s.replace(".","")
s = s.split(" ")

print(s)
s_list = []

for a in s:
	s_list.append(len(a))

print(s_list)