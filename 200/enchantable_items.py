from pathlib import Path
from urllib.request import urlretrieve
import re

from bs4 import BeautifulSoup as Soup
from collections import defaultdict

out_dir = "/tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"


class Enchantment:
    """Minecraft enchantment class
    
    Implements the following: 
        id_name, name, max_level, description, items
    """

    def __init__(self, id_name, name, max_level, description, items=None):
        self.id_name = id_name
        self.name = name
        self.max_level = max_level
        self.description = description
        self.items = items or []

    def __str__(self):
        return f"{self.name.title()} ({self.max_level}): {self.description}"


class Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """

    def __init__(self, name, enchantments=None):
        self.name = name
        self.enchantments = enchantments or []

    def __str__(self):
        name = self.name.title().replace("_", " ")
        enchantments_str = ""
        for enchantment in sorted(self.enchantments, key=lambda x: x.id_name):
            max_level = enchantment.max_level
            id_name = enchantment.id_name
            enchantments_str += f"\n  [{max_level}] {id_name}"
        return f"{name}: {enchantments_str}"


def roman_to_int(input):
    """ Convert a Roman numeral to integer """
    if not isinstance(input, str):
        raise TypeError(f"Expected string, got {type(input)}")

    input = input.upper()
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sum = 0

    for i, _ in enumerate(input):
        try:
            value = nums[input[i]]
            if i + 1 < len(input) and nums[input[i+1]] > value:
                sum -= value
            else:
                sum += value
        except KeyError:
            raise ValueError("Not a valid Roman numeral")
    return sum


def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """
    enchantments_soup = soup.select('tr:nth-of-type(n+2)')
    enchantments = {}

    for data in enchantments_soup:
        name, id_name, _ = re.split(r"\(|\)", data.select_one('td:nth-of-type(1)').get_text())
        max_level = roman_to_int(data.select_one('td:nth-of-type(2)').get_text())
        description = data.select_one('td:nth-of-type(3)').get_text()
        enchantments[id_name] = Enchantment(id_name, name, max_level, description)
        img = data.select_one("img")
        url = img['data-src']
        url = url.split("/")[3] 
        for thing in {".", "_", "enchanted", "iron", "png", "sm"}:
            url = url.replace(thing, " ")
        url = url.strip()
        enchantments[id_name].items = []
        for item in url.split():
            if item == "fishing":
                enchantments[id_name].items.append("fishing_rod")
                break
            else:
                enchantments[id_name].items.append(item)

    return enchantments


def generate_items(data):
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """
    items = []
    for enchantment in data.values():
        for thing in enchantment.items:
            item = Item(thing)
            items.append(item)

    for enchantment in data.values():
        for thing in enchantment.items:
            for item in items:
                if thing == item.name:
                    item.enchantments.append(enchantment)

    result = {}
    for item in items:
        result[item.name] = item

    return result


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not HTML_FILE.is_file():
            urlretrieve(URL, HTML_FILE)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def main():
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()
    pass

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""