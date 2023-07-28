def accounting_func(company_type:int, num_employees:int) -> dict:
    '''
    Расчет бухгалтерских услуг на основе количества сотрудников.
    На вход принимается количество сотрудников и тип компании.
    Затем расчитывается стоимость услуг за квартал (для менее 150 операций),
    согласно прейскуранту на сайте buhgalteria-plus.ru
    '''

    ip_tariffs = {'ИП (УСН 6%)':15_500,
                'ИП (УСН 15%, ЕСХН)':17_500,
                'ИП (ОСН)':27_500}
    ooo_tariffs ={'ООО (УСН 6%)':19_000,
                'ООО (УСН 15%, ЕСХН)':22_500,
                'ООО (ОСН)':34_000}
    stdout_tariffs = ip_tariffs if company_type == 1 else ooo_tariffs
    for i in stdout_tariffs:
            stdout_tariffs[i] +=  250 * num_employees
    return stdout_tariffs

