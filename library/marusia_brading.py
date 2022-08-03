def amount():
    braid = input('Введите необходимое количество кос: ')
    if braid.isdigit():
        return int(braid)
    else:
        return False


def total_weight():
    weight = input('Введите расчетный вес материала: ')
    if weight.isdigit():
        return int(weight)
    else:
        return False


def braids_weight():
    braid_selection = (input('Введите (через "пробел") косы какого веса будут использованы в комплекте: ')).split()
    for i in range(len(braid_selection)):
        braid_selection[i] = int(braid_selection[i])
    braid_selection.sort()
    return braid_selection


def counting(remain_weight, braid_weight):
    if remain_weight >= braid_weight:
        remain_weight -= braid_weight
    return remain_weight


def braid_quantity(braid_dict):
    for key, value in braid_dict.items():
        braid_dict[key] = sum(value)
    return braid_dict


weight = total_weight()
braids = braids_weight()
braids_count = {}
pigtails = 0
while weight >= braids[0]:
    for i in range(len(braids) - 1, - 1, - 1):
        if weight >= braids[i]:
            weight = counting(weight, braids[i])
            braids_count.setdefault(braids[i], []).append(1)
        else:
            continue


braids_count = braid_quantity(braids_count)

for mass, quantity in braids_count.items():
    pigtails += quantity
    print(f'Получится {quantity} кос весом {mass} гр.')
print(f'Всего получится {pigtails} кос.')
print(f'Остататок материала {weight} гр.')

