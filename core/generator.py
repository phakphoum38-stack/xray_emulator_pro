import time

class XRayGenerator:

    def __init__(self):
        self.kv = 70
        self.ma = 200
        self.exposure_time = 100

    def configure(self, kv, ma, exposure):

        self.kv = kv
        self.ma = ma
        self.exposure_time = exposure

        print(f"[GENERATOR] {kv}kV {ma}mA {exposure}ms")

    def fire(self):

        print("[GENERATOR] Exposure start")
        time.sleep(self.exposure_time/1000)
        print("[GENERATOR] Exposure done")

        return {
            "kv": self.kv,
            "ma": self.ma,
            "time": self.exposure_time
        }
