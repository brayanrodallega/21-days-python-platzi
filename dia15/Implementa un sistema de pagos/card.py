from pay import Pay

class Card(Pay):

    def __init__(self, card_number) -> None:
        super().__init__()
        self._card_number = card_number

    def make_pay(self, quantity):
        if len(self._card_number) == 16:
            info = super().make_pay(quantity)
            info["last_card_numbers"] = self._card_number[12:]
            return info
        else:
            raise Exception("La longitud de la tarjeta debe ser de 16 digitos")

    @property
    def card_number(self):
        return self._card_number
    
    @card_number.setter
    def card_number(self, card_number):
        self._card_number = card_number
    