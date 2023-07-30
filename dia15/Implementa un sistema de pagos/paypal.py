from pay import Pay

class PayPal(Pay):

    def __init__(self, email) -> None:
        super().__init__()
        self._email = email

    def make_pay(self, quantity):
        info = super().make_pay(quantity)
        info["platform"] = "PayPal"
        info["email"] = self._email
        return info
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email