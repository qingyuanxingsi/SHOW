import os 

show_dir = os.environ['SHOW_DIR']
ider_cfg=dict(
    type='arcface_ider',
    threshold=0.40,
    npy_folder_name='arcface',
    weight=os.path.join(show_dir, 'models/arcface/glink360k_cosface_r100_fp16_0.1.pth'),
    name='r100',fp16=True,det='mtcnn',
)