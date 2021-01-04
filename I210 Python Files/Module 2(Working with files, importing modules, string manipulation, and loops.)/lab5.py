#data = [("tyronnosaurus", 16000, 'Carnivore', 'Late Cretaceous'),
#        ("Ankylosaurus", 10000, 'Herbivore', 'Late Cretaceous'),
#        ('Stegosaurus', 6000, 'Herbivore', 'Late Cretaceous'),
#        ('Dienonychus', 175, 'Cornivore', 'Early Creaceous')]
#header = ['Name', 'Weight(lbs)', 'Diet', 'Time']
#output = "{:<15} {:<12} {:<12} {:<12}"
#print(output.format(header[0], header[1], header[2], header[3]))
#print('-' * (5 + len(output.format(header[0], header[1], header[2], header[3]))))
#for entry in data:
#    print(output.format(entry[0], entry[1], entry[2], entry[3]))
    
head = ['Nest', 'Eggs']
lis = []

def table_print(headers, data, formt):
    output = "{:{}} {:{}}"
    print(output.format(headers[0], formt, headers[1], formt))
    print('-' * formt * 2)
    for entry in data:
        dino_name, num_eggs = entry
        print(output.format(dino_name, formt, num_eggs, formt))


width = 0
for i in range(3):
    name = input('Please enter the dinosaurs name: ')
    egg = input('Please enter how many eggs were found: ')
    if len(name) > width:
        width = len(name)
    if len(egg) > width:
        width = len(egg)
    lis.append((name, egg))
    print('Current fossilized dinosaur egg count.')
    table_print(head, lis, width)
    print()



