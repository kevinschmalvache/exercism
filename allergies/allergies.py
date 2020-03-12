class Allergies:
    ALLERGENS = "eggs peanuts shellfish strawberries tomatoes chocolate pollen cats".split()

    def __init__(self, score):
        self._lst = [item for (number, item) in enumerate(self.ALLERGENS) if (score >> number) & 1]

    def allergic_to(self, item):
        return item in self._lst

    @property
    def lst(self):
        return self._lst
