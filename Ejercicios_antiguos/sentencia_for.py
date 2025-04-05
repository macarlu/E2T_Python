# midiendo cadenas

words = ["cat", "window", "defenestrate"]
for w in words:
    print(w, len(w))
print("---------------")

# creamos un diccionario
users = {"Hans" : "active", "Eleonore" : "inactive", "Shon" : "active"}

# Estrategia: iterar sobre una copia
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

# Estrategia: crear un nuevo diccionario
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status
        print(active_users)
print("---------------")

# La función range()
for i in range(5):
    print(i)
print("---------------")
list(range(5, 10))
#genera el resultado de abajo
print(list(range(5, 10)))
# el tercer argumento indica el incremento con el que cuenta
list(range(0, 10, 2))
print(list(range(0, 10, 2)))
print("---------------")
# para iterar sobre los indices se pueden combinar range() y len()
a = ["Mary", "had", "a","little", "lamb"]
for i in range(len(a)):
    print(i, a[i])
