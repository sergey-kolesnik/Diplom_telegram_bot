def year_calculate_output(start, stop):
    for year in range(start, stop + 1):
        for check in range(10):
            count = 0
            for number in str(year):
                if int(number) == int(check):
                    count += 1
                if count >= 3:
                    print(year)


start_year = int(input('Введите первый год: '))
stop_year = int(input('Введите последний год: '))
print(f'Года от {start_year} до {stop_year} c тремя одинаковыми цифрами :')


year_calculate_output(start_year, stop_year)