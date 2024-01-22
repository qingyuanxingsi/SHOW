# usually, "{{ fileDirname }}/../../" comes to be the code root

import os
from global_config import SHOW_MAIN_DIR

if 0:
    smplx_model_path='{{ fileDirname }}/models/smplx/2019/SMPLX_MALE.npz'
    betas_ver_temp='{{ fileDirname }}/data/id_pic/betas_shape2019male_exp2019/{}.npy'
elif 0:
    smplx_model_path='{{ fileDirname }}/models/smplx/SMPLX_NEUTRAL_2020_org.npz'
    betas_ver_temp='{{ fileDirname }}/data/id_pic/betas_shape2020natrual_exp2020/{}.npy'
elif 1:
    smplx_model_path=f'{SHOW_MAIN_DIR}/models/smplx/SMPLX_MALE_shape2019_exp2020.npz'
    betas_ver_temp=f'{SHOW_MAIN_DIR}/data/id_pic/SMPLX_MALE_shape2019_exp2020/'+'{}.npy'
    

# smplx_model_path='{{ fileDirname }}/../../../models/smplx/SMPLX_MALE_shape2019_exp2020.npz'
# betas_ver_temp='{{ fileDirname }}/../../../data/id_pic/betas_2019_male/{}.npy'

part_segm_fn= f'{SHOW_MAIN_DIR}/data/smplx_parts_segm.pkl'
vposer_ckpt=f'{SHOW_MAIN_DIR}/models/vposer_v1_0'
assets_root=f'{SHOW_MAIN_DIR}/data'


smplx_cfg=dict(
    # model_path='{{ fileDirname }}/../../../models'
    # model_type= 'smplx',
    # gender= 'neutral',
    
    model_path = smplx_model_path,
    flat_hand_mean= False,
    use_face_contour= True,
    use_pca= True,
    use_hands= True,
    use_face= True,
    
    num_betas= 300,
    num_pca_comps= 12,
    num_expression_coeffs= 100,
)
