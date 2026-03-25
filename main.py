from core.generator import XRayGenerator
from core.detector import Detector
from core.physics import apply_attenuation
from core.imaging_pipeline import enhance

from dicom.dicom_export import save
from dicom.pacs_simulator import PACSServer

generator = XRayGenerator()
detector = Detector()
pacs = PACSServer()

generator.configure(80,200,100)

exp = generator.fire()

image = detector.capture(exp)

image = apply_attenuation(image)

image = enhance(image)

save(image,"output.dcm")

pacs.store("output.dcm")

print("Simulation complete")
