#!/usr/bin/env python
# coding: utf-8

# In[8]:


def rent(square: int, district, type: int, special_zone: bool) -> dict:
    '''
    Функция расчета аренды, аренда+ ремонт, аренда+строительство, покупка, покупка+ремонт
    На вход принимается площадь,округ, тип реализации проека, проверка ОЭЗ(особая экономическая зона).
    Эти данные вводит пользователь.
    Выходные данные формируются в словарь.
    '''
    dict_type_rent = {"Аренда здания (требуется ремонт)": 1,
                      "Аренда здания (ремонт не требуется)": 2,
                      "Аренда земли и капитальное строительство": 3,
                      "Покупка здания (ремонт не требуется)": 4,
                      "Покупка здания (требуется ремонт)": 5}

    dict_district = {'Центральный АО': 657.86,  # ЦАО
                     'Северный АО': 1164.55,  # САО
                     'Северо-Восточный АО': 697.97,  # СВАО
                     'Восточный АО': 1064.41,  # ВАО
                     'Юго-Восточный АО': 948.40,  # ЮВАО
                     'Южный АО': 898.01,  # ЮАО
                     'Юго-Западный АО': 1841.33,  # ЮЗАО
                     'Западный АО': 776.76,  # ЗАО
                     'Северо-Западный АО': 600.00,  # СЗАО
                     'Зеленоградский АО': 803.99,  # ЗелАО
                     'Троицкий АО': 670.33,  # ТАО
                     'Новомосковский АО': 685.53}  # НАО
    dict_district_buy = {'Центральный АО': 143790.10,  # ЦАО
                         'Северный АО': 89873.67,  # САО
                         'Северо-Восточный АО': 96446.17,  # СВАО
                         'Восточный АО': 59288.15,  # ВАО
                         'Юго-Восточный АО': 75014.48,  # ЮВАО
                         'Южный АО': 88668.48,  # ЮАО
                         'Юго-Западный АО': 78868.48,  # ЮЗАО
                         'Западный АО': 53327.22,  # ЗАО
                         'Северо-Западный АО': 117696.30,  # СЗАО
                         'Зеленоградский АО': 70926.20,  # ЗелАО
                         'Троицкий АО': 9285.50,  # ТАО
                         'Новомосковский АО': 78000}  # НАО
    dict_kadastr = {'Центральный АО': 63274.79,  # ЦАО
                    'Северный АО': 20532.99,  # САО
                    'Северо-Восточный АО': 19485.33,  # СВАО
                    'Восточный АО': 15492.36,  # ВАО
                    'Юго-Восточный АО': 14086.97,  # ЮВАО
                    'Южный АО': 13510.37,  # ЮАО
                    'Юго-Западный АО': 16423.10,  # ЮЗАО
                    'Западный АО': 11703.22,  # ЗАО
                    'Северо-Западный АО': 19961.59,  # СЗАО
                    'Зеленоградский АО': 4111.50,  # ЗелАО
                    'Троицкий АО': 2890.51,  # ТАО
                    'Новомосковский АО': 5333.94}  # НАО
    dict_sz_rent = {'Восточный АО': 712.5,  # ВАО
                    'Зеленоградский АО': 916.66,  # ЗелАО
                    'Юго-Восточный АО': 1012.50}  # ЮВАО
    for i in dict_type_rent.keys():
        if i == type:
            type = dict_type_rent[i]

    district_of_special_zone_index = ['Восточный АО', 'Зеленоградский АО', 'Юго-Восточный АО']  # ВАО,ЗелАО,ЮВАО
    period = [6, 12]
    cost_of_capital_construction = [80_000, 120_000]
    repair = 5000

    if special_zone:
        if type > 3 or district not in district_of_special_zone_index:
            return "Введены некорректные данные"
        else:
            if type == 2 and district_of_special_zone_index[0] == 1:  # Аренда
                amount_of_rent_sz_6 = round(dict_sz_rent[district] * square, 3) * period[0]
                amount_of_rent_sz_12 = round(dict_sz_rent[district] * square, 3) * period[1]
                res_dict = {'Аренда здания(ремонт не требуется) на 6 месяцев': amount_of_rent_sz_6,
                            'Аренда здания(ремонт не требуется) на 12 месяцев': amount_of_rent_sz_12}
                return res_dict
            elif type == 1 and district_of_special_zone_index[0] == 1:  # Аренда+ремонт
                amount_of_rent_repair_sz_6 = round(dict_sz_rent[district] * square, 3) * period[0] + (repair * square)
                amount_of_rent_repair_sz_12 = round(dict_sz_rent[district] * square, 3) * period[1] + (repair * square)
                res_dict = {'Аренда здания(ремонт требуется) на 6 месяцев': amount_of_rent_repair_sz_6,
                            'Аренда здания(ремонт требуется) на 12 месяцев': amount_of_rent_repair_sz_12}
                return res_dict
            elif type == 3 and district_of_special_zone_index[0] == 1:  # Аренда+строительство
                amount_of_rent_build_sz_6 = [round(dict_sz_rent[district] * square, 3) * period[0] + i for i in
                                             list(map(lambda x: x * square, cost_of_capital_construction))]
                amount_of_rent_build_sz_12 = [round(dict_sz_rent[district] * square, 3) * period[1] + i for i in
                                              list(map(lambda x: x * square, cost_of_capital_construction))]
                res_dict = {'Аренда здания(на 6 месяцев) и капитальное строительство': amount_of_rent_build_sz_6,
                            'Аренда здания(на 12 месяцев) и капитальное строительство': amount_of_rent_build_sz_12}
                return res_dict
            elif type == 2 and district_of_special_zone_index[1] == 3:  # Аренда
                amount_of_rent_sz_6 = round(dict_sz_rent[district] * square, 3) * period[0]
                amount_of_rent_sz_12 = round(dict_sz_rent[district] * square, 3) * period[1]
                res_dict = {'Аренда здания(ремонт не требуется) на 6 месяцев': amount_of_rent_sz_6,
                            'Аренда здания(ремонт не требуется) на 12 месяцев': amount_of_rent_sz_12}
                return res_dict
            elif type == 1 and district_of_special_zone_index[1] == 3:  # Аренда+ремонт
                amount_of_rent_repair_sz_6 = round(dict_sz_rent[district] * square, 3) * period[0] + (repair * square)
                amount_of_rent_repair_sz_12 = round(dict_sz_rent[district] * square, 3) * period[1] + (repair * square)
                res_dict = {'Аренда здания(ремонт требуется) на 6 месяцев': amount_of_rent_repair_sz_6,
                            'Аренда здания(ремонт требуется) на 12 месяцев': amount_of_rent_repair_sz_12}
                return res_dict
            elif type == 3 and district_of_special_zone_index[1] == 3:  # Аренда+строительство
                amount_of_rent_build_sz_6 = [round(dict_sz_rent[district] * square, 3) * period[0] + i for i in
                                             list(map(lambda x: x * square, cost_of_capital_construction))]
                amount_of_rent_build_sz_12 = [round(dict_sz_rent[district] * square, 3) * period[1] + i for i in
                                              list(map(lambda x: x * square, cost_of_capital_construction))]
                res_dict = {'Аренда здания(на 6 месяцев) и капитальное строительство': amount_of_rent_build_sz_6,
                            'Аренда здания(на 12 месяцев) и капитальное строительство': amount_of_rent_build_sz_12}
                return res_dict
            elif type == 2 and district_of_special_zone_index[2] == 11:  # Аренда
                amount_of_rent_sz_6 = round(dict_sz_rent[district] * square, 3) * period[0]
                amount_of_rent_sz_12 = round(dict_sz_rent[district] * square, 3) * period[1]
                res_dict = {'Аренда здания(ремонт не требуется) на 6 месяцев': amount_of_rent_sz_6,
                            'Аренда здания(ремонт не требуется) на 12 месяцев': amount_of_rent_sz_12}
                return res_dict
            elif type == 1 and district_of_special_zone_index[2] == 11:  # Аренда+ремонт
                amount_of_rent_repair_sz_6 = round(dict_sz_rent[district] * square, 3) * period[0] + (repair * square)
                amount_of_rent_repair_sz_12 = round(dict_sz_rent[district] * square, 3) * period[1] + (repair * square)
                res_dict = {'Аренда здания(ремонт требуется) на 6 месяцев': amount_of_rent_repair_sz_6,
                            'Аренда здания(ремонт требуется) на 12 месяцев': amount_of_rent_repair_sz_12}
                return res_dict
            elif type == 3 and district_of_special_zone_index[2] == 11:  # Аренда+строительство
                amount_of_rent_build_sz_6 = [round(dict_sz_rent[district] * square, 3) * period[0] + i for i in
                                             list(map(lambda x: x * square, cost_of_capital_construction))]
                amount_of_rent_build_sz_12 = [round(dict_sz_rent[district] * square, 3) * period[1] + i for i in
                                              list(map(lambda x: x * square, cost_of_capital_construction))]
                res_dict = {'Аренда здания(на 6 месяцев) и капитальное строительство': amount_of_rent_build_sz_6,
                            'Аренда здания(на 12 месяцев) и капитальное строительство': amount_of_rent_build_sz_12}
                return res_dict

    else:
        if type == 2:  # Аренда
            amount_of_rent_perdistrict_6 = round(dict_district[district] * square, 3) * period[0]  # Аренда за 6 месяцев
            amount_of_rent_perdistrict_12 = round(dict_district[district] * square, 3) * period[1]  # Арена за 12 месцев
            res_dict = {'Аренда здания(ремонт не требуется) на 6 месяцев': amount_of_rent_perdistrict_6,
                        'Аренда здания(ремонт не требуется) на 12 месяцев': amount_of_rent_perdistrict_12}
            return res_dict
        elif type == 1:  # Аренда + ремонт
            amount_of_rent_repair_6 = round(dict_district[district] * square, 3) * period[0] + (repair * square)
            amount_of_rent_repair_12 = round(dict_district[district] * square, 3) * period[1] + (repair * square)
            res_dict = {'Аренда здания(ремонт требуется) на 6 месяцев': amount_of_rent_repair_6,
                        'Аренда здания(ремонт требуется) на 12 месяцев': amount_of_rent_repair_12}
            return res_dict
        elif type == 3:  # Аренда+строительство
            amount_of_rent_build_6 = [round(dict_district[district] * square, 3) * period[0] + i for i in
                                      list(map(lambda x: x * square, cost_of_capital_construction))]
            amount_of_rent_build_12 = [round(dict_district[district] * square, 3) * period[1] + i for i in
                                       list(map(lambda x: x * square, cost_of_capital_construction))]
            res_dict = {'Аренда здания(на 6 месяцев) и капитальное строительство': amount_of_rent_build_6,
                        'Аренда здания(на 12 месяцев) и капитальное строительство': amount_of_rent_build_12}
            return res_dict
        elif type == 4:  # Покупка
            amount_of_buy = round(dict_district_buy[district] * square, 3) + (dict_kadastr[district] * square) * 1.9 + (
                        dict_kadastr[
                            district] * square) * 1.5  # покупка+ сумма налога на имущество за год + сумма налога на землю за год
            res_dict = {'Покупка здания(ремонт не требуется)': amount_of_buy}
            return res_dict
        elif type == 5:  # Покупка + ремонт
            amount_of_buy_repair = round(dict_district_buy[district] * square, 3) + (
                        dict_kadastr[district] * square) * 1.9 + (
                                               dict_kadastr[district] * square) * 1.5 + repair * square
            res_dict = {'Покупка здания(ремонт требуется)': amount_of_buy_repair}
            return res_dict

    #print('Введены некорректные данные')

# In[10]:


# rent(square=100, district=1, type=1, special_zone=False)

