def roundup(N):
	return int(N)+1
import time  
N =input()
#file = open("test_input.txt","r")
#N = file.read()
#file.close()
temps = time.time()
if len(set(N))==1:
	print(N)
else :

	tab = [0]*26;
	sum_tab=0
	for j in N:
		for i in range(65,91):
			if i==ord(j):
				tab[i-65]+=1
				sum_tab+=1
				break
	#print("temps post remplissage tab ", time.time()-temps)
	temp = 0
	for i in tab:
		if i%2!=0:
			temp+=1
		if temp>1:
			print("NO SOLUTION")
			break
	#ord("A") pour la valeur ascii
	#cht(65) pour afficher le chr de la valuer ASCII

	# Si string = BAACCCC
	# tab = [ 2, 1, 4, ... ]
	#if (len(set(N)))<=roundup(len(N)/2):
	to_print=""
	if temp<2:
		for i in range(len(tab)):
			if tab[i]==1:
				tab[i]==1
			else :
				tab[i]=int(tab[i]/2)
		#while(maxi>int(maxi_temoin/2)):
		temps = time.time()
		for i in range(65,91):
			for j in range(0,tab[i-65]):
				to_print+=chr(i)
		#print("temps concaténation", time.time()-temps)
		if (len(to_print)%2 !=0) and sum_tab%2!=0:
			print(to_print[0:-1:]+to_print[::-1])			
		else :
			print(to_print+to_print[::-1])
			































	
