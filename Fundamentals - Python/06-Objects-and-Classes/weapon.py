class Weapon:
    
    def __init__(self, number_of_bullets: int):
        self.number_of_bullets = number_of_bullets
        
    def shoot(self):
        if self.number_of_bullets > 0:
            self.number_of_bullets -= 1
            return f"shooting..."
        else:
            return f"no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.number_of_bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)


        
        