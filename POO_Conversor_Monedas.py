
class Money:

    rates = {
        'USD' : 1,
        'ARS' : 350,
        'EUR' : 1.2,
        'GBP' : 1.3
    }

    def __init__(self, quantity, currency):
        if currency not in Money.rates:
            raise ValueError(f'Moneda desconocida: {currency}')
        self.quantity = float(quantity)    
        self.currency = currency

    def __str__(self):
        return f'{self.quantity:.2f} {self.currency}'
    
    def to_usd(self):
        return self.quantity / Money.rates[self.currency]
    
    def from_usd(amount_usd, target_currency):
        if target_currency not in Money.rates:
            raise ValueError(f'Moneda desconocida: {target_currency}')
        return amount_usd * Money.rates[target_currency]

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        total_usd = self.to_usd() + other.to_usd()
        total_in_self_currency = Money.from_usd(total_usd, self.currency)
        return Money(total_in_self_currency, self.currency) 
    
    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return abs(self.to_usd() - other.to_usd()) < 1e-9

def main():

    m1 = Money(10, 'USD')
    m2 = Money(2000, 'ARS')

    print(m1)
    print(m2)

    suma1 = m1 + m2
    print('Suma:', suma1)

    suma2 = m2 + m1
    print('Suma en ARS:', suma2)

    m3 = Money(5, 'GBP') + Money(1000, 'ARS')
    print('GBP', m3)

if __name__ == '__main__':
    main()

    