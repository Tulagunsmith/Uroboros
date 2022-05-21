text = ['2018-01-01', 'yandex', 'cpc', 100]
reversed_text = list(reversed(text))

dictionary = {reversed_text[1]: reversed_text[0]}

for i in range(2, len(reversed_text)):
    matreshka = {reversed_text[i]: dictionary}
    dictionary = matreshka
print(matreshka)
# matreshka = reversed_text[0]
# dictionary = {}
# dictionary_2 = {}
# dictionary_3 = {}
# dictionary.setdefault(reversed_text[1], matreshka)
# dictionary_2.setdefault(reversed_text[2], dictionary)
# dictionary_3.setdefault(reversed_text[3], dictionary_2)
#
# print(dictionary_3)
# for i in range(1, len(reversed_text)):
#     dictionary.setdefault(reversed_text[i], reversed_text[i - 1])
#     matreshka = dict(dictionary.items())
#
#     print(dictionary)
# print(matreshka)









# print(creepy)
# creepy2 = {}
# dictionary = {creepy[0]}
# # dictionary.setdefault(creepy[0])
# print(dictionary)
# for i in range(1, len(creepy)):
#     creepy2.setdefault(creepy[i - 1])
#     print(creepy2)

# for key, value in



# word = {}
# creepy2.extend(creepy)
# dictionary = dict(zip(creepy, creepy2))
# for i in range(len(dictionary)):
#
# print(dictionary)



# dictionary = {}
#
# for i in range(len(creepy)):
#
#     dictionary.setdefault(creepy[i])
# # for j in range(len(dictionary)):
# #     word.setdefault()
# word = dictionary.copy()
# third = zip(word, dictionary)
# print(dictionary)
# print(word)
# print(third)