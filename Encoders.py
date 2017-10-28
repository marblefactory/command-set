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
            return obj.name
        return json.JSONEncoder.default(self, obj)


class LocationEncoder(json.JSONEncoder, ABC):
    """
    The Abstract Location Encoder

    Used to get the type of the objet and call the relevant encoder.
    """
    def default(self, obj):
        if isinstance(obj, Contextual):
            return json.loads(json.dumps(obj, cls=ContextualEncoder))
        elif isinstance(obj, Rememebered):
            return json.loads(json.dumps(obj, cls=RememberedEncoder))
        elif isinstance(obj, Absolute):
            return json.loads(json.dumps(obj, cls=AbsoluteEncoder))

# TODO Encoder for the Absolute class
class AbsoluteEncoder(LocationEncoder):
    """
    Encodes an Absolute Location in JSON format
    """
    def default(self, obj):
        if isinstance(obj, Absolute):
            return {
                'type'     : 'absolute'
            }
        return json.JSONEncoder.default(self, obj)

class ContextualEncoder(LocationEncoder):
    """
    Encodes a Contextual Location in JSON format
    """
    def default(self, obj):
        if isinstance(obj, Contextual):
            return {
                'type'     : 'contextual',
                'direction': json.loads(json.dumps(obj.direction,cls=EnumEncoder)),
                'num'      : obj.num
            }
        return json.JSONEncoder.default(self, obj)

class RememberedEncoder(LocationEncoder):
    """
    Encodes a Rememebered Location in JSON format
    """
    def default(self, obj):
        if isinstance(obj, Rememebered):
            return {
                'type'     : 'rememebered',
                'start_pos': json.loads(json.dumps(obj.start,cls=EnumEncoder)),
                'offset'   : obj.offset
            }
        return json.JSONEncoder.default(self, obj)

class ObjectEncoder(json.JSONEncoder):
    """
    Encodes an Object in JSON format
    """
    def default(self, obj):
        if isinstance(obj, Object):
            return {
                'name'     : obj.name,
                'location' : json.loads(json.dumps(obj.location, cls=LocationEncoder))
            }

        return json.JSONEncoder.default(self, obj)
