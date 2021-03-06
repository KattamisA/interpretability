import torch
import torch.nn as nn
import torchvision
import sys
import os

import numpy as np
from PIL import Image
import PIL
import numpy as np

import matplotlib.pyplot as plt

def crop_image(img, d=32):
    '''Make dimensions divisible by `d`'''

    new_size = (img.size[0] - img.size[0] % d, 
                img.size[1] - img.size[1] % d)

    bbox = [
            int((img.size[0] - new_size[0])/2), 
            int((img.size[1] - new_size[1])/2),
            int((img.size[0] + new_size[0])/2),
            int((img.size[1] + new_size[1])/2),
    ]

    img_cropped = img.crop(bbox)
    return img_cropped

def get_params(opt_over, net, net_input, downsampler=None):
    '''Returns parameters that we want to optimize over.

    Args:
        opt_over: comma separated list, e.g. "net,input" or "net"
        net: network
        net_input: torch.Tensor that stores input `z`
    '''
    opt_over_list = opt_over.split(',')
    params = []
    
    for opt in opt_over_list:
    
        if opt == 'net':
            params += [x for x in net.parameters() ]
        elif  opt=='down':
            assert downsampler is not None
            params = [x for x in downsampler.parameters()]
        elif opt == 'input':
            net_input.requires_grad = True
            params += [net_input]
        else:
            assert False, 'what is it?'
            
    return params

#def load(path):
#    """Load PIL image."""
#    img = Image.open(path)
#    return img

#def get_image(path, imsize=-1):
#    """Load an image and resize to a cpecific size. 
#
#    Args: 
#        path: path to image
#        imsize: tuple or scalar with dimensions; -1 for `no resize`
#    """
#    img = load(path)
#
#    if isinstance(imsize, int):
#        imsize = (imsize, imsize)
#
#    if imsize[0]!= -1 and img.size != imsize:
#        if imsize[0] > img.size[0]:
#            img = img.resize(imsize, Image.BICUBIC)
#        else:
#            img = img.resize(imsize, Image.ANTIALIAS)
#
#    img_np = pil_to_np(img)
#
#    return img, img_np



def fill_noise(x, noise_type):
    """Fills tensor `x` with noise of type `noise_type`."""
    if noise_type == 'u':
        x.uniform_()
    elif noise_type == 'n':
        x.normal_() 
    else:
        assert False

def get_noise(input_depth, method, spatial_size, noise_type='u', var=1./10):
    """Returns a pytorch.Tensor of size (1 x `input_depth` x `spatial_size[0]` x `spatial_size[1]`) 
    initialized in a specific way.
    Args:
        input_depth: number of channels in the tensor
        method: `noise` for fillting tensor with noise; `meshgrid` for np.meshgrid
        spatial_size: spatial size of the tensor to initialize
        noise_type: 'u' for uniform; 'n' for normal
        var: a factor, a noise will be multiplicated by. Basically it is standard deviation scaler. 
    """
    if isinstance(spatial_size, int):
        spatial_size = (spatial_size, spatial_size)
    if method == 'noise':
        shape = [1, input_depth, spatial_size[0], spatial_size[1]]
        net_input = torch.zeros(shape)
        
        fill_noise(net_input, noise_type)
        net_input *= var            
    elif method == 'meshgrid': 
        assert input_depth == 2
        X, Y = np.meshgrid(np.arange(0, spatial_size[1])/float(spatial_size[1]-1), np.arange(0, spatial_size[0])/float(spatial_size[0]-1))
        meshgrid = np.concatenate([X[None,:], Y[None,:]])
        net_input=  np_to_torch(meshgrid)
    else:
        assert False
        
    return net_input

def pil_to_np(img_PIL):
    '''Converts image in PIL format to np.array.
    
    From W x H x C [0...255] to C x W x H [0..1]
    '''
    ar = np.array(img_PIL)

    if len(ar.shape) == 3:
        ar = ar.transpose(2,0,1)
    else:
        ar = ar[None, ...]

    return ar.astype(np.float32) / 255.

def np_to_pil(img_np): 
    '''Converts image in np.array format to PIL image.
    
    From C x W x H [0..1] to  W x H x C [0...255]
    '''
    ar = np.clip(img_np*255,0,255).astype(np.uint8)
    
    if img_np.shape[0] == 1:
        ar = ar[0]
    else:
        ar = ar.transpose(1, 2, 0)

    return Image.fromarray(ar)

def np_to_torch(img_np):
    '''Converts image in numpy.array to torch.Tensor.

    From C x W x H [0..1] to  C x W x H [0..1]
    '''
    return torch.from_numpy(img_np)[None, :]

def torch_to_np(img_var):
    '''Converts an image in torch.Tensor format to np.array.

    From 1 x C x W x H [0..1] to  C x W x H [0..1]
    '''
    return img_var.detach().cpu().numpy()[0]


def optimize(glparam, optimizer_type, parameters, closure, LR, num_iter):
    """Runs optimization loop.

    Args:
        optimizer_type: 'LBFGS' or 'adam'
        parameters: list of Tensors to optimize over
        closure: function, that returns loss variable
        LR: learning rate
        num_iter: number of iterations 
    """
    if optimizer_type == 'LBFGS':
        # Do several steps with adam first
        optimizer = torch.optim.Adam(parameters, lr=0.001)
        for j in range(100):
            optimizer.zero_grad()
            closure(j)
            optimizer.step()

        print('Starting optimization with LBFGS')        
        def closure2():
            optimizer.zero_grad()
            return closure()
        optimizer = torch.optim.LBFGS(parameters, max_iter=num_iter, lr=LR, tolerance_grad=-1, tolerance_change=-1)
        optimizer.step(closure2)

    elif optimizer_type == 'adam':
        print('Starting optimization with ADAM')
        optimizer = torch.optim.Adam(parameters, lr=LR)
        
        for j in range(num_iter):
            optimizer.zero_grad()
            closure(j)
            optimizer.step()
    else:
        assert False

def save_net_details(save_path, arch, param_number, pad, opt_over, optimizer,
                     input_depth, loss_fn = 'Mean Squared Error', LR = 0.01, num_iter = 1000, exp_weight = 0.99,
                     reg_noise_std = 1.0/30, INPUT = 'noise', name = None, net = None):
    
    if name == None:
        name = "No input name given"
    if net == None:
        net = "No net given"
    f = open("{}/Details.txt".format(save_path),"w+")
    
    f.write("\n{:<60}{:<12}".format('Image run through the deep image prior:   ',name))
    f.write("\n\n{:<60}{:<12}".format('Architecture:   ',arch))
    f.write("\n{:<60}{:<12}".format('Number of parameters:   ',param_number))
    f.write("\n{:<60}{:<12}".format('Input depth/feature maps:   ',input_depth))
    f.write("\n{:<60}{:<12}".format('Padding:   ',pad))
    f.write("\n\n{:<60}{:<12}".format('Optimize over:   ',opt_over))
    f.write("\n{:<60}{:<12}".format('Optimizer:   ',optimizer))
    f.write("\n\n{:<60}{:<12}".format('Learning rate:   ',LR))
    f.write("\n{:<60}{:<12}".format('Number of iterations:   ',num_iter))
    f.write("\n\n{:<60}{:<12}".format('Loss function:   ',loss_fn))
    f.write("\n\n{:<60}{:<12}".format('Input:   ',INPUT))
    f.write("\n{:<60}{:<12}".format('Standard deviation of noise added in each iteration:   ',reg_noise_std))
    f.write("\n{:<60}{:<12}".format('Exponential weight on output:   ',exp_weight))
    f.write("\n\n{:<60}".format('Entire Net:'))
    f.write("\n\n{:<60}".format(net))