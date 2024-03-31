import random
from n_array import NArray

N = 5


def creator():
    """
    This is the real data creator
    ___

    Generate (N2+1)x(N2+1) original patterns
    Like the one below
    - - - - - + - - - - -
    - - - - + - + - - - -
    - - - + - - - + - - -
    - - + - - - - - + - -
    - + - - - - - - - + -
    + - - - - - - - - - +
    - + - - - - - - - + -
    - - + - - - - - + - -
    - - - + - - - + - - -
    - - - - + - + - - - -
    - - - - - + - - - - -
    """
    D = N + 1
    sample = NArray.n2(D)
    x, y = 0, D - 1
    while x < D:
        sample[y][x] = 1
        x += random.choice([0, 1])
        y -= random.choice([0, 1])
        if y < 0:
            y = 0
    sample = NArray.unfold(sample)
    if random.choice([0,1])==1:
        sample=NArray.rotate90(sample)
    return sample


# Step 1
def generator():
    """
    This is the fake data generator
    FIXME: this should be NN
    """
    pass


# Step 2
def discriminator():
    """
    This is the investigator
    FIXME: this should be NN
    """
    pass


sample = creator()
NArray.visualize(sample)