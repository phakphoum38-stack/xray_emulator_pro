import pydicom
from pydicom.dataset import Dataset
from pydicom.uid import generate_uid

def save(image, path):

    ds = Dataset()

    ds.PatientName = "Simulator^Patient"
    ds.PatientID = "SIM001"

    ds.Modality = "DX"

    ds.Rows, ds.Columns = image.shape

    ds.SamplesPerPixel = 1
    ds.PhotometricInterpretation = "MONOCHROME2"

    ds.BitsAllocated = 8
    ds.BitsStored = 8
    ds.HighBit = 7

    ds.PixelRepresentation = 0

    ds.StudyInstanceUID = generate_uid()
    ds.SeriesInstanceUID = generate_uid()

    ds.PixelData = image.tobytes()

    pydicom.dcmwrite(path, ds)

    print("[DICOM] Saved:", path)
