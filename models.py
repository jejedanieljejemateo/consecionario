

#La clase utilizada paraz el crud
class Car:#Car(Base):
    __tablename__ = "car"
    def __init__(self,name,brand,brach):
        self.name =name
        self.brand=brand
        self.brach=brach
        pass
    #name = Column(String, primary_key=True, index=True)
    #brand = Column(String(255), unique=True, index=True)
    #branch = Column(String(255))
