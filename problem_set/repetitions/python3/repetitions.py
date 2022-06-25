string = input()

i_min = string[0]
string=string
indice = 0
max_indice = 0
for i in string :
	if i_min == i :
		indice+=1
	else :
		i_min = i
		indice =1

	if indice>max_indice:
		max_indice=indice
	
	#print("iem    ",i)
	#print("ieme-1 ",i_min)
#if indice!=0 and i_min == string[-1::] and indice+1>max_indice:
	#max_indice+=1
#print()
#print(i_min)
#print(string[-1::])
print(max_indice)
		
