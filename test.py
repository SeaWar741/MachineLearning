names = ['pepe','raul','Josefina de la fuente','penelope']
print("el nombre mayor es:",max(names, key=lambda name: len(name)))
print("nombres sorted case insensitve", sorted(names, key=lambda name: name.lower()))
print(names)
print("el nombre mas pequeño es:",max(names, key=lambda name:min(name)))

