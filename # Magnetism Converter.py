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
    "ampere_meter_AM": {
        "ampere_turn_meter_ATM" : 1,
        "kiloampere_meter_KAM" : 0.001,
        "oersted_OE" : 0.0125663706,
    },
    "ampere_turn_meter_ATM" : {
        "ampere_meter_AM" : 1,
        "kiloampere_meter_KAM": 0.001,
        "oersted_OE" : 0.0125663706,
    },
    "kiloampere_meter_KAM": {
        "ampere_meter_AM" : 1,
        "ampere_turn_meter_ATM" : 1,
        "oersted_OE" : 1,
    },
    "oersted_OE":{
        "ampere_meter_AM" : 1,
        "ampere_turn_meter_ATM" : 1,
        "kiloampere_meter_KAM" : 1,        
    }
}

# The users chooses the inital unit type
unit_type = int(input("""What type of unit would you like to convert? 
type the number of the following unit type:
1 - Ampere Meter AM
2 - Ampere Turn Meter KAM
3 - Kiloampere Meter KAM
4 - Orsted OE
Please select a number from 1 - 4 : """))

# The users chooses what they would like the initial unit to convert into
unit_conversion = int(input(f"""What what tould you like to convert {unit_type} into? 
1 - Ampere Meter AM
2 - Ampere Turn Meter KAM
3 - Kiloampere Meter KAM
4 - Orsted OE
Please select a number from 1 - 4 : """))