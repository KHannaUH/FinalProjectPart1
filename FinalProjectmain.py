## Name: Karim Hanna StudID: 1969165
import csv # import csv to read / write files
from datetime import datetime # imports current date to compare later


class Item:
    ## this init fuctions stores all the values
    def __init__(self, item_id, manufacturer_name, item_type, item_price=None, service_date=None,
                 damage=None):  # item = Item(item_id, manufacturer_name, item_type)
        self.item_id = item_id
        self.manufacturer_name = manufacturer_name
        self.item_type = item_type
        if item_price != None:
            self.item_price = int(item_price)
        if service_date != None:
            self.service_date = datetime.strptime(service_date, '%m/%d/%Y').date()  # 1/10/2000
        if damage != None:
            self.damage = damage
    # converts date that prints into m/d/y
    def get_service_date(self):
        return datetime.strftime(self.service_date, '%#m/%#d/%Y')


class Inventory:
    def __init__(self, items):  # inv = Inventory()
        self.items = items  # dictionary of item_id to Item object
        self.types = []
        for key, value in items.items():
            ## if values are not present they are added in
            if value.item_type not in self.types:
                self.types.append(value.item_type)
        ## this fuction when called on will start wrting in FullInventory.csv file
    def fullInventoryReport(self):
        with open('FullInventory.csv', 'w') as file:
            #sorts item based on manufacturer name
            sorted_items = sorted(items.values(), key=lambda v: v.manufacturer_name)
            ## the for function writes in all values line by line
            for i in sorted_items:
                file.write(
                    f'{i.item_id},{i.manufacturer_name},{i.item_type},{i.item_price},{i.get_service_date()},{i.damage}\n')

    def itemInventoryReports(self):
        for current_type in self.types: ## creates files under tower phone laptop
            with open(current_type.title() + 'Inventory.csv', 'w') as file:
                sorted_items = sorted(items.values(),key=lambda v: v.item_id) #sorts values based on item id
                for i in sorted_items:
                    if i.item_type == current_type: #prints values line by line
                        file.write(f'{i.item_id},{i.manufacturer_name},{i.item_price},{i.get_service_date()},{i.damage}\n')

    def pastServiceInventoryReport(self):
        with open('PartServiceDateInventory.csv', 'w') as file: #opens PartServiceDateInventory.csv file in write mode
            sorted_items = sorted(items.values(),
                                  key=lambda v: v.service_date)  # puts values in order based on service date
            for i in sorted_items:
                if i.service_date < datetime.now().date(): # if function to check if its was serverced before today
                    file.write(
                        f'{i.item_id},{i.manufacturer_name},{i.item_type},{i.item_price},{i.get_service_date()},{i.damage}\n')

    def damageInventoryReport(self):
        with open('DamagedInventory.csv', 'w') as file:
            sorted_items = sorted(items.values(), key=lambda v: v.item_price, reverse=True)
            for i in sorted_items:
                if i.damage == 'damaged': # if function checks if item had been damedged if so it adds it to file
                    file.write(f'{i.item_id},{i.manufacturer_name},{i.item_type},{i.item_price},{i.get_service_date()}\n')


if __name__ == '__main__':  # program starts running
    items = {} # main dictionary
    with open('ManufacturerList.csv') as file:
        csvfile = csv.reader(file)
        for line in csvfile:
            item = Item(line[0], line[1], line[2], damage=line[3]) # pulls out information from file id, manuc, and item type
            items[line[0]] = item

    with open('PriceList.csv') as file:
        csvfile = csv.reader(file)
        for line in csvfile:
            items[line[0]].item_price = line[1]

    with open('ServiceDatesList.csv') as file:
        csvfile = csv.reader(file)
        for line in csvfile:
            items[line[0]].service_date = datetime.strptime(line[1], '%m/%d/%Y').date()

#below these call all the functions in the class
    inventory = Inventory(items)
    inventory.fullInventoryReport()
    inventory.itemInventoryReports()
    inventory.pastServiceInventoryReport()
    inventory.damageInventoryReport()
