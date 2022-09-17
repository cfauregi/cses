test = "MWNYFUIRUX"
print(len(test))
print(len(set(test)))

print("a")
print("a"*5)
print("a"*0)
print(3.5%0.5)
print(3.5%1)

print(0%1)

for i in range(0,11):
	print((i/10)%1)

file = open("log.txt","r")
string = file.read()[:-1:]
file.close()

#print(string)


tab = ["a", "ccc", "b", "e", "ff"]
tab.sort(key = len)
print(tab[::-1])
tab = tab[::-1]

string = ""

for i in tab:
	string+=i
print(string)
