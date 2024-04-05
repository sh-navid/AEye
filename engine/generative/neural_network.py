import sys


INPUTS = 4
LAYERS = 5


mermaid = f"""
## NN with {INPUTS} inputs and {LAYERS} hidden layers

```mermaid
flowchart LR

"""
header = []
spacer = []


for i in range(1, INPUTS + 1):
    input=[]
    for l in range(1, LAYERS + 1):
        if l<LAYERS:
            mermaid+=f"{l}_{i} --- {l+1}_{i}\n"
        else:
            mermaid+=f"{l}_{i} --- output\n"

        if l==1:
            mermaid+=f"input --- {l}_{i}\n"

        if i>1 and l<LAYERS:
            mermaid+=f"{l}_{i} --- {l+1}_{i-1}\n"
        if i<INPUTS and l<LAYERS:
            mermaid+=f"{l}_{i} --- {l+1}_{i+1}\n"
        

        mermaid+=f"{l}_{i}((<img src='./sample/{l}_{i}.png' height='80' style='border-radius:2em'>))\n"

mermaid+="```"

with open(sys.path[0] + "/neural_network.md", "w") as f:
    f.write(mermaid)