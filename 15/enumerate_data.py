names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()
NAME_WIDTH = 11


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""

    for idx, (name, country) in enumerate(zip(names, countries), start=1):
        print(f"{idx}. {name:<{NAME_WIDTH}}{country}")
