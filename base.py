# Import's
import utils.Utils as utl

# Path's
PATH_DATA = 'WeaponS'
PATH_BBOX = 'WeaponS_bbox'

# Object
obj = utl.Tools()

# Function
obj.xml_to_csv_yolo(path_data=PATH_DATA, path_bbox=PATH_BBOX)