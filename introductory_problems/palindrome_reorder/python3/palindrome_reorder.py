def roundup(N):
	return int(N)+1
 
N =input()
 
if len(N)%2==0:
	print("NO SOLUTION")
else:
	if len(set(N))==1:
		print(N[0]*len(N))
	else :
		if (len(set(N)))<=roundup(len(N)/2):
			tab = [0]*26;
			for i in range(65,91):
				for j in N:
#					print(ord(j))
					if i==ord(j):
						tab[i-65]+=1
					
				
			#	ord("A") pour la valeur ascii
			maxi = max(tab)
			while len(set(tab))!=1:
				if maxi%2==0:
					for i in range(65,91):
						if tab[i-65]==maxi:
							print(chr(i))
							tab[i-65]-=1
							#print("c'est ici")
				else :
					j=25
					for i in range(65,91):
						if tab[j]==maxi:
							print(chr(j+65))
							tab[j]-=1
						j-=1
				maxi=maxi-1
		else :
			print("NO SOLUTION")
	

 
#for i in range(65,91):
#	print(chr(i))
#print(tab) 
#print(len(tab))
#tab.sort(reverse=True)
#print(tab)
#print(len(set(N)))
#print(roundup(len(N)/2))
#print(set(N))
#print(N)
