# Import's
import os
import tools.Tools as utl

# Path's
PATH_DATA = 'WeaponS'
PATH_BBOX = 'WeaponS_bbox'

# Object
obj = utl.Tools()

# Function
obj.xml_to_csv(path_data=PATH_DATA, path_bbox=PATH_BBOX)

dir_arquivo = os.path.join(os.getcwd(), PATH_DATA, 'images.txt')

for line in os.listdir(PATH_DATA):
    if not os.path.exists(dir_arquivo):
      with open(dir_arquivo, 'w+') as out_arq:
            out_arq.write(os.path.join(os.getcwd(), PATH_DATA, line))
    else:
        with open(dir_arquivo, 'a+') as out_arq:
            out_arq.write('\n' + os.path.join(os.getcwd(), PATH_DATA, line))