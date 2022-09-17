def fast_return(i):
	alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"	
	for j in range(len(alph)) :
		if i == alph[j]:
			return 1, j
	return 0
N =input()
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"	
tab = [0] *26
temp = 0
h = 0
for i in N:
	temp,h = fast_return(i)
	tab[h]+= temp

string = ""
tt = 0
h=0
for i in tab :
	if i%2!=0:
		h+=1
if h > 1 :
	print("NO SOLUTION")

else :
	for i in range(len(alph)):
		tt = tab[i]/2
		if tt % 1 != 0 :
			impair = alph[i]
			tt = int(tt)
		else :
			tt = int(tt)
		tab[i] = tt
		string+=alph[i]*tt
	if len(N)%2 != 0 :
		string_to_print = string +impair+ string[::-1]
	else :
		string_to_print = string + string[::-1]
	print(string_to_print)

