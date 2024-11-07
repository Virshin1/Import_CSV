import csv

class Store:
    cost=0.9
    all=[]
    def __init__(self,name:str, price:float, quantity:int):
        self.name=name
        self.price=price
        self.quantity=quantity
        Store.all.append(self)
        assert price>=0,f"{self.price} is not valid!!"
        assert quantity>=0,f"{self.quantity} is not valid!!"
    def __repr__(self):
        return f"Store('{self.name}', {self.price}, {self.quantity})"
    @classmethod
    def from_csv(cls):
        with open("Store.csv","r") as f :
            reader=csv.DictReader(f)
            content=list(reader)
            for item in content:
               Store(
                   name=item.get('name'),
                   price = float(item.get('price')),
                   quantity =int(item.get('quantity'))
               )
Store.from_csv()
print(Store.all)







