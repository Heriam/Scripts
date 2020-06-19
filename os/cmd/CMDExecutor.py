# coding=UTF-8
import sys
import inspect
import os
import shutil
import CMDUtils as cutil
from osgeo import gdal

WORK_DIR = 'C:\\Users\\Public\\Desktop\\OSGeo4W\\'
OGRMERGE = 'python C:\ProgramData\Anaconda3\envs\Scripts\Lib\site-packages\GDAL-3.0.2-py3.7-win-amd64.egg-info\scripts\ogrmerge.py '
SHFORMAT = '-f "ESRI Shapefile" '
SRC_DIR = 'source'
DST_DIR = 'target'
MRG_DIR = 'merged'
SLASH = '/'
BLANK = ' '
LCO = '-lco '
OUT = '-o '
UTF_8 = 'encoding=UTF-8 '
UPDATE = '-update '
APPEND = '-append '
SINGLE = '-single '
LAYERLIST = ['AANP','AGNP','HYDA','HYDL','HYDP','LRDL','LRRL','RESA','RESP', 'BOUL', 'BOUP', 'BOUA']


def convert():
    os.chdir(WORK_DIR)
    src_list = os.listdir(SRC_DIR)
    if not os.path.exists(DST_DIR):
        os.mkdir(DST_DIR)
    for src_file in src_list:
        id = src_file.split('.')[0]
        if not (src_file.endswith('.gdb')):
            continue
        cmd = OGRMERGE + OUT + DST_DIR + SLASH + id + BLANK + SRC_DIR + SLASH + src_file + BLANK + SHFORMAT + LCO + UTF_8
        print(cmd)
        os.system(cmd)


def move():
    os.chdir(WORK_DIR)
    dst_list = os.listdir(DST_DIR)
    for block_dir in dst_list:
        file_list = os.listdir(DST_DIR + SLASH + block_dir)
        for layer in LAYERLIST:
            os.mkdir(DST_DIR + SLASH + block_dir + SLASH + layer)
            for layer_file in file_list:
                if layer in layer_file:
                    shutil.move(DST_DIR + SLASH + block_dir + SLASH + layer_file, DST_DIR + SLASH + block_dir + SLASH + layer)
            if len(os.listdir(DST_DIR + SLASH + block_dir + SLASH + layer)) == 0:
                shutil.rmtree(DST_DIR + SLASH + block_dir + SLASH + layer)


def merge():
    os.chdir(WORK_DIR)
    dst_list = os.listdir(DST_DIR)
    if not os.path.exists(MRG_DIR):
        os.mkdir(MRG_DIR)
    for layer in LAYERLIST:
        layer_file_list = []
        for block_dir in dst_list:
            if os.path.isdir(DST_DIR + SLASH + block_dir + SLASH + layer):
                layer_file_list.append(DST_DIR + SLASH + block_dir + SLASH + layer)
        layer_file_list_str = ' '.join(layer_file_list)
        print(layer_file_list_str)
        cmd = OGRMERGE + SINGLE + OUT + MRG_DIR + SLASH + layer + '.shp' + BLANK + layer_file_list_str + BLANK + LCO + UTF_8
        os.system(cmd)


def clear():
    os.chdir(WORK_DIR)
    shutil.rmtree(DST_DIR)
    shutil.rmtree(MRG_DIR)


if __name__ == '__main__':
    merge()