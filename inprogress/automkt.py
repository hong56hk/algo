vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort()

print(vowels)

dd = [
  (0,10),(22,33), (1,4), (9, 12), (15,20)
]

dd.sort(key=lambda x : x[0])

print(dd)
