from tabulate import tabulate

table = [['Nombre', 'Ak', 'Rank'],
        ['Eduardo', 'El king', 1], 
        ['Daniel', 'El Pastor', 2], 
        ['Steven', 'Cirilo', 3],
        ['Erycherd', 'Gargajo', 4],
        ['Christian', 'Panadero',5],
        ['Carlos J', 'EHA', 6]        
    ]    

title = '\n**** Mundial de pronosticos ****\n'

print(title)
print(tabulate(table, headers='firstrow', tablefmt='grid'), '\n')