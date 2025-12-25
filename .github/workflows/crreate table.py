from tabulate import tabulate

data = [['tafseer', '1200af', '2025', 'fazalhaq', '4800'],
        ['math', '300af', '2023', 'latif', '489'],
        ['biology', '450af', '2024', 'ali', '900'],
        ['hisab', '130', '2000', 'haron', '240'], ]
header = ['book name', 'price', 'year', 'autor', 'pages']
table = tabulate(data, header, tablefmt='psql')
print(table)
