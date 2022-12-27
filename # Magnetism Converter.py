# Magnetic Field Strength Converter

# Welcome to message
print("Welcome to your Magnetic Field Strength Converter")

# List of conversion types
# ampere/meter
# ampere turn/meter 
# kiloampere/meter
# oersted 

# Conversation for each unit type 
conversion = {
    "ampere meter": {
        "ampere turn" : 1,
        "kiloampere" : 0.001,
        "orsted" : 0.0125663706,
    },
    "ampere turn" : {
        "ampere meter" : 1,
        "kiloampere": 0.001,
        "orsted" : 0.0125663706,
    },
    "kiloampere": {
        "ampere meter" : 1,
        "ampere turn" : 1,
        "orsted" : 1,
    },
    "orsted":{
        "ampere meter" : 1,
        "ampere turn" : 1,
        "kiloampere" : 1,        
    }
}

while True:
    
    question = input("Would you like to convert a unit? y/n :")

    if question == 'y':
        print()
        # The users chooses the inital unit type
        initial_unit = (input("""What type of unit would you like to convert? 
        type the number of the following unit type:
        1 - Ampere Meter AM - Type as ampere meter
        2 - Ampere Turn Meter KAM - Type as ampere turn
        3 - Kiloampere Meter KAM - Type as kiloampere
        4 - Orsted OE - Type as orsted
        Please type lowercase: """))

        # The users chooses what they would like the initial unit to convert into
        unit_conversion = (input(f"""What what tould you like to convert {initial_unit} into? 
        1 - Ampere Meter AM - Type as ampere meter
        2 - Ampere Turn Meter KAM - Type as ampere turn
        3 - Kiloampere Meter KAM - Type as kiloampere
        4 - Orsted OE - Type as orsted
        Please type lowercase: """))

        # Request the amount the user would like to conver - Example 1 ampere meter into a oersted
        value_converter = float(input(f"How many {initial_unit}(s) would you like to convert?"))

        # It takes the amount of initial units and * the amount into the preffered unit
        converted_value = value_converter * conversion[initial_unit][unit_conversion]

        print(f" Your conversion {converted_value}")
        
    elif question == 'n':
        print("Ahh ok, you can convert a unit when you are ready")
    else:
        break
