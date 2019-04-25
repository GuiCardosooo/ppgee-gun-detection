"""

Tools Library
-------------------------------------------------------------------------------

UFES - Universidade Federal do Espírito Santo

-------------------------------------------------------------------------------
Full documentation is at <https://github.com/GuiCardosooo/ppgee-gun-detection>.

"""

import io
import os
import sys
import zipfile
import requests
import xml.etree.ElementTree as ET
from glob import glob

class Tools(object):
  '''Classe com algumas funções essenciais no pré processamento dos dados'''

  # TODO: Definir o método aqui
  def get_url_zip(self, url, new_dir=None):
    '''Função responsável por baixar um arquivo .zip de uma url'''

    try:
      print('Downloading zip file... :)')
      r = requests.get(url)
      z = zipfile.ZipFile(io.BytesIO(r.content))

      if new_dir is None:
        z.extractall()
      else:
        zinfos = z.infolist()
        old_dir = zinfos[0].filename
        z.extractall()
        os.rename(old_dir[:-1], new_dir)
        
      print('Done!')
      return True

    except:
      print('Oops!', sys.exc_info()[0], 'occured.')
      return False


  # TODO: Definir o método aqui
  def xml_to_csv(self, path_data, path_bbox):
    '''Gera a anotação de uma imagem a partir de uma marcação'''

    # TODO: Validar dados aqui
    dict_class = self._get_dict_class()

    for xml_file in glob(path_bbox + '/*.xml'):
      tree = ET.parse(xml_file)
      root = tree.getroot()

      for member in root.findall('object'):
        bndbox = member.find('bndbox')
        filename = root.find('filename').text
        tp_class = member.find("name").text
        size = (
          int(root.find('size')[0].text),
          int(root.find('size')[1].text)
        )

        box = (
          int(bndbox.find('xmin').text), # xmin
          int(bndbox.find('ymin').text), # ymin
          int(bndbox.find('xmax').text), # xmax
          int(bndbox.find('ymax').text)  # ymax
        )

        xml_str = self._convert(dict_class[tp_class], size, box, out_str=True)
        self._create_text_file(xml_str, path_data, filename)


  # TODO: Definir o método aqui
  def _convert(self, c, size, box, out_str=None):
    '''Converte o bbox em anotações para treinamento'''
    dw = 1. / size[0]
    dh = 1. / size[1]
    
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]

    x, y = round(x * dw, 6), round(y * dh, 6)
    w, h = round(w * dw, 6), round(h * dh, 6)

    # Define a saída
    if out_str:
      return str(c) + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h)
    else:
      return (c, x, y, w, h)


  # TODO: Definir o método aqui
  def _get_dict_class(self):
    try:
      arq = open('./config/config-class.txt', 'r')
      out_dict = {}

      for i, lin in enumerate(arq):
        if i != 0:
          out_dict[lin.replace('\n', '')] = i - 1

      return out_dict
        
    except:
      print('Ops!', sys.exc_info()[0], 'occured.')
      return False


  # TODO: Definir o método aqui
  def _create_text_file(self, str_truncada, path, filename):
    '''Cria um arquivo de texto baseado em uma string'''

    diretorio = os.path.join(os.getcwd(), path, filename) + '.txt'
    
    if not os.path.exists(diretorio):
      with open(diretorio, 'w+') as out_arq:
        out_arq.write(str_truncada)
    else:
      with open(diretorio, 'a+') as out_arq:
        out_arq.write('\n' + str_truncada)


  # TODO: Definir o método aqui
  def hello_world(self):
    print('Hello world')