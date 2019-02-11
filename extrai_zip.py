# coding: utf-8

import os
import zipfile
import sys


def main(path):
    if not os.path.exists(path):
        print('Arquivo {} não existe'.format(path))
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print('Arquivos extraídos')


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("""\
USO: python3 extrai_zip.py dados.zip
""")
        sys.exit(-1)
    main(sys.argv[1])
