#  Программа, которая подбирает пару из двух отсортированных по алфавиту списков,
#  если количество элементов в списках одинаковое.
boys = sorted(['Peter', 'Alex', 'John', 'Arthur', 'Richard'])
girls = sorted(['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'])
if len(boys) == len(girls):
    zipped_pairs = list(zip(boys, girls))
    print('Идеальные пары:')
    for pair in zipped_pairs:
        print(pair[0], 'и', pair[1])
else:
    print('''К сожалению, не хватает претендентов для формирования достаточного количества пар.
    Попробуйте снова позже.''')