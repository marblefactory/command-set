from Actions import *
from Movement import *

############
# Movement #
############

# Run half way down the corridor
m1 = Move(to=Relative(to=Object('corridor'), proportion=0.5), speed=Speed.FAST)

# Slowly crawl to the end of the room
m2 = Move(to=Relative(to=Object('room')), speed=Speed.SLOW, stance=Speed.SLOW)

# Walk to office 811
m3 = Move(to=Object('room 812', location=Absolute()))

# Go back to the last door
m4 = Move(to=Rememebered(Object("door"), index=MemoryIndex(StartPos.END)))

# Go Prone behind the grey desk in room 812
m5 = Composite(Move(to=Object('room 812', location=Absolute()), stance=Stance.PRONE), Move(to=Object('desk'), stance=Stance.PRONE))

# Go through the door on your right
m6 = Move(to=Object('door', location=Contextual(direction=Direction.RIGHT)))

# Go back to the 2nd door you came
m7 = Move(to=Rememebered(obj=Object('door'), index=MemoryIndex(StartPos.START, offset=1)))

# Go the the 2nd door on the right
m8 = Move(to=Object('door', location=Contextual(direction=Direction.RIGHT, num=1)))

print(m5)
