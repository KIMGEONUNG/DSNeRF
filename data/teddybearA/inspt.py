#!/usr/bin/env python
from PIL import Image
import numpy as np

# x1 = np.load('train_depths.npy', allow_pickle=True)
x1 = np.load('train_depths.npy', allow_pickle=True)[0]
coords = x1["coord"]
depths = x1["depth"]

print(coords.shape)
print(depths.shape)
x = np.zeros((384, 384))

for i, (a, b) in enumerate(coords):
    a, b = int(a), int(b)
    x[b, a] = depths[i]

x = (x / 6 * 255).astype('uint8')

im = Image.fromarray(x)
im.show()
