class KomodoDragon:
    def __init__(self, arms, legs, eyes, tail, furry):
        self.arms=arms
        self.legs=legs
        self.eyes=eyes
        self.tail=tail
        self.furry=furry
    
    def print_attributes(self):
        print(self.arms,self.legs,self.eyes,self.tail,self.furry)
        
instance = KomodoDragon(arms=2.5, legs=2.5, eyes=2, tail=True, furry=False)

instance.print_attributes()