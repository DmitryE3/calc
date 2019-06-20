year = None
while not isinstance(year, int):
    try:
        year = int(input('Введите год: '))
    except:
        year = None
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print('not intercalary year')
else:
    print('intercalary year')
