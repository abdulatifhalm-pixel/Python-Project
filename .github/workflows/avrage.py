from prettytable import PrettyTable

mytable = PrettyTable(['name', 'age', 'class', 'id', 'add'])
mytable.add_row(['asad', '15', '11', '098798', 'kabul'])
mytable.add_row(['ali', '16', '12', '0985598', 'paktia'])
mytable.add_row(['zahid', '17', '12', '098798', 'paktia'])
mytable.add_autoindex('number')
print(mytable)
