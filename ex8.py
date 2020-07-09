WIDGETS = 75
GIZMO = 112

widgets = int(input('Enter the number of widgets: '))
gizmos = int(input('Enter the number of gizmos: '))

total_weight = widgets*WIDGETS + gizmos*GIZMO

print('The total weight of the order is %d grams' %total_weight)