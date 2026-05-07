class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return (f"{self.name} available from {self.start_time} to {self.end_time} : items available : {self.items}" )

  def calculate_bill(self,purchased_items):
    bill=0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return (f"Total bill: {bill}")

class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return (f"Franchise at {self.address}")

  def available_menus(self,time):
    menus_found = []
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        menus_found.append(menu)
    return menus_found   

class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises
  def __repr__(self):
    return (f"new Business {self.name} has {self.franchises}")
    
# Brunch menu
brunch = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch_menu = Menu("Branch_Menu",brunch,1100,1600)

#print(brunch_menu)

#Early Bird Menu
early_bird ={
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird_menu = Menu("Early_Bird_Menu",early_bird,1500,1800)

#print(early_bird_menu)

#Dinner Menu
dinner_menu = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu("Dinner_Menu",dinner_menu,1700,2300)

#print(dinner_menu)

#Kids Menu
kids_menu = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("Kids_Menu",kids_menu,1100,2100)

#print(kids)

#print(brunch_menu.calculate_bill(["pancakes", "home fries","coffee" ]))

#print(early_bird_menu.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)" ]))

#franchise objects

menus_list=[kids,dinner,early_bird_menu,brunch_menu]

flagship_store = Franchise("1232 West End Road",menus_list)
new_installment = Franchise("12 East Mulberry Street",menus_list)


#print(flagship_store)
#print(new_installment)
#print(flagship_store.available_menus(2200))

arepas_menu={
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas = Menu("Take a’ Arepa",arepas_menu,1000,2000)
arepas_place=Franchise("189 Fitzgerald Avenue",arepas)

arepas_business=Business("Take a' Arepa",arepas_place)
print(arepas_business)


