from dataclasses import dataclass


@dataclass
class Paths:
    bucket: str
    path_to_s3: str
    path_to_local: str

