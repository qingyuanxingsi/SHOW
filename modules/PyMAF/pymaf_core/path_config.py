import os

MAIN_DIR = os.environ['main_dir']
JOINT_REGRESSOR_TRAIN_EXTRA = f'{MAIN_DIR}/data/J_regressor_extra.npy'
JOINT_REGRESSOR_H36M = f'{MAIN_DIR}/data/J_regressor_h36m.npy'
SMPL_MEAN_PARAMS = f'{MAIN_DIR}/data/smpl_mean_params.npz'
SMPL_MODEL_DIR = f'{MAIN_DIR}/models/pymaf_data/smpl'
PYMAF_DATA_DIR = f'{MAIN_DIR}/models/pymaf_data'
