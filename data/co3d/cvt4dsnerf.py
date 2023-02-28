import argparse
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


def parse():

    p = argparse.ArgumentParser()
    p.add_argument('--depth', default='teddy_depth.png')
    p.add_argument('--image', default='teddy_img.png')
    return p.parse_args()


if __name__ == "__main__":

    args = parse()

    # BDS
    bds = np.array([1.0, 6.0]).astype('float32')
    np.save("bds.npy", bds)

    # IMAGE
    im = Image.open(args.image)
    assert im.mode == 'RGBA'
    im = np.array(im)
    rgb = im[..., :3] / 255
    alpha = im[..., 3:] / 255
    rgb = rgb * alpha + (1 - alpha) * np.ones_like(rgb)
    rgb = rgb[None, ...].astype('float32')
    # print(rgb.shape, rgb.min(), rgb.max(), rgb.dtype)
    np.save("train_images.npy", rgb)
    np.save("test_images.npy", rgb)

    # POSE
    pose = np.array([
        [1, 0, 0, 0, 384],
        [0, 1, 0, 0, 384],
        [0, 0, 1, 3, 332],
    ]).astype('float32')
    pose = pose[None, ...]
    np.save("test_poses.npy", pose)
    np.save("train_poses.npy", pose)
    np.save("video_poses.npy", pose)

    # DEPTH
    depth = Image.open(args.depth).convert('L')
    depth = np.array(depth) / 255 * 6
    y, x = np.where(depth != 0)
    # x = 384 - x
    
    coord = np.column_stack([x, y]).astype('float32')

    d_sparse = []
    for x, y in coord:
        d = depth[int(y)][int(x)]
        d_sparse.append(d)

    d_sparse = np.array(d_sparse).astype('float32')
    error = np.ones_like(d_sparse)

    depth_info = np.array([{
        "coord": coord,
        "depth": d_sparse,
        "error": error,
    }])

    # assert im.mode == 'RGBA'
    np.save("train_depths.npy", depth_info, allow_pickle=True)

    # mat = np.array([
    #     [
    #         9.9561214e-01, -2.0686002e-02, -9.1260545e-02, -2.9630968e-01,
    #         7.5600000e+02
    #     ],
    #     [
    #         2.5019741e-02, 9.9860018e-01, 4.6601858e-02, 1.2991698e-01,
    #         1.0080000e+03
    #     ],
    #     [
    #         9.0168789e-02, -4.8680693e-02, 9.9473602e-01, 3.7948530e-02,
    #         8.2989215e+02
    #     ],
    # ])
    # print((mat * 100).astype('int'))
    #
