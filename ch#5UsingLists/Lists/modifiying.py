things = ['wood','door','chair','pen','paper','spoon','pen']
print(list(things))

things[1] = 'windows'
print(list(things))

things.append('door')
print(list(things))

things.extend(['frame','painting','table'])

print(list(things))

print(things.index('pen'))
print(things.count('pen'))

del things[things.index('pen')]
print(list(things))
things.remove('pen')
print(list(things))
