# Neural Net Ideas
---
# Goal
To take a string of spoken text, run though several NNs and result in a tensor that can help post processing to create an Action.

## Action NN

### Input
A vector the size of the entire vocabulary containing `0` or `1` to indicate whether the word was in the spoken command. (As in the sentiment analysis class)

For example, the spoken phrase "Run to the room at the end of the corridor" would result in the following input tensor.

`[chair tree run and the room corridor end to dog window ...]`

`[0     0    1   0   1   1    1        1   1  0   0 ...]`

### Output
This first NN would then output a smaller vector to indicet which type of action the text was describing. As the above vector describes a Move command, the output would be:

`[Look Interact Move Compound Stop Invalid]`

`[0    0        1    0        0    0]`

This vectore would then indicate which of the other NNs to use for the next step.

## Movement NN
### Input
Each of the subsiquent NNs would also recieve the inital large vectors.

### Output
The output would describe the attributes of the movement command. For example,
the spoken phrase "Run to room 821" would be described by the following vector:

`[Slow Fast Standing Prone AbsoluteLoc RememberedLoc ContextualLoc]`

`[0    1    1        0     1        0          0]`

The vector contains how fast the movement should be, what stance the player should move in, and information about the location of the object.

From here, more information needs be gathered about the object to move to. For example, we don't yet know what object to move to, only that it's at an absolute location.

## Compound Action NN
If the first neural network decides the spoken phrase is a compound action, e.g. "go to room 821, then hack the camera", the phrase could be split on joining words (e.g. "then") to create a list of phrases. Each phrase could then be passed through the pipeline of NNs to determine each action in the compound action.

## Natural Language Post Processing
To get the rest of the required information, a NL library would be used. For example,
in the phrase "Run to room 821" we know we're looking for an absolute location to move the spy to, so we search through the spoken phrase looking for nouns which are also absolute locations in the game, "room 821" in this case.

# Generating BNF classes
Now we've got all the information we need an `Action` can be created.

### Example
Given the spoken phrase "run to room 821" we have how fast to move the spy, what stance they are in from the NN and "room 821" from post processing. Therefore the following Python object can be created:

`Move(to=Object("room 821", location=Absolute()), speed=Speed.FAST, stance=Stance.Stand)`
