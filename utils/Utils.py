import io
import os
import sys
import glob
import pandas as pd
import zipfile
import requests
import xml.etree.ElementTree as ET

class Tools(object):
  
  def get_url_zip(self, url, new_dir=None):
    '''
    Função responsável por baixar um arquivo .zip de uma url
    
    Param:
      url - (obr) string
      new_dir - (opc) string

    Return:
      True - Caso a url seja válida e se arquivo foi descompactado
      False - Caso ocorra um erro na url ou na descompactação
    '''

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

  def xml_to_csv(self, path, name_new_dir=None):
    '''
    Converte um path de arquivos ".xml" em uma lista em ".csv" (separado por vírgulas)
    
    Param:
      path - (obr) string
      name_new_dir - (opc) string

    Return:
      True - CONSTRUÇÃO
      False - CONSTRUÇÃO
    '''
    xml_list = []
    
    for xml_file in glob.glob(path + '/*.xml'):
      tree = ET.parse(xml_file)
      root = tree.getroot()

      for member in root.findall('object'):
        bndbox = member.find("bndbox")
        value = (root.find('filename').text,
          int(root.find('size')[0].text),
          int(root.find('size')[1].text),
          member.find("name").text,
          int(bndbox.find("xmin").text),
          int(bndbox.find("ymin").text),
          int(bndbox.find("xmax").text),
          int(bndbox.find("ymax").text)
          )
        xml_list.append(value)

    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)

    output_dir = os.path.join(os.getcwd(), 'data')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    xml_df.to_csv('data/labels.csv', index=None)
    print('Convertido com sucesso:', output_dir)

    return xml_df