class Door():

    def __init__(self, is_opened):
        self.is_opened = is_opened

    def open_door(self):
        self.is_opened = True
        print("The dor is open")

    def open_door(self):
        self.is_opened = False
        print("The dor is close")

class BlockedDoor(Door):

    def open_door(self):
        raise Exception("BlockedDoor can't be open")
      
    def close_door(self):
        raise Exception("BlockedDoor can't be open")  
    

new_door = Door(True)
new_door.open_door()
new_door.close_door()

print()