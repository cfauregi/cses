def int_input():
	N = input()
	N = N.split(' ')
	if len(N)!=1:
		return [int(i) for i in N]
	else :
		return int(N[0])
 
N = int_input()
 
temp = []
 
for i in range(N):
    temp.append(int_input())
    
for i in temp:
    ligne = i[0]
    colonne = i[1]
 
    if ligne >= colonne :
        if ligne&1!=1:
            res = ligne**2-colonne +1
        else :
            res = (ligne-1)**2+colonne 
    else :
        if colonne &1 ==1:
            res = colonne**2-ligne+1
        else :
            res = (colonne -1)**2 + ligne 
            
    print(res)
