import json
from enum import Enum
from abc import ABC

from Movement import *


class EnumEncoder(json.JSONEncoder):
    """
    Encodes a generic Enum in JSON format
    """
    def default(self, obj):
        if isinstance(obj, Enum):
            return {'value': obj.value}
        return json.JSONEncoder.default(self, obj)


class LocationEncoder(json.JSONEncoder, ABC):
    """
    The Abstract Location Encoder
    """
    pass

class ContextualEncoder(json.JSONEncoder):
    """
    Encodes a Contextual Location in JSON format
    """
    def default(self, obj):
        if isinstance(obj, Contextual):
            return {
                'direction': json.loads(json.dumps(obj.direction,cls=EnumEncoder)),
                'num'      : obj.num
            }
        return json.JSONEncoder.default(self, obj)
