def solution(ings, menu, sell):
    answer = 0
    dict_ings = {}
    dict_revenue = {}

    for ing in ings:
        ing = ing.split()
        dict_ings[ing[0]] = int(ing[1])

    for x in menu:
        menu_ings = x.split()
        menu_name = menu_ings[0]
        menu_ings_price = 0
        menu_sell_price = int(menu_ings[2])

        for ing in menu_ings[1]:
            menu_ings_price += dict_ings[ing]
            dict_revenue[menu_name] = menu_ings_price

        dict_revenue[menu_name] = menu_sell_price - dict_revenue[menu_name]
    
    for sell_menu in sell:
        sell_menu = sell_menu.split()
        sell_menu_name = sell_menu[0]
        sell_num = int(sell_menu[1])
        answer += dict_revenue[sell_menu_name] * sell_num
 
    return answer


ings = ["r 10", "a 23", "t 124", "k 9"]
menu = ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"]
sell = ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]

print(solution(ings, menu, sell))