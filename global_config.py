# -*- coding: utf-8 -*-

import os

candidates = [
    '/mnt/chongqinggeminiceph1fs/geminicephfs/security-others-common',
    '/mnt/cephfs'
]
main_dir = ''
for cand in candidates:
    if os.path.exists(cand):
        main_dir = cand
        break
SHOW_MAIN_DIR = f'{main_dir}/doodleliang/SHOW'
EXTRA_MAIN_DIR = SHOW_MAIN_DIR
FACE_MAIN_DIR = SHOW_MAIN_DIR