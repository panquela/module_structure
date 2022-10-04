import torch


__all__ = ['Torch_calculator']

class Torch_calculator():

    def __init__(self):

        return None

    def torch_ones(dim_x,
                   dim_y,
                   dim_z):

        ones = torch.ones([dim_x,dim_y,dim_z])

        return ones


