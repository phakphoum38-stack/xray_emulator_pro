import numpy as np

class Detector:

    def __init__(self, width=1024, height=1024):

        self.width = width
        self.height = height

    def capture(self, exposure):

        base = exposure["kv"] * 1.5

        image = np.random.normal(
            loc=base,
            scale=25,
            size=(self.height, self.width)
        )

        image = image.clip(0,255)

        return image.astype("uint8")
