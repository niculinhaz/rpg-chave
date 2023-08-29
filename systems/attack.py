
from effect import Effect


class InvalidDamage(Exception):
    pass


class Attack(object):
    def __init__(self, dmg: int, description: str, effects: list[Effect] = []) -> None:
        if dmg < 0:
            raise InvalidDamage("O dano passado para o ataque não pode ser menor que zero.")
        
        self._damage = dmg
        self.description = description
        self.effects = effects

    @property
    def damage(self) -> int:
        return self._damage
    
    @damage.setter
    def damage(self, value) -> None:
        if value < 0:
            raise InvalidDamage("O dano passado para o ataque não pode ser menor que zero.")
        
        self._damage = value
