# coding=utf-8
__author__ = 'modoso'

import os
from PIL import Image
from numpy import *

IMAGE_PATH = os.path.abspath('../../../resources/images')
THUMB_PATH = os.path.abspath('../../../resources/thumbs')


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


def imagePath(imageName):
    return os.path.join(IMAGE_PATH, imageName)


def thumbPath(imageName):
    return os.path.join(THUMB_PATH, imageName)


def imresize(im, sz):
    pil_im = Image.fromarray(im)
    return array(pil_im.resize(sz))


def histeq(a, im, nbr_bins=256):
    imhist, bins = histogram(a, nbr_bins, normed=True)
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf[-1]
    im2 = interp(a, bins[:-1], cdf)
    return im2.reshape(im.shape), cdf


def compute_average(imlist):
    averageim = array(Image.open(imlist[0], 'f'))

    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print imname + '... skipped'
    averageim /= len(imlist)

    return array(averageim, 'uint8')


# X is a matrix
#图像主成分分析
def pca(X):
    num_data, dim = X.shape

    # decentrialized
    mean_X = X.mean(axis=0)
    X = X - mean_X

    if dim > num_data:
        # 协方差
        M = dot(X, X.T)
        # 特征值和特征向量
        e, EV = linalg.eigh(M)
        tmp = dot(X.T, EV).T
        V = tmp[::-1]
        S = sqrt(e)[::-1]
        for i in range(V.shape[1]):
            V[:, i] /= S
    else:
        U, S, V = linalg.svd(X)
        V = V[:num_data]

    # 返回投影矩阵，方差和均值
    return V, S, mean_X


