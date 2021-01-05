
fisier= r"C:\Users\Anelia Babuc\workspace\Proiect_Jess_Teletin_Babuc\graf.txt"
f = open(fisier, 'r')

lfile = f.read().split('\n')
print(lfile)

ln1 = []
for i in lfile:
    ln1.append(i.split(" "))
print(ln1)

teams = []
for echipe in ln1:
    for i in range(len(echipe)):
        if i==2:
            teams.append(echipe[i][:-1])
print(teams)

cod = []
for echipe in ln1:
    for i in range(len(echipe)):
        if i==8:
            cod.append(echipe[i][:-1])
print(cod)

tara = []
for echipe in ln1:
    for i in range(len(echipe)):
        if i==4:
            tara.append(echipe[i][:-1])
print(tara)

palarie = []
for echipe in ln1:
    for i in range(len(echipe)):
        if i==6:
            palarie.append(echipe[i][:-1])
print(palarie)

string = ""
for i in range(len(teams)):
    string += teams[i] + " " + cod[i] + " " + tara[i] + " " + palarie[i] + '\n'
print(string)

g = open("Graph.txt", "w")
g.write(string)
g.close()
