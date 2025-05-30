from enum import auto, Enum


class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class RunMode(StrEnum):
    app = auto()
    back_office_app = auto()
    generator = auto()
    runpod = auto()
