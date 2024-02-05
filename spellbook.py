from typing import Any
import requests
spellbook_url = "https://www.dnd5eapi.co/api/spells/"

class InvalidSpellName(Exception):
    pass


class Spell:
    def __init__(self, name):
        self.name = name

        self.url = spellbook_url + self.name
        response = requests.get(self.url)
        spells_data = response.json()

        self.desc = spells_data['desc']
        self.higher_level = spells_data['higher_level']
        self.components = spells_data['components']
        self.material = spells_data['material']
        self.ritual = spells_data['ritual']
        self.duration = spells_data['duration']
        self.concentration = spells_data['concentration']
        self.casting_time = spells_data['casting_time']
        self.level = spells_data['level']
        self.attack_type = spells_data['attack_type']
        self.damage = spells_data['damage']
        #self.damage_at_slot_level = spells_data['damage_at_slot_level']
        self.school = spells_data['school']
        self.classes = spells_data['classes']
        self.subclasses = spells_data['subclasses']
        self.range = spells_data['range']

            


    def getName(self) -> str:
        return str(self.name)
    
    def getDesc(self) -> str:
        return self.desc
    
    def getHigherLevel(self) -> str:
        return self.higher_level
    
    def getRange(self) -> int:
        temp = str(self.range)
        temp = temp.replace(' feet', '')
        return int(temp)
    
    def getComponents(self) -> list[str]:
        return self.components
    



if __name__ == '__main__':
    sp1 = Spell('acid-arrow')
    print(f"Name: {sp1.getName()}, Range: {sp1.getRange()}")