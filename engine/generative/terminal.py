import sys
from sample import Sample
from pattern import Pattern

N = 128  # Pattern Size


iteration = 0
input, INPUTS = 1, 4
layer, LAYERS = 1, 5

func = {
    1: Sample.creator,
    2: Sample.creator2,
    3: Sample.generator,
    4: Sample.creator2,
    5: Sample.creator2,
    6: Sample.creator2,
}

while True:
    # sample = generator()
    # sample = Sample.creator(N)
    sample = func[layer](N)
    iteration += 1
    print("input", input, "layer", layer, "iteration", iteration)
    d = Sample.discriminator(sample)

    if d[0] == True:
        # NArray.visualize(sample, {0: " ", 1: "+"})
        print(d)

        tile_path = sys.path[0] + f"/sample/{layer}_{input}.png"
        # pattern_path = sys.path[0] + f"/sample/{counter}_pattern.png"
        Pattern.create(sample, 64, tile_path)
        # Pattern.tile(tile_path, pattern_path, 3, 2)

        input += 1
        iteration = 0

        if input > INPUTS:
            input = 1
            layer += 1

        if layer > LAYERS:
            break
