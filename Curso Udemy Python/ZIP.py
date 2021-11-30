from itertools import zip_longest

Str1 = ('Roberto', 'Elaine', 'Francisco')
Str2 = (31, 61, 52)
Str3 = ('Iperó', 'Iperó', 'Ceará')

zip_nome = zip(Str1, Str2, Str3)

print(list(zip_nome))

zipL = zip_longest(Str1, Str2, Str3, fillvalue='-')
print(list(zipL))
