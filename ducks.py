https://stepik.org/lesson/296966/step/13?thread=solutions&unit=278694
Дили Вили Били завели себе аккаунты в одной известной соцсети. Их страницы стали пользоваться популярностью и, конечно же, появились поклонники, оставляющие комментарии.  
Ребята решили узнать у кого из них самое большое количество уникальных комментаторов. Ваша задача помочь им в этом и собрать нужную информацию.

l = []
while True:
    i = input()
    if i == 'конец': break
    else: l.append(i.split(': '))
Dili, Bili, Vili = set(), set(), set()
for i in l:
    if i[0] == 'Дили': Dili.add(i[1])
    elif i[0] == 'Били': Bili.add(i[1])
    else: Vili.add(i[1])
    
users = {'Дили': len(Dili), 'Били': len(Bili), 'Вили': len(Vili)}
sorted_dict = {}
sorted_keys = sorted(users, key=users.get)
for i in sorted_keys:
    sorted_dict[i] = users[i]
sorted_dict = list(sorted_dict.items())

print(f'Количество уникальных комментаторов у {sorted_dict[2][0]} - {sorted_dict[2][1]}')
print(f'Количество уникальных комментаторов у {sorted_dict[1][0]} - {sorted_dict[1][1]}')
print(f'Количество уникальных комментаторов у {sorted_dict[0][0]} - {sorted_dict[0][1]}')
