cook_book = {}


def cookbook(file_name):
    with open(file_name, encoding='utf-8') as book:
        name = 'name'
        while name != '':
            name = book.readline().strip()
            cook_book[name] = []
            ingredient_num = int(book.readline().strip())
            for i in range(ingredient_num):
                data = book.readline().strip()
                data = data.split(' | ')
                ingredient = {}
                ingredient['ingredient_name'] = data[0]
                ingredient['quantity'] = data[1]
                ingredient['measure'] = data[2]
                cook_book[name].append(ingredient)
            name = book.readline()


def get_shop_list_by_dishes(person_count, *dishes):
    ingredient = {}
    for dishe in dishes:
        dishe_recept = []
        dishe_recept += cook_book[dishe]
        for i in range(len(cook_book[dishe])):
            if dishe_recept[i]['ingredient_name'] in ingredient:
                ingredient[dishe_recept[i]['ingredient_name']]['quantity'] += \
                    int(dishe_recept[i]['quantity']) * person_count
            else:
                ingredient[dishe_recept[i]['ingredient_name']] = dishe_recept[i]
                del(dishe_recept[i]['ingredient_name'])
                dishe_recept[i]['quantity'] = int(dishe_recept[i]['quantity']) * person_count

    print(ingredient)


cookbook('cook_book.txt')
get_shop_list_by_dishes(2, 'Омлет', 'Фахитос')
