

import numpy as np
import torch
from ..model_tools import ModelMethods as sdf_ModelMethods
from ... import tensors as sdf_tensors

__all__ = ['Noise', 'Addition', 'Concatenation']


class Noise(sdf_ModelMethods):

    def __init__(self, scale=0.1):
        """

        :param scale: the sigma of the noise to be added to each batch input "x" is defined as the sigma of "x"
            multiplied by the "scale"
        :type scale: float | int
        """
        superclass = Noise
        try:
            # noinspection PyUnresolvedReferences
            self.superclasses_initiated
        except AttributeError:
            self.superclasses_initiated = []
        except NameError:
            self.superclasses_initiated = []

        if sdf_ModelMethods not in self.superclasses_initiated:
            sdf_ModelMethods.__init__(self=self)
            if sdf_ModelMethods not in self.superclasses_initiated:
                self.superclasses_initiated.append(sdf_ModelMethods)

        self.mu = 0.0
        # self.sigma = None
        self.scale = scale

        if superclass not in self.superclasses_initiated:
            self.superclasses_initiated.append(superclass)

    def forward(self, x, generator=None):
        """

        :param x: The batch input which the noise has to be added to.
        :type x: torch.Tensor | np.ndarray
        :param generator: The torch generator of the noise values.
        :type generator: torch.Generator | None
        :return: The noisy tensor.
        :rtype: torch.Tensor
        """
        # :type x: torch.Tensor # | list[torch.Tensor] | tuple[torch.Tensor]

        if self.training:
            return sdf_tensors.add_noise(x=x, scale=self.scale, mu=self.mu, generator=generator)
        else:
            return x


class Addition(sdf_ModelMethods):

    def __init__(self, axes, keepdim=False):
        """

        :param axes: The axes over which to perform the sum
        :type axes: int | list | tuple | torch.Tensor | np.ndarray
        :type keepdim: bool
        """
        superclass = Addition
        try:
            # noinspection PyUnresolvedReferences
            self.superclasses_initiated
        except AttributeError:
            self.superclasses_initiated = []
        except NameError:
            self.superclasses_initiated = []

        if sdf_ModelMethods not in self.superclasses_initiated:
            sdf_ModelMethods.__init__(self=self)
            if sdf_ModelMethods not in self.superclasses_initiated:
                self.superclasses_initiated.append(sdf_ModelMethods)

        if isinstance(axes, int):
            self.axes = tuple([axes])
        elif isinstance(axes, (list, torch.Size)):
            self.axes = tuple(axes)
        elif isinstance(axes, tuple):
            self.axes = axes
        elif isinstance(axes, (torch.Tensor, np.ndarray)):
            self.axes = tuple(axes.tolist())
        else:
            raise TypeError('axes')

        if isinstance(keepdim, bool):
            self.keepdim = keepdim
        else:
            raise TypeError('keepdim')

        if superclass not in self.superclasses_initiated:
            self.superclasses_initiated.append(superclass)

    def forward(self, x):
        """

        :param x: The input data.
        :type x: torch.Tensor | np.ndarray
        :return: The output data.
        :rtype: torch.Tensor
        """

        return torch.sum(input=x, dim=self.axes, keepdim=self.keepdim)


class Concatenation(sdf_ModelMethods):

    def __init__(self, axis):
        """

        :param axis: the axis over which to concatenate
        :type axis: int
        """
        superclass = Concatenation
        try:
            # noinspection PyUnresolvedReferences
            self.superclasses_initiated
        except AttributeError:
            self.superclasses_initiated = []
        except NameError:
            self.superclasses_initiated = []

        if sdf_ModelMethods not in self.superclasses_initiated:
            sdf_ModelMethods.__init__(self=self)
            if sdf_ModelMethods not in self.superclasses_initiated:
                self.superclasses_initiated.append(sdf_ModelMethods)

        if isinstance(axis, int):
            self.axis = axis
        else:
            raise TypeError('axis')

        if superclass not in self.superclasses_initiated:
            self.superclasses_initiated.append(superclass)

    def forward(self, xs):
        """

        :param xs: The input data.
        :type xs: list[torch.Tensor | np.ndarray]
        :return: The output data.
        :rtype: torch.Tensor
        """

        return torch.concatenate(tensors=xs, dim=self.axis, out=None)
