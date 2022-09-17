def roundup(N):
	return int(N)+1

def fast(N,i):
	for j in N:
		if i==ord(j):
			return 1
	return 0

def the_fast(j):
	for i in range(65,91):
		if i==ord(j):
			return 1 ,i 
		elif j=='\n':
			return 0, 65
	return 0

def fast_return(i):
	alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"	
	for j in range(len(alph)) :
		if i == alph[j]:
			return 1, j
	return 0
N =input()
#file = open("test_input_test9.txt","r")

#N = file.read()
#N = N[:-1:]
#file.close()

#print("set de N",set(N))
#print("len de N",len(N))
#print("len/set de N",len(N)/len(set(N)))

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"	
tab = [0] *26
temp = 0
h = 0
for i in N:

	#for j in alph :
	#	if i == j:
	#		temp+=1
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
		#print(tt,end="   ")
		#if tt == 0.5:
		#	tt=1
		if tt % 1 != 0 :
			impair = alph[i]
			tt = int(tt)
		else :
			tt = int(tt)
		tab[i] = tt
		#print(tt)
		string+=alph[i]*tt
	#full_tab = []
	#for i in range(len(alph)):
	#	full_tab.append(alph[i]*tab[i])
	#print(full_tab)
	#full_tab.sort(key=len)
	#full_tab = full_tab[::-1]
	#print("jerome",full_tab)
	#string =""
	#for i in range(len(full_tab)):
		#print(i)
	#	string += full_tab[i]
	#print(string)
	#print(impair)
	if len(N)%2 != 0 :
		string_to_print = string +impair+ string[::-1]
	else :
		string_to_print = string + string[::-1]
	print(string_to_print)

#print(temp)
#print(tab)
