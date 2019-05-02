# Import's
import config
from lib import get_data as gd
from lib import mod_data as md

# Get dataset
b_data = gd.get_url_zip(config.url['url_data'])
b_bbox = gd.get_url_zip(config.url['url_bbox'])

# Divide dataset
# if b_data == b_bbox == True:
#     md.divide_dataset()