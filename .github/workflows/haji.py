from tabulate import tabulate

data = [['ali', '20', 'teacher'],
        ['khan', '22', 'qazi'],
        ['khalil', '34', 'student']]
header = ['name', 'age', 'job']
print(tabulate(data, headers=header, tablefmt='grid'))
