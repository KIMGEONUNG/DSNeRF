#!/usr/bin/env python

import numpy as np
from scipy.spatial.transform import Rotation as R

example = [
    [1., 0., 0., 0., 384.],
    [0., 1., 0., 0., 384.],
    [0., 0., 1., 3., 332.],
]

path = 'video_poses.npy'
num = 120
radius = 3
pi = 2 * np.pi / 1
frames = []
size = 384
focal = 332
for i in range(num):

    mat = np.zeros((3, 5))
    mat[0, 4] = size
    mat[1, 4] = size
    mat[2, 4] = focal

    radian = pi / num * i
    tx = radius * np.sin(radian)
    ty = 0
    tz = radius * np.cos(radian)

    # radian = 0
    r = R.from_euler('y', radian, degrees=False).as_matrix()

    # print(f"x:{tx}, y:{ty}, z:{tz}, r:{radian}")

    # tx = 1 / num * i
    # ty = 1 / num * i
    # tz = 1 / num * i

    mat[:3, :3] = r
    mat[0, 3] = tx
    mat[1, 3] = ty
    mat[2, 3] = tz
    # print(mat)

    frames.append(mat[None, ...])

frames = np.row_stack(frames)
np.save(path, frames)
