#counting to twenty
for number in range(1 , 21):
  print(number)


#one million
million = list(range(1, 1000001))
for number in million:
  print(number)

#summing a million
million = list(range(1, 1000001))
print(min(million))
print(max(million))
print(sum(million))


#odd numbers
odd_numbers = list(range(1, 20 , 2))
for odd in odd_numbers:
  print(f"{odd} is an odd number")


#threes
three_multiples = list(range(3 , 30 ,3))
for threes in three_multiples:
  print(f"{threes} is a multiple of three ")

#cubes
cubes = []
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)
print(cubes)


#cube comprehension
cubes = [number **3 for number in range(1 ,11)]
print(cubes)