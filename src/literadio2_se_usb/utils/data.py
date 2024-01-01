from dataclasses import dataclass


@dataclass
class Controls:
    roll: int = 0
    pitch: int = 0
    throttle: int = 0
    yaw: int = 0

    sa: int = 0
    sb: int = 0
    sc: int = 0
    sd: int = 0
