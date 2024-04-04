import sys


INPUTS = 6
LAYERS = 4


markdown = ""
header = []
spacer = []


for l in range(1, LAYERS + 1):
    header.append(f"Layer{l}")
    spacer.append(f"------")


header_section = "|input|" + "|".join(header) + "|output|\n"
spacer_section = "|-----|" + "|".join(spacer) + "|------|\n"
markdown += header_section + spacer_section


for r in range(1, INPUTS + 1):
    row = ["" + str(r)]
    for l in range(1, LAYERS + 1):
        row.append(f"![](./sample/{l}_{r}.png)")
    row.append("" + str(r))
    markdown += "|" + "|".join(row) + "|\n"


with open(sys.path[0] + "/neural_network.md", "w") as f:
    f.write(markdown)
