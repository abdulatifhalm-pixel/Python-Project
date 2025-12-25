from tabulate import tabulate

data = [['ali', '18', 'student', ''],
        ['mahmood', '20', 'bachler'],
        ['latif', '33', 'teacher'],
        ['khan', '73', 'doctor'],
        ['haji', '19', 'skyridder']]
header = ['name', 'age', 'job']
print(tabulate(data, headers=header, tablefmt='double_grid'))
