class FabricDesign:
    def __init__(self,temperature,mood):
        self.temperature=temperature
        self.mood=mood
        self.pattern=self.generate_pattern()

        def generate_pattern(self):
            if self.temperature>25 and mood<5:
                return f"{pattern} changes to sunflower"
            elif self.temperature<25 and mood>5:
                return f"{pattern} changes to wavy"
            else: 
                return f"{pattern} remains sunflower or wavy"