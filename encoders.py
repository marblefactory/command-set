import json
from enum     import Enum
from objects import *
from movements import *
from actions  import *
from locations import *


class EnumEncoder(json.JSONEncoder):
    """
    Encodes a generic Enum in JSON format
    """
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.name
        return json.JSONEncoder.default(self, obj)


class LocationEncoder(json.JSONEncoder):
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
        return json.JSONEncoder.default(self, obj)


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
                'type'         : 'rememebered',
                'iteration_dir': json.loads(json.dumps(obj.iteration_dir,cls=EnumEncoder)),
                'offset'       : obj.offset
            }
        return json.JSONEncoder.default(self, obj)


class ObjectEncoder(json.JSONEncoder):
    """
    Encodes an Object in JSON format
    """
    def default(self, obj):
        if isinstance(obj, Relative):
            return json.loads(json.dumps(obj, cls=RelativeEncoder))
        if isinstance(obj, Object):
            return {
                'type'     : 'object',
                'name'     : obj.name,
                'location' : json.loads(json.dumps(obj.location, cls=LocationEncoder))
            }

        return json.JSONEncoder.default(self, obj)


class RelativeEncoder(ObjectEncoder):
    """
    Encodes an Object in JSON format
    """
    def default(self, obj):
        if isinstance(obj, Relative):
            return {
                'type'      : 'relative',
                'to'        : json.loads(json.dumps(obj.to, cls=ObjectEncoder)),
                'proportion': obj.proportion
            }

        return json.JSONEncoder.default(self, obj)


class ActionEncoder(json.JSONEncoder):
    """
    The Abstract Action Encoder

    Used to get the type of the objet and call the relevant encoder.
    """
    def default(self, obj):
        if isinstance(obj, Move):
            return json.loads(json.dumps(obj, cls=MoveEncoder))
        elif isinstance(obj, Composite):
            return json.loads(json.dumps(obj, cls=CompositeEncoder))
        return json.JSONEncoder.default(self, obj)


class CompositeEncoder(ActionEncoder):
    """
    Encodes a Composite Action in JSON format
    """
    def default(self, obj):
        if isinstance(obj, Composite):
            return {
                'type'      : 'composite',
                'actions'   : [json.loads(json.dumps(encodedAction,cls=ActionEncoder)) for encodedAction in obj.actions]
            }
        return json.JSONEncoder.default(self, obj)


class MoveEncoder(ActionEncoder):
    """
    Encodes a Move in JSON format
    """
    def default(self, obj):
        if isinstance(obj, Move):
            return {
                'type'      : 'move',
                'speed'     : json.loads(json.dumps(obj.speed, cls=EnumEncoder)),
                'stance'    : json.loads(json.dumps(obj.stance,cls=EnumEncoder)),
                'dest'      : json.loads(json.dumps(obj.dest,  cls=ObjectEncoder))
            }

        return json.JSONEncoder.default(self, obj)
