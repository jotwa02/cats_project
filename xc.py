import tqdm
import random
import pathlib
import itertools
import collections
import os
import cv2
import numpy as np
import remotezip as rz
import tensorflow as tf

"""# Some modules to display an animation using imageio.
import imageio
from IPython import display
from urllib import request
from tensorflow_docs.vis import embed"""

URL = 'https://storage.googleapis.com/catsvideos/cats.zip'


def list_files_from_zip_url(zip_url):
    files = []
    with rz.RemoteZip(zip_url) as zip:
        for zip_info in zip.infolist():
            files.append(zip_info.filename)
    return files


files = list_files_from_zip_url(URL)
files = [f for f in files if f.endswith('.mp4')]


def get_class(fname):
    return fname.split('_')[-1]


def get_files_per_class(files):
    files_for_class = collections.defaultdict(list)
    for fname in files:
        class_name = get_class(fname)
        files_for_class[class_name].append(fname)
    return files_for_class


files_for_class = get_files_per_class(files)
classes = list(files_for_class.keys())
print('Num classes:', len(classes))
print('Num videos for class[0]:', len(files_for_class[classes[0]]))
print('Num videos for class[0]:', len(files_for_class[classes[1]]))
print('Num videos for class[0]:', len(files_for_class[classes[2]]))
print('Num videos for class[0]:', len(files_for_class[classes[6]]))