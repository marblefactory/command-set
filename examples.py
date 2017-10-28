from Actions import *
from Movement import *

# ############
# # Movement #
# ############
#
# print("\nMovement examples:")
#
# # Run half way down the corridor
# m1 = Move(to=Relative(to=Object('corridor'), proportion=0.5), speed=Speed.FAST)
# print(m1)
#
# # Slowly crawl to the end of the room
# m2 = Move(to=Relative(to=Object('room')), speed=Speed.SLOW, stance=Speed.SLOW)
# print(m2)
#
# # Walk to office 811
# m3 = Move(to=Object('room 812', location=Absolute()))
# print(m3)
#
# # Go back to the last door
# m4 = Move(to=Object(name='door', location=Rememebered(start=StartPos.END, offset=0)))
# print(m4)
#
# # Go Prone behind the grey desk in room 812
# m5 = Composite(Move(to=Object('room 812', location=Absolute()), stance=Stance.PRONE), Move(to=Object('desk'), stance=Stance.PRONE))
# print(m5)
#
# # Go through the door on your right
# m6 = Move(to=Object('door', location=Contextual(direction=Direction.RIGHT)))
# print(m6)
#
# # Go back to the 2nd doors you came
# m7 = Move(to=Object(name='door', location=Rememebered(start=StartPos.START, offset=1)))
# print(m7)
#
# # Go the the 4th door on the right
# m8 = Move(to=Object('door', location=Contextual(direction=Direction.RIGHT, num=3)))
# print(m8)

############
# JSON     #
############
from Encoders import *
import json

print("\nJSON examples:")

tester = Contextual()
print(json.dumps(tester, cls=ContextualEncoder))
