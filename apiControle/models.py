class Classroom:
    def __init__(self, id, name, capacity):
        self.id = id
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"Classroom {self.name} - Capacity: {self.capacity}"

class Schedule:
    def __init__(self, class_id, hour, reserved=False):
        self.class_id = class_id
        self.hour = hour
        self.reserved = reserved

    def __str__(self):
        return f"Class ID: {self.class_id}, Hour: {self.hour}, Reserved: {self.reserved}"
