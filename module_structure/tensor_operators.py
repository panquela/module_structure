import torch


__all__ = ['Tensor_calculator']

class Tensor_calculator():

    def __init__(self):

        return None

    def tensor_ones(dim_x,
                   dim_y,
                   dim_z):

        ones = torch.ones([dim_x,dim_y,dim_z])

        return ones


