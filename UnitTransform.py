
class UnitTransform():
    """
    Class responsible for transforming the lb to kg and feet to cm
    """
    @staticmethod
    def lbs_to_kg(weight):
            return weight / 2.2

    @staticmethod
    def feet_to_cm(height):
        return height / 3.28084