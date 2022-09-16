def roundup(N):
	return int(N)+1
import time  
N	 =input()
#file = open("test_input.txt","r")
#N = file.read()
#file.close()
temps = time.time()
N_temp = N
if len(set(N))==1:
	print(N)
else :

	tab = [0]*26;
	sum_tab=0
	for i in range(65,91):
		N_new = N.replace(str(chr(i)),"")
		tab[i-65]+= len(N)-len(N_new)
		sum_tab+= len(N) - len(N_new)
		N = N_new
		
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
			if (len(N_temp)%2 == 1):
				print(to_print[:-1:]+to_print[::-1])
			else :
				print(to_print+to_print[::-1])
#print(len(N))
#N = N.replace(str(chr(65)),"")
#print(len(N))			
#print(tab)




























	
