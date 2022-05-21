total_weight = 400

weight_3 = 0
weight_4 = 0
weight_5 = 0
weight_6 = 0
weight_7 = 0
weight_8 = 0
weight_9 = 0
weight_10 = 0

quantity = 55

common = total_weight // quantity
rest_weight = 400  #total_weight - (common * quantity)
print(rest_weight)
while rest_weight >= 3:
    if rest_weight >= 10:
        rest_weight -= 10
        weight_10 += 1
    if rest_weight >= 9:
        rest_weight -= 9
        weight_9 += 1
    if rest_weight >= 8:
        rest_weight -= 8
        weight_8 += 1
    if rest_weight >= 7:
        rest_weight -= 7
        weight_7 += 1
    if rest_weight >= 6:
        rest_weight -= 6
        weight_6 += 1
    if rest_weight >= 5:
        rest_weight -= 5
        weight_5 += 1
    if rest_weight >= 4:
        rest_weight -= 4
        weight_4 += 1
    if rest_weight >= 3:
        rest_weight -= 3
        weight_3 += 1
print(f'Количество кос по 10 г. {weight_10} шт.\n'
      f'Количество кос по 9 г. {weight_9} шт.\n'
      f'Количество кос по 8 г. {weight_8} шт.\n'
      f'Количество кос по 7 г. {weight_7} шт.\n'
      f'Количество кос по 6 г. {weight_6} шт.\n'
      f'Количество кос по 5 г. {weight_5} шт.\n'
      f'Количество кос по 4 г. {weight_4} шт.\n'
      f'Количество кос по 3 г. {weight_3} шт.')
print(rest_weight)
print('Леша - молодец!')
