class universe:
    def __init__(self, name,size):
        self.name = name
        self.size = size
        
    def get_universe_info(self):
        return f"Universe: {self.name}, Size: {self.size}"
    
class earth(universe):
    def __init__(self,name,size,population):
        super().__init__(name,size)
        self.population = population
        
        
    def get_earth_info(self):
        return f"Earth: {self.name}, Size: {self.size}, Population: {self.population}"
    
class asia(earth):
    def __init__(self,name,size,population,area):
        super().__init__(name,size,population)
        self.area = area
        
    def get_asia_info(self):
        return f"Asia: {self.name}, Size: {self.size}, Population: {self.population}, Area: {self.area}"
    
u1 = universe("Milky Way", "Large")
print(u1.get_universe_info())

e1 = earth("Earth", "Medium", 7_000_000_000)
print(e1.get_earth_info())

a1 = asia("Asia", "Small", 4_500_000_000, "44.58 million km²")
print(a1.get_asia_info())
    
    
class pakistan(asia):
    def __init__(self,name,size,population,area,capital):
        super().__init__(name,size,population,area)
        self.capital = capital
        
    def get_pakistan_info(self):
        return f"Pakistan: {self.name}, Size: {self.size}, Population: {self.population}, Area: {self.area}, Capital: {self.capital}"
    
class korea(asia):
    def __init__(self,name,size,population,area,capital):
        super().__init__(name,size,population,area)
        self.capital = capital
        
    def get_korea_info(self):
        return f"Korea: {self.name}, Size: {self.size}, Population: {self.population}, Area: {self.area}, Capital: {self.capital}"
    
class india(asia):
    def __init__(self,name,size,population,area,capital):
        super().__init__(name,size,population,area)
        self.capital = capital
    
    def get_india_info(self):
        return f"India: {self.name}, Size: {self.size}, Population: {self.population}, Area: {self.area}, Capital: {self.capital}"
    
p1 = pakistan("Pakistan", "Medium", 240_000_000, "881,913 km²", "Islamabad")
print(p1.get_pakistan_info())

k1 = korea("Korea", "Small", 51_000_000, "220,847 km²", "Seoul")
print(k1.get_korea_info())

i1 = india("India", "Large", 1_400_000_000, "3.287 million km²", "New Delhi")
print(i1.get_india_info())














#next

class real_state:
    company_name = "Fatima Real State"
    Serial_code = "12343E234"

  

    @classmethod
    def get_company_name(cls):
        return f"Company: {cls.company_name}, Serial: {cls.Serial_code}"

    @staticmethod
    def get_prophit():
        price_of_purchase = 1000000
        price_of_selling = 1200000
        if price_of_purchase > price_of_selling:
            print("Loss")
        elif price_of_purchase < price_of_selling:
            print("Profit")
        else:
            print("No Profit No Loss")

    def instance_method(self, name, price):
        self.name = name
        self.price = price
        print(f"Name: {self.name}, Price: {self.price}")


class real_state_chief_officer(real_state):
    def __init__(self, officer_name, officer_age):
        super().__init__()
        self.officer_name = officer_name
        self.officer_age = officer_age
        print(f"Officer Name: {self.officer_name}, Officer Age: {self.officer_age} , Company: {self.company_name}")


p1 = real_state()
p1.instance_method("House", 2000000)

print(real_state.get_company_name())
real_state.get_prophit()

officer = real_state_chief_officer("John Doe", 45)
