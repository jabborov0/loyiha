# class davlatlar:
#     def __init__( self, nomi,poytaxt, aholi, joylashuv):
#         self.nomi = nomi
#         self.poytaxt = poytaxt
#         self.aholi = aholi
#         self.joylashuv = joylashuv
        
        


#     def get_nomi(self):
#         return f"{self.nomi.title()}"
#     def info(self):
#         return f"{self.nomi.title()} davlatining poytahti {self.poytaxt} shahri {self.aholi} nafar aholiga ega" 
#     def get_joylashuv(self):
#         return f"{self.nomi.title()} daavlati {self.joylashuv} da joylashgan"
    
# uzb = davlatlar('uzbekiston', 'toshkent', 38, 'Orta Osiyo')



class shaxs:
    def __init__(self, ism, familiya, ochestva, yoshi):
        self.name = ism
        self.surname = familiya
        self.fname = ochestva
        self.age = yoshi
    
class talaba (shaxs):
    def __init__(self, ism, familiya, tyil, bosqich):
        super().__init__(ism, familiya, tyil)
        self.bosqich = bosqich
    def get_bosqich(self):
        return f"{self.get_name()} {self.bosqich} - bosqich talabasi"
    

class fanlar(talaba):
    def __init__(self,ism,familiya,tyil,bosqich,fan,ustoz):
        super().__init__(ism,familiya,tyil,bosqich)
        self.fan = fan
        self.fan = ustoz
    def get_fan(self)
        return f"{self.fan.title()}"
    def get_ustoz(self):
        return f"{self.ustoz}"
    
talaba = fanlar('murod', 'karimov', 1998, 4, 'oliy matematika', 'professor atxam boburovich')
print(talaba.get_info())
