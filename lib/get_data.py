# -*- coding: utf-8 -*-
# UFES - Universidade Federal do Espiríto Santo
# Gun Detection
# Written by Guilherme Cardoso
"""
Full documentation is at:
<https://github.com/GuiCardosooo/ppgee-gun-detection>.
"""


import io
import os
import sys
import requests
import zipfile
import warnings


__all__ = ['get_url_zip']
__author__ = ('Guilherme Vinícius Simões Cardoso <cardoso.guivi@gmail.com>')


# TODO: Definir a classe aqui
class _CreatePaths:
    ''''''
    # Constructor
    def __init__(self, base_path=None):
        self._len_data = None
        self._base_path = os.getcwd()
        if base_path is not None:
            self._base_path = base_path


    # Get's and Setter's
    @property
    def base_path(self):
        return self._base_path


    @base_path.setter
    def base_path(self, value):
        self._base_path = value


    @property
    def len_data(self):
        return self._len_data


    @len_data.setter
    def len_data(self, value):
        self._len_data = value


# Retorna o tamanho de um diretório EXISTENTE
def _get_len_dir(path):
    return len(os.listdir(path))


# Renomeia um diretório
def _rename_dir(old_dir, new_dir):
    try:
        print('> Renaming directory')
        os.rename(old_dir, new_dir)
        _delete_spaces(new_dir)
        return True
    except:
        return False


# Verifica se existe espaços no nome destino
def _delete_spaces(new_dir):
    path = os.path.join(os.getcwd(), new_dir)
    for line in os.listdir(path):
        if line.find(' ') >= 0:
            print('> Search for spaces')
            old = os.path.join(path, line)
            new = os.path.join(path, line.replace(' ', '_'))
            os.rename(old, new)


# Faz a download do dataset
def get_url_zip(url, new_dir):
    '''Função responsável por baixar um arquivo .zip de uma url'''

    obj = _CreatePaths()
    if os.path.exists(os.path.join(obj.base_path, new_dir)):
        obj.len_data = _get_len_dir(new_dir)
        warnings.warn('Este diretório já existe!')
        return True

    try:
        print('> Downloading zip file:\n>', url)
        r = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        old_dir = z.infolist()[0].filename[:-1]
        z.extractall()
    except:
        print('Oops!', sys.exc_info()[0], 'occured.')
        return False

    if _rename_dir(old_dir, new_dir):
        print('Done!')
        return True
    else:
        return False