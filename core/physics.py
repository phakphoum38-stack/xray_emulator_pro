import numpy as np

def apply_attenuation(image):

    attenuation_map = np.random.uniform(
        0.6,
        1.0,
        image.shape
    )

    return (image * attenuation_map).astype("uint8")
