from abc import ABC
from abc import abstractmethod
from typing import Dict
from typing import Tuple

import torch


class AbsSVSModel(torch.nn.Module, ABC):
    """The common abstract class among each tasks
    "SVSModel" is referred to a class which inherits torch.nn.Module,
    and makes the dnn-models forward as its member field,
    a.k.a delegate pattern,
    and defines "loss", "stats", and "weight" for the task.
    If you intend to implement new task in SVS,
    the model must inherit this class.
    In other words, the "mediator" objects between
    our training system and the your task class are
    just only these three values, loss, stats, and weight.
    Example:
        >>> from SVS2.tasks.abs_task import AbsTask
        >>> class YourSVSModel(AbsSVSModel):
        ...     def forward(self, input, input_lengths):
        ...         ...
        ...         return loss, stats, weight
        >>> class YourTask(AbsTask):
        ...     @classmethod
        ...     def build_model(cls, args: argparse.Namespace) -> YourSVSModel:
    """

    @abstractmethod
    def forward(
        self, **batch: torch.Tensor
    ) -> Tuple[torch.Tensor, Dict[str, torch.Tensor], torch.Tensor]:
        raise NotImplementedError

    @abstractmethod
    def collect_feats(self, **batch: torch.Tensor) -> Dict[str, torch.Tensor]:
        raise NotImplementedError