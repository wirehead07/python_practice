motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

children = []
children.append('Estee')
children.append('Atticus')
children.append('Tobias')
print(children)

children.insert(3, 'Jack')
print(children)

del children[3]
print(children)