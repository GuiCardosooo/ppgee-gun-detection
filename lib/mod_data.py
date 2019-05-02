# -*- coding: utf-8 -*-
# UFES - Universidade Federal do Espiríto Santo
# Gun Detection
# Written by Guilherme Cardoso


"""
Full documentation is at:
<https://github.com/GuiCardosooo/ppgee-gun-detection>.
"""


# __all__ = ['create_annotations']
__author__ = ('Guilherme Vinícius Simões Cardoso <cardoso.guivi@gmail.com>')

import os
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
from glob import glob
from shutil import copyfile

# Importa o arquivo de configuração
import sys
sys.path.insert(0, os.getcwd())
import config


# Cria os paths do projeto
class _PathsAndLists:
    '''Cria os paths do projeto'''
    def __init__(self):
        print('> Create path\'s')
        self._path = os.getcwd()
        self._path_data = os.path.join(self.path, config.paths['data'])
        self._path_bbox = os.path.join(self.path, config.paths['bbox'])
        self._path_db = os.path.join(self.path, config.paths['database'])
        self._path_db_train = os.path.join(self.path_db, config.paths['train'])
        self._path_db_valid = os.path.join(self.path_db, config.paths['valid'])
        self._path_db_test = os.path.join(self.path_db, config.paths['test'])

        print('> Create DataFrame\'s: [train, valid]')
        data = pd.Series(os.listdir(self.path_data))
        sample = np.random.choice(
            a=data.index,
            size=int(len(data)*config.param['train']),
            replace=False)
        self._df_train, self._df_valid = data.ix[sample], data.drop(sample)

        self._create_dir()

    @property
    def path(self):
        return self._path

    @property
    def path_data(self):
        return self._path_data

    @property
    def path_bbox(self):
        return self._path_bbox

    @property
    def path_db(self):
        return self._path_db

    @property
    def path_db_train(self):
        return self._path_db_train

    @property
    def path_db_valid(self):
        return self._path_db_valid

    @property
    def path_db_test(self):
        return self._path_db_test

    @property
    def df_train(self):
        return self._df_train

    @property
    def df_valid(self):
        return self._df_valid


    # Cria o diretório do projeto
    def _create_dir(self):
        '''Cria o diretório do projeto'''
        if not os.path.exists(self.path_db):
            print('> Create directory')
            os.mkdir(self.path_db)
            os.mkdir(self.path_db_train)
            os.mkdir(self.path_db_valid)
            os.mkdir(self.path_db_test)


# Cria um arquivo txt (path) ou adiciona linhas
def _create_txt(line, path):
    '''Cria um arquivo txt (path) ou adiciona linhas em um arquivo'''
    if not os.path.exists(path):
        with open(path, 'w+') as arq:
            arq.write(line)
    else:
        with open(path, 'a+') as arq:
            arq.write('\n' + line)


# TODO: Definir
def _read_xml(path_src, path_dst):
    '''Definir'''
    dict_class = config.classes
    tree = ET.parse(path_src)
    root = tree.getroot()

    for member in root.findall('object'):
        bndbox = member.find('bndbox')
        filename = root.find('filename').text.replace(' ', '_')
        tp_class = member.find("name").text
        size = (
            int(root.find('size')[0].text),
            int(root.find('size')[1].text)
        )

        box = (
            int(bndbox.find('xmin').text),  # xmin
            int(bndbox.find('ymin').text),  # ymin
            int(bndbox.find('xmax').text),  # xmax
            int(bndbox.find('ymax').text)  # ymax
        )

        xml_str = _convert(dict_class[tp_class], size, box)
        _create_txt(line=xml_str, path=os.path.join(path_dst, filename + '.txt'))


# TODO: Definir
def _convert(c, size, box):
    '''Converte o bbox em anotações para treinamento'''
    dw = 1. / size[0]
    dh = 1. / size[1]

    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]

    x, y = round(x * dw, 6), round(y * dh, 6)
    w, h = round(w * dw, 6), round(h * dh, 6)

    return str(c) + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)


# TODO: Definir
def divide_dataset():
    # Instance of the object
    obj = _PathsAndLists()


    # Train
    _dir_arq = os.path.join(obj.path_db_train, config.paths['train'] + '.txt')
    print('> Create file: ', _dir_arq)
    for arq in obj.df_train:
        src_data = os.path.join(obj.path_data, arq)
        src_bbox = os.path.join(obj.path_bbox, arq.replace('.jpg', '.xml'))
        dst = os.path.join(obj.path_db_train, arq)

        print('> Copy files: ', src_data, ' =>', dst)
        copyfile(src_data, dst)

        print('> Create XML files:', arq)
        _create_txt(line=arq, path=_dir_arq)
        _read_xml(path_src=src_bbox, path_dst=obj.path_db_train)
    
    # Valid
    _dir_arq = os.path.join(obj.path_db_valid, config.paths['valid'] + '.txt')
    print('> Create file: ', _dir_arq)
    for arq in obj.df_valid:
        src_data = os.path.join(obj.path_data, arq)
        src_bbox = os.path.join(obj.path_bbox, arq.replace('.jpg', '.xml'))
        dst = os.path.join(obj.path_db_valid, arq)

        print('> Copy files: ', src_data, ' =>', dst)
        copyfile(src_data, dst)

        print('> Create XML files:', arq)
        _create_txt(line=arq, path=_dir_arq)
        _read_xml(path_src=src_bbox, path_dst=obj.path_db_valid)