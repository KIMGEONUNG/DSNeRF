import numpy as np
from PIL import Image
from pathlib import Path

files = [
    "bds.npy",
    "train_images.npy",
    "test_images.npy",
    "test_poses.npy",
    "train_poses.npy",
    "video_poses.npy",
    "train_depths.npy",
]

# BDS
if False:
    bsd = np.load("bds.npy")
    print(bsd.dtype)

# IMGES
if False:
    img = np.load("train_images.npy")
    print(img.shape, img.min(), img.max(), img.dtype)
    exit()
    img = (img[0] * 255).astype('uint8')
    im = Image.fromarray(img)
    im.show()
    # print(img.shape)
    # np.save("my/train_images.npy", img)
    exit()

# POSES
if False:
    p1 = np.load("test_poses.npy")
    p2 = np.load("train_poses.npy")
    p3 = np.load("video_poses.npy")
    print((p1[1]* 100).astype('int'))
    print(p1.shape, p1.dtype)
    print(p2.shape, p2.dtype)
    print(p3.shape, p3.dtype)

# DEPTH
if False:
    img = np.load("train_images.npy")[0]
    depth_map = np.zeros_like(img[...,0])
    depth_info = np.load("train_depths.npy", allow_pickle=True)[0]

    d = depth_info['depth']
    c = depth_info['coord']
    e = depth_info['error']
    c = c.astype('int')

    for i, (x,y) in enumerate(c):
        depth_map[y, x] = d[i]

    depth_map /= 6

    
    depth = Image.fromarray((depth_map * 255).astype('uint8'))
    img = Image.fromarray((img * 255).astype('uint8'))
    img.show()
    depth.show()

# DEPTH
if True:
    img = np.load("train_images.npy")[0]
    depth_map = np.zeros_like(img[...,0])
    depth_info = np.load("train_depths.npy", allow_pickle=True)[0]

    d = depth_info['depth']
    c = depth_info['coord']
    e = depth_info['error']

    print(d.shape)
    print(c.shape)
    print(e.shape)
    exit()

    c = c.astype('int')

    for i, (x,y) in enumerate(c):
        depth_map[y, x] = d[i]


    c = c.astype('int')

    for i, (x,y) in enumerate(c):
        depth_map[y, x] = d[i]

    depth_map /= 6

    
    depth = Image.fromarray((depth_map * 255).astype('uint8'))
    img = Image.fromarray((img * 255).astype('uint8'))
    img.show()
    depth.show()
