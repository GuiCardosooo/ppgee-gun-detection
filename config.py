# -*- coding: utf-8 -*-
# UFES - Universidade Federal do Espiríto Santo
# Gun Detection
# Written by Guilherme Cardoso


"""
Full documentation is at:
<https://github.com/GuiCardosooo/ppgee-gun-detection>.
"""

## Configurações referente a estrutura da base de dados

# URL's: Tuple => (url, rename_zip)
url = {
    'url_data': ('https://sci2s.ugr.es/sites/default/files/files/TematicWebSites/WeaponsDetection/BasesDeDatos/WeaponS.zip', 'data'),
    'url_bbox': ('https://sci2s.ugr.es/sites/default/files/files/TematicWebSites/WeaponsDetection/BasesDeDatos/WeaponS_bbox.zip', 'bbox')
}

# Path's
paths = {
    'database': 'db',
    'train': 'train',
    'valid': 'valid',
    'test': 'test',
    'data': 'data',
    'bbox': 'bbox'
}

## Configurações referente ao treinamento

# Parameters [0~1]
param = {
    'train': 0.8,
    'valid': 0.2
}

# Classes
classes = {
    'pistol': 0
}