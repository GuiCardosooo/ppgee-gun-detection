# Import's
import config
from tools import get_data as gd

# import tools.Tools as utl

# Get dataset
b_data = gd.get_url_zip(url=config.paths['url_data'],
    new_dir=config.paths['lb_data'])
b_bbox = gd.get_url_zip(url=config.paths['url_bbox'],
    new_dir=config.paths['lb_bbox'])

# if b_data == b_bbox == True:
#     print('Teste')

# obj.xml_to_csv(path_data=PATH_DATA, path_bbox=PATH_BBOX)

# dir_arquivo = os.path.join(os.getcwd(), PATH_DATA, 'images.txt')

# for line in os.listdir(PATH_DATA):
#     if not os.path.exists(dir_arquivo):
#       with open(dir_arquivo, 'w+') as out_arq:
#             out_arq.write(os.path.join(os.getcwd(), PATH_DATA, line))
#     else:
#         with open(dir_arquivo, 'a+') as out_arq:
#             out_arq.write('\n' + os.path.join(os.getcwd(), PATH_DATA, line))