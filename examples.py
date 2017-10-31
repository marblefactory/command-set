from objects import *
from actions import *
from movement import *

############
# Movement #
############

print("\nMovement examples:")

# Run half way down the corridor
m1 = Move(to=Relative(to=Object('corridor'), proportion=0.5), speed=Speed.FAST)
print(m1)

# Slowly crawl to the end of the room
m2 = Move(to=Relative(to=Object('room')), speed=Speed.SLOW, stance=Speed.SLOW)
print(m2)

# Walk to office 811
m3 = Move(to=Object('room 812',
          location=Absolute()))
print(m3)

# Go back to the last door
m4 = Move(to=Object(name='door', location=Rememebered(iteration_dir=MemoryIterationDirection.END_TO_START, offset=0)))
print(m4)

# Go Prone behind the grey desk in room 812
m5 = Composite(Move(to=Object('room 812', location=Absolute()), stance=Stance.PRONE), Move(to=Object('desk'), stance=Stance.PRONE))
print(m5)

# Go through the door on your right
m6 = Move(to=Object('door', location=Contextual(direction=Direction.RIGHT)))
print(m6)

# Go back to the 2nd doors you came
m7 = Move(to=Object(name='door', location=Rememebered(iteration_dir=MemoryIterationDirection.START_TO_END, offset=1)))
print(m7)

# Go the the 4th door on the right
m8 = Move(to=Object('door', location=Contextual(direction=Direction.RIGHT, num=3)))
print(m8)


############
# JSON     #
############
from encoders import *
import json

print("\nJSON examples:")

print("Absolute Location       : " + json.dumps(Absolute(), cls=LocationEncoder))
print("Contextual Location     : " + json.dumps(Contextual(), cls=LocationEncoder))
print("Rememebered Location    : " + json.dumps(Rememebered(MemoryIterationDirection.END_TO_START), cls=LocationEncoder))
print("Object with Contextual  : " + json.dumps(Object(name='door'), cls=ObjectEncoder))
print("Object with Rememebered : " + json.dumps(Object(name='door', location=Rememebered(MemoryIterationDirection.END_TO_START)), cls=ObjectEncoder))
print("Relative Object         : " + json.dumps(Relative(to=Object(name='door', location=Rememebered(MemoryIterationDirection.END_TO_START)), proportion=0.5), cls=ObjectEncoder))
print("Move Action             : " + json.dumps(Move(to=Object('door', location=Contextual(direction=Direction.RIGHT))), cls=ActionEncoder))
print("Composite Action        : " + json.dumps(Composite(Move(to=Object('room 812', location=Absolute()), stance=Stance.PRONE), Move(to=Object('desk'), stance=Stance.PRONE)), cls=ActionEncoder))
