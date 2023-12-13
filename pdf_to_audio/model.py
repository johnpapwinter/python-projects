from dataclasses import dataclass


@dataclass
class Document:
    filename: str
    text: str

