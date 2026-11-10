from pyscript import document, display

# Elements
# Dictionary with information about Elements
# Element Name: symbol, atomic number, atomic weight

nonmetals = {
    "Hydrogen": ("a", 2, 3),
    "Helium": ("a", 2, 3),
    "Carbon": ("a", 2, 3),
    "Nitrogen": ("a", 2, 3),
    "Oxygen": ("a", 2, 3),
    "Fluorine": ("a", 2, 3),
    "Neon": ("a", 2, 3),
    "Phosphorus": ("a", 2, 3),
    "Sulfur": ("a", 2, 3),
    "Chlorine": ("a", 2, 3),
    "Argon": ("a", 2, 3),
    "Selenium": ("a", 2, 3),
    "Bromine": ("a", 2, 3),
    "Krypton": ("a", 2, 3),
    "Iodine": ("a", 2, 3),
    "Xenon": ("a", 2, 3),
    "Radon": ("a", 2, 3)
}

# Function in searching for an element

def search_element(e):
    # Get the imput from HTML
    Planet1 = document.getElementById("planet1").value
    # Retrieve information from the dictionary
    result = nonmetals.get(Planet1, ("Planet not found", "-", "-"))
    # Display of result
    document.getElementById("code").innerText = Planet1
    document.getElementById("name").innerText = result[0]
    document.getElementById("order").innerText = result[1]
    document.getElementById("moons").innerText = result[2]