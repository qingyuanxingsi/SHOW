import os 

flame_dir = os.environ['SHOW_DIR']

flame_cfg=dict(
    flame_geom_path = f'{flame_dir}/data/generic_model.pkl',
    flame_template_path = f'{flame_dir}/data/uv_template.obj',
    flame_static_lmk_path = f'{flame_dir}/data/flame_static_embedding_68_v4.npz',
    flame_dynamic_lmk_path = f'{flame_dir}/data/flame_dynamic_embedding.npy',
    tex_space_path = f'{flame_dir}/data/FLAME_albedo_from_BFM.npz',
    num_shape_params = 300,
    num_exp_params = 50,
    tex_params = 150,
    image_size = [512, 512],
)