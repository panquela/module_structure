import torch


__all__ = ['TensorCalculator']

class TensorCalculator():

    def __init__(self):

        return None

    def tensor_ones(dim_x,
                   dim_y,
                   dim_z):

        ones = torch.ones([dim_x,dim_y,dim_z])

        return ones


