


class person:
    def __init__(self, name,country,date_of_birth ):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def getdate_of_birth(self):
        print("Date of Birth of the person: ", self.date_of_birth)
        return self.date_of_birth
    
d1 = person("DJ", "USA", "1990-01-01")
d1.getdate_of_birth()


