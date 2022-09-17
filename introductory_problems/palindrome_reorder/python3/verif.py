def fast_return(i):
	alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"	
	for j in range(len(alph)) :
		if i == alph[j]:
			return 1, j
	return 0

file = open("log.txt","r")
string_me = file.read()[:-1:]
file.close()

file = open("test_output_test9.txt","r")
string_test = file.read()[:-1:]
file.close()

print("Ma len ", len(string_me))
print("Sa len ", len(string_test))

print("Ma set ", set(string_me))
print("Sa set ", set(string_test))

print("Mid string_me  ", string_me[int(len(string_me)/2)-5:int(len(string_me)/2)+5:])
print("Mid string_test", string_test[int(len(string_test)/2)-5:int(len(string_test)/2)+5:])
	

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"	
tab_me = [0] *26
temp = 0
h = 0
for i in string_me:
	temp,h = fast_return(i)
	tab_me[h]+= temp
print("tab me ", tab_me)
for i in tab_me :
	print(i/2)

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"	
tab_test = [0] *26
temp = 0
h = 0
for i in string_test:
	temp,h = fast_return(i)
	tab_test[h]+= temp
print("tab test", tab_test)
for i in tab_test:
	print(i/2)
for i in range(len(tab_me)):
	if tab_me[i]!=tab_test[i]:
		print("lettre faisant probleme ", alph[i])
		print("différence entre moi et test de ", tab_me[i]-tab_test[i])




