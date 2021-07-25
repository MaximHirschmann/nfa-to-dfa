alphabet = input("Gib das Alphabet in der Form \"a b c\" ohne \"\" ein!\n").split(" ")

states = input("Gib die Zustände in der Form \"q0 q1 q2\" ohne \"\" ein!\n").split(" ")

startingStates = input("Gib die Anfangszustände \"q0 q1 q2\" ohne \"\" ein!\n").split(" ")

endingStates = input("Gib die Endzustände \"q0 q1 q2\" ohne \"\" ein!\n").split(" ")
transitions = "\n"
while(True):
    text = input("Gebe eine neue Kante der Form \"q0 a q1 q2\" für (q0, a ->q1,q2) ein:\n")
    if(text == "NONE"):
        break
    text = text.split(" ")
    states = text[2]
    for i in range(3, len(text)):
        states += ", "+str(text[i])
    transitions += str(text[0]+", "+text[1]+" -> "+states+"\n")
from collections import defaultdict, deque
class Graph:
    def __init__(self, V):
        self.V = V
        self.pointsTo = defaultdict(list)
    
    def addEdge(self, beg, end, letter):
        self.pointsTo[(beg, letter)].append(end)

def transitionsToGraph(transitions):
    g = Graph(len(states))
    for line in transitions.split("\n"):
        split = line.replace(" ", "").replace("\n", "").split("->")
        if len(split) < 2:
            continue
        l, r = split
        split2 = l.split(",")
        beginningState = split2[0]
        letter = split2[1]
        split3 = r.split(",")
        for endingState in split3:
            g.addEdge(beginningState, endingState, letter)
    return g

space = 50

graph = transitionsToGraph(transitions)

memory = {tuple(startingStates): True}
q = deque([startingStates])

print(" "*(space + 5), end="")
for letter in alphabet:
    print(letter.ljust(space), end="")
print()
print("-"*(space * (len(alphabet)+1)))
counter = 0
while len(q) > 0:
    currentStates = q.popleft()
    prefix = ""
    isStarting = currentStates == startingStates
    isFinal = any([i in endingStates for i in currentStates])
    if isStarting and isFinal:
        prefix = "S, F"
    elif isStarting:
        prefix = "S"
    elif isFinal:
        prefix = "F"
    print((prefix.ljust(5) + currentStates.__str__().replace("[", "{").replace("]", "}")).ljust(space), end="")

    for letter in alphabet:
        new = set()
        for currentState in currentStates:
            for v in graph.pointsTo[(currentState, letter)]:
                new.add(v)
        new = sorted(list(new))
        print(new.__str__().replace("[", "{").replace("]", "}").ljust(space), end = "")
        if tuple(new) not in memory:
            memory[tuple(new)] = True
            q.append(new)
    print("s"+str(counter))
    counter += 1

input("press Enter to exit")
