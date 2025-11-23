
class Vehicle:
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def display_info(self):
      
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")



class Car(Vehicle):
    def __init__(self, brand: str, year: int, num_doors: int):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def display_info(self):
      
        super().display_info()
        print(f"Number of doors: {self.num_doors}")



class Motorcycle(Vehicle):
    def __init__(self, brand: str, year: int, has_sidecar: bool):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
      
        super().display_info()
        sidecar_text = "Yes" if self.has_sidecar else "No"
        print(f"Has sidecar: {sidecar_text}")



if __name__ == "__main__":
    v = Vehicle("GenericBrand", 2010)
    print("=== Vehicle ===")
    v.display_info()

    print("\n=== Car ===")
    c = Car("Toyota", 2022, num_doors=4)
    c.display_info()

    print("\n=== Motorcycle ===")
    m = Motorcycle("Harley", 2018, has_sidecar=False)
    m.display_info()
