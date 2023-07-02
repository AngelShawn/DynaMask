from mmcv.utils import Registry, build_from_cfg
from mmdet.utils import get_root_logger
from torch import nn

BACKBONES = Registry('backbone')
NECKS = Registry('neck')
ROI_EXTRACTORS = Registry('roi_extractor')
SHARED_HEADS = Registry('shared_head')
HEADS = Registry('head')
LOSSES = Registry('loss')
DETECTORS = Registry('detector')


def build(cfg, registry, default_args=None):
    """Build a module.

    Args:
        cfg (dict, list[dict]): The config of modules, is is either a dict
            or a list of configs.
        registry (:obj:`Registry`): A registry the module belongs to.
        default_args (dict, optional): Default arguments to build the module.
            Defaults to None.

    Returns:
        nn.Module: A built nn module.
    """
    if isinstance(cfg, list):
        modules = [
            build_from_cfg(cfg_, registry, default_args) for cfg_ in cfg
        ]
        return nn.Sequential(*modules)
    else:
        return build_from_cfg(cfg, registry, default_args)


def build_backbone(cfg):
    """Build backbone."""
    return build(cfg, BACKBONES)


def build_neck(cfg):
    """Build neck."""
    return build(cfg, NECKS)


def build_roi_extractor(cfg):
    """Build roi extractor."""
    return build(cfg, ROI_EXTRACTORS)


def build_shared_head(cfg):
    """Build shared head."""
    return build(cfg, SHARED_HEADS)


def build_head(cfg):
    """Build head."""
    return build(cfg, HEADS)


def build_loss(cfg):
    """Build loss."""
    return build(cfg, LOSSES)


def build_detector(cfg, train_cfg=None, test_cfg=None):
    """Build detector."""
    model = build(cfg, DETECTORS, dict(train_cfg=train_cfg, test_cfg=test_cfg))

    logger = get_root_logger()
    logger.info(str(model))

    return model
