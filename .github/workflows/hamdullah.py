from tabulate import tabulate

data = [['ali', '19', 'paktiawal', '20000'],
        ['haji', '19', 'gardizi', '20000'],
        ['forbad', '19', 'laondan', '20000'],
        ['latif', '19', 'kabloi', '20000'],
        ['ali', '19', 'logar', '20000'],
        ['ali', '19', 'logar', '20000'], ]
header = ['name', 'age', 'last name', 'sallary']
print(tabulate(data, headers=header, tablefmt='heavy_grid'))
