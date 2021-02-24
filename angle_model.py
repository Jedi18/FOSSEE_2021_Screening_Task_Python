class AngleModel:
    """Angle Model Class"""
    column_names = []
    column_types = []

    def __init__(self, data):
        self.id = data[0]
        self.designation = data[1]
        self.data = data
