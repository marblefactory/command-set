from Actions import *
from Movement import *

############
# Movement #
############

# Run half way down the corridor
m1 = Move(location=Relative(to=Object('corridor'), proportion=0.5), speed=Speed.FAST)


# Slowly crawl to the end of the room
m2 = Move(location=Relative(to=Object('room')), speed=Speed.SLOW, stance=Speed.SLOW)

# Walk to office 811
m3 = Move(location=Object('room 812', relation=Relation.SPECIFIC))

# Go back to the last door
m4 = Move(location=Rememebered(Object("door"), index=MemoryIndex(StartPos.END)))

# Go Prone behind the grey desk in  room 812
m5 = Composite(Move(location=Object('room 812', relation=Relation.SPECIFIC), stance=Stance.PRONE), Move(location=Object('desk'), stance=Stance.PRONE))

# Go through the door on your right

# Go back to the 2nd door you came
m7 = Move(location=Rememebered(obj=Object('door'), index=MemoryIndex(StartPos.START, offset=1)))

# Go the the 2nd door on the right
