from os.path import basename, getmtime, getsize
from hashlib import sha256
from binascii import crc32
from os.path import normpath, isdir, isfile, join, abspath, split
from os import listdir, makedirs, rename
import datetime
from shutil import move
from PySide.QtGui import *
from PySide.QtCore import *
from os.path import isdir, expanduser
import os
import sys
import zipfile

# -- DEFINE READ FILE  ----
DEF_VERSION = "Version : 3.8"
DEF_DATE_EDIT = "Last Edit :31/05/2017"


# -- DEFINE READ FILE  ----

DEF_FILE_NAME = 0
DEF_FILE_PATH = 1
DEF_FILE_CRC =  2
DEF_FILE_SIZE = 3
DEF_FILE_DATE = 4


# -- DEFINE LISTA DATI  ----

DEF_paths_to_scan      = 0
DEF_path_dest          = 1
DEF_tollerance_active  = 2
DEF_tollerance         = 3
DEF_samename           = 4
DEF_checksum_active    = 5
DEF_checksum_type      = 6
DEF_what_to_keep       = 7
