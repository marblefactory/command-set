from networks  import Movement_NN
from movements import Move
from encoders  import MoveEncoder
from client    import Client
import json


print("\nMovement flow\n")

text   = "go to room 102a and then .."
print('Input text:"' + text + '"')

tensor = Movement_NN().run(text)

print('NN output: \n"' + str(tensor) + '"')
move = Move.from_tensor_and_text(tensor, text)
print('Move: "' + str(move) + '"')

data = json.dumps(move, cls=MoveEncoder)
print('JSON: ' + str(data))


client = Client(PORT=1024)

client.send(data)
