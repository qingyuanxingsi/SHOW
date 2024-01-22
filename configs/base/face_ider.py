import os 
from global_config import FACE_MAIN_DIR

ider_cfg=dict(
    type='arcface_ider',
    threshold=0.40,
    npy_folder_name='arcface',
    weight=os.path.join(FACE_MAIN_DIR, 'models/arcface/glink360k_cosface_r100_fp16_0.1.pth'),
    name='r100',fp16=True,det='mtcnn',
)