from easydict import EasyDict as edict
import json

config = edict()
config.TRAIN = edict()
config.TEST = edict()

## Adam
config.TRAIN.batch_size = 8 
config.TRAIN.batch_size_init = 16
config.TRAIN.lr_init = 1e-4
config.TRAIN.beta1 = 0.9

# learning rate
config.TRAIN.n_epoch = 10000
config.TRAIN.n_epoch_init = 100
config.TRAIN.lr_decay = 0.8
config.TRAIN.decay_every = 200

## total_variation
config.TRAIN.lambda_tv = 1e-7

## train set location
# config.TRAIN.synthetic_img_path = '/data1/junyonglee/blur_sharp_only/image_dof/'
# config.TRAIN.defocus_map_path = '/data1/junyonglee/blur_sharp_only/defocus_map/'
# config.TRAIN.synthetic_binary_map_path = '/data1/junyonglee/blur_sharp_only/binary_map/'

config.TRAIN.synthetic_img_path = '/data1/synthetic_datasets/out/image/'
config.TRAIN.defocus_map_path = '/data1/synthetic_datasets/out/blur_map/'
config.TRAIN.defocus_map_norm_path = '/data1/synthetic_datasets/out/blur_map_norm/'
config.TRAIN.synthetic_binary_map_path = '/data1/synthetic_datasets/out/blur_map_binary/'

config.TRAIN.real_img_path = '/data1/junyonglee/BlurDetection/train/image/'
config.TRAIN.real_binary_map_path = '/data1/junyonglee/BlurDetection/train/gt/'

## test set location
config.TEST.real_img_path = '/data1/junyonglee/BlurDetection/test/image/'
config.TEST.real_binary_map_path = '/data1/junyonglee/BlurDetection/test/gt/'

## train image size
config.TRAIN.height = 240
config.TRAIN.width = 240

## log & checkpoint & samples
# every global step
config.TRAIN.write_log_every = 20
config.TRAIN.write_ckpt_every = 300
config.TRAIN.write_sample_every = 1000
# every epoch
config.TRAIN.refresh_image_log_every = 50

# save dir
config.TRAIN.root_dir = '/data2/junyonglee/sharpness_assessment/'

def log_config(path, cfg):
    with open(path + '/config.txt', 'w') as f:
        f.write('================================================\n')
        f.write(json.dumps(cfg, indent=4))
        f.write('\n================================================\n')
