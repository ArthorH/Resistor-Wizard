#I WELCOME YOU INTERNET SURFER INTO MY 

#  /$$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$                       
# | $$__  $$| $$_____/ /$$__  $$|_  $$_/ /$$__  $$|__  $$__//$$__  $$| $$__  $$                     
# | $$  \ $$| $$      | $$  \__/  | $$  | $$  \__/   | $$  | $$  \ $$| $$  \ $$                   
# | $$$$$$$/| $$$$$   |  $$$$$$   | $$  |  $$$$$$    | $$  | $$  | $$| $$$$$$$/                      
# | $$__  $$| $$__/    \____  $$  | $$   \____  $$   | $$  | $$  | $$| $$__  $$                          
# | $$  \ $$| $$       /$$  \ $$  | $$   /$$  \ $$   | $$  | $$  | $$| $$  \ $$              
# | $$  | $$| $$$$$$$$|  $$$$$$/ /$$$$$$|  $$$$$$/   | $$  |  $$$$$$/| $$  | $$                    
# |__/  |__/|________/ \______/ |______/ \______/    |__/   \______/ |__/  |__/  
#                                                                                                                                                                              
#                                     ....
#                                  .'' .'''
#  .                             .'   :
#  \\                          .:    :
#   \\                        _:    :       ..----.._
#    \\                    .:::.....:::.. .'         ''.
#     \\                 .'  #-. .-######'     #        '.
#      \\                 '.##'/ ' ################       :
#       \\                  #####################         :
#        \\               ..##.-.#### .''''###'.._        :
#         \\             :--:########:            '.    .' :
#          \\..__...--.. :--:#######.'   '.         '.     :
#          :     :  : : '':'-:'':'::        .         '.  .'
#          '---'''..: :    ':    '..'''.      '.        :'
#             \\  :: : :     '      ''''''.     '.      .:
#              \\ ::  : :     '            '.      '      :
#               \\::   : :           ....' ..:       '     '.
#                \\::  : :    .....####\\ .~~.:.             :
#                 \\':.:.:.:'#########.===. ~ |.'-.   . '''.. :
#                  \\    .'  ########## \ \ _.' '. '-.       '''.
#                  :\\  :     ########   \ \      '.  '-.        :
#                 :  \\'    '   #### :    \ \      :.    '-.      :
#                :  .'\\   :'  :     :     \ \       :      '-.    :
#               : .'  .\\  '  :      :     :\ \       :        '.   :
#               ::   :  \\'  :.      :     : \ \      :          '. :
#               ::. :    \\  : :      :    ;  \ \     :           '.:
#                : ':    '\\ :  :     :     :  \:\     :        ..'
#                   :    ' \\ :        :     ;  \|      :   .'''
#                   '.   '  \\:                         :.''
#                    .:..... \\:       :            ..''
#                   '._____|'.\\......'''''''.:..'''
#                              \\                                                                                                                                                                                                                                                                                                                   
#
#       __   __   ______     __         __  __     ______     ______                                    
#      /\ \ / /  /\  __ \   /\ \       /\ \/\ \   /\  ___\   /\  ___\                                   
#      \ \ \'/   \ \  __ \  \ \ \____  \ \ \_\ \  \ \  __\   \ \___  \                                  
#       \ \__|    \ \_\ \_\  \ \_____\  \ \_____\  \ \_____\  \/\_____\                                 
#        \/_/      \/_/\/_/   \/_____/   \/_____/   \/_____/   \/_____/                                 
#                                                                                                 
#       __     __     __     ______     ______     ______     _____   
#      /\ \  _ \ \   /\ \   /\___  \   /\  __ \   /\  == \   /\  __-. 
#      \ \ \/ ".\ \  \ \ \  \/_/  /__  \ \  __ \  \ \  __<   \ \ \/\ \
#       \ \__/".~\_\  \ \_\   /\_____\  \ \_\ \_\  \ \_\ \_\  \ \____-
#        \/_/   \/_/   \/_/   \/_____/   \/_/\/_/   \/_/ /_/   \/____/


from itertools import product, permutations, combinations
import eia
import numpy as np

vref = 1.25

def calc_vout(r1, r2):
	return vref*(1+(((r2)/(r1))))

best_distance = float('inf')

#some chat GPT standard stuff ... life is too short to write it manually 

def generate_combinations_with_replacement_and_shuffle(items, n):
    # Generate all possible combinations of size n with replacement
    comb_with_replacement = product(items, repeat=n)
    
    # Create a set to store unique permutations (shuffled combinations)
    unique_permutations = set()
    
    # For each combination with replacement, generate all permutations
    for comb in comb_with_replacement:
        perm = permutations(comb)
        for p in perm:
            unique_permutations.add(p)
    
    # Convert the set of unique permutations to a list of lists
    result = [list(p) for p in unique_permutations]
    return result

def generate_all_combinations(items):
    all_combinations = []
    
    # Generate combinations for all possible sizes
    for size in range(1, len(items) + 1):
        comb = combinations(items, size)
        # Convert combinations to a list of lists and add to the result
        all_combinations.extend([list(c) for c in comb])
    
    return all_combinations

def calculate_parallel_resistance(resistors):
    if not resistors:
        raise ValueError("The list of resistors must not be empty.")
    
    # Compute the reciprocal of the equivalent resistance
    reciprocal_sum = sum(1 / r for r in resistors)
    
    # Compute the equivalent resistance
    if reciprocal_sum == 0:
        raise ValueError("The sum of reciprocals of resistances must not be zero.")
    
    equivalent_resistance = 1 / reciprocal_sum
    return equivalent_resistance

def generate_all_permutations(arr):
    # Generate all permutations of the array
    perm = permutations(arr)
    
    # Convert permutations to a list of lists
    perm_list = [list(p) for p in perm]
    return np.array(perm_list)

def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return float('inf')

#User menu 

print("#       __   __   ______     __         __  __     ______     ______                                    ")
print("#      /\\ \\ / /  /\\  __ \\   /\\ \\       /\\ \\/\\ \\   /\\  ___\\   /\\  ___\\                                   ")
print("#      \\ \\ \\'/   \\ \\  __ \\  \\ \\ \\____  \\ \\ \\_\\ \\  \\ \\  __\\   \\ \\___  \\                                  ")
print("#       \\ \\__|    \\ \\_\\ \\_\\  \\ \\_____\\  \\ \\_____\\  \\ \\_____\\  \\/_____\\                                 ")
print("#        \\/_/      \\/_/\\/_/   \\/_____/   \\/_____/   \\/_____/   \\/_____/                                 ")
print("#                                                                                                  ")
print("#       __     __     __     ______     ______     ______     _____                                 ")
print("#      /\\ \\  _ \\ \\   /\\ \\   /\\___  \\   /\\  __ \\   /\\  == \\   /\\  __-.                               ")
print("#      \\ \\ \\/ \".\\ \\  \\ \\ \\  \\/_/  /__  \\ \\  __ \\  \\ \\  __<   \\ \\ \\/\\ \\                              ")
print("#       \\ \\__/\".~\\_\\  \\ \\_\\   /\\_____\\  \\ \\_\\ \\_\\  \\ \\_\\ \\_\\  \\ \\____-                                ")
print("#        \\/_/   \\/_/   \\/_/   \\/_____/   \\/_/\\/_/   \\/_/ /_/   \\/____/                                ")


#resistor_ammount = 4
#expected_voltages_list = [12,18,22,29,34,36,42]
resistor_ammount = 3
expected_voltages_list = [12,29,42]
print("==================================================================================")
print("                 .----------------------.")
print("                 |                      |")
print("          VIN o---------   - -----------|---o--------------o  VOUT")
print("                 |      \\ ^             |   |")
print("                 |      ---             |  .-.")
print("                 |       |              |  |R|")
print("                 |       |              |  |1|")
print("                 |       |              |  '-'")
print("                 |       |      /|      |   |")
print("                 |       |     /+|- ----|---o------o------o")
print("                 |       |----<  |      |   |      |      |")
print("                 |             \\-|- |   |  .-.    .-.    .-.")
print("                 |              \\|  |   |  |R|    |R|    |R|")
print("                 |                  |   |  |2|    |3|    |4|")
print("                 |       .--------. |   |  '-'    '-'    '-'")
print("                 |       |  VREF  |-|   |   |      |      |")
print("                 |       '--------'     |   |      |      |")
print("                 |                      |   |    |/     |/")
print("                 '-----------o----------'   |  o-|    o-|")
print("                             |              |    |>     |>")
print("                             |              |      |      |")
print("                             |              |      |      |")
print("                             |              |      |      |")
print("                            ---            ---    ---    ---")
print("==================================================================================")
print("Type voltage stabilizer VREF in [V]:")
vref = float(input("Vref in [V] : "))
print("==================================================================================")
print("Select value set:")
print("1. E3")
print("2. E6")
print("3. E12")
print("4. E24")
print("5. E48")
print("6. E98")
correct_selection = False
while correct_selection == False:
    value_set_select = int(input("Select value set: "))
    match value_set_select:
        case 1:
            value_set = eia.E3
            correct_selection = True
        case 2:
            value_set = eia.E6
            correct_selection = True
        case 3:
            value_set = eia.E12
            correct_selection = True
        case 4:
            value_set = eia.E24
            correct_selection = True
        case 5:
            value_set = eia.E48
            correct_selection = True
        case 6:
            value_set = eia.E96
            correct_selection = True
        case _:
            print("user error >:(  ... choose from 1 to 6")

value_setx10 = [round(i * 10,2) for i in value_set]
#value_setx100 = [round(i * 100.0,4) for i in eia.E48]
value_set = np.append(value_set, value_setx10)
print("=================================== OK ===========================================")

correct_selection = False
while correct_selection == False:
    resistor_ammount = int(input("Resistor ammount (3 or 4): "))
    match resistor_ammount:
        case 3:
             desired_voltages_ammount = 3
             correct_selection = True
        case 4:
             desired_voltages_ammount = 7
             correct_selection = True
        case _:
            print("inacurate ammount >:(  ... choose 3 or 4")

print("=================================== OK ===========================================")

# Initialize an empty array to store the expected voltages
expected_voltages_list = []
print("INPUT EXPECTED VOLTAGES")
print("From most to least significant")
# Loop to get 'n' values from the user
for i in range(desired_voltages_ammount):
    value = float(input(f"Enter expected voltage no. {i+1}: "))
    expected_voltages_list.append(value)
print("=================================== OK ===========================================")
best_decade_values = []
best_voltages = []

max_voltage = max(expected_voltages_list)
min_voltage = min(expected_voltages_list)

all_resistor_values_permutations_list = generate_combinations_with_replacement_and_shuffle(value_set, resistor_ammount-1)

#generate all permutations of voltages
#all_permutations_of_expected_voltages = generate_all_permutations(expected_voltages_list)    # generate all possible permutations of voltages

voltages_checksum = 1
temp_val_exp_checksum = expected_voltages_list[0]
temp_diff_exp = 1


for possible_R1_values in value_set:
    R1 = possible_R1_values
    #print("=========================== CHECKING R1 VALUES ===========================")
    #print("Checknig \"R1\": " + str(R1))
    #print("==========================================================================")
    for all_possible_permutations in all_resistor_values_permutations_list:        # calculate all combinations of all permutations of resistors
        all_combinations_of_permutation = generate_all_combinations(all_possible_permutations)
        #print(all_possible_permutations)
        output_voltages_list = []
    # for all i know this segment generates all possible resistor combinations (meaning every resistor array for E24 or whatever) and then it does
    #calculate output voltages according to formula for all possible switches combinations and then outputs it in array
        for switch_combination in all_combinations_of_permutation:                 # calculate all switch combinations for all resistors
           if len(switch_combination) < 2:
               eq_resistance = int(switch_combination[0])                                #if current combination does not contain 2 or more resistors than skip parralel resistance calculation
           else:
               eq_resistance = calculate_parallel_resistance(switch_combination)
           output_voltages_list = np.append(output_voltages_list,round(calc_vout(R1, eq_resistance),4))   #write all voltages to array 
    # this code takes those voltages values and compares them to expected voltages. 
    # user voltages and output voltages that had been calculated may be shuffled so in order to not compare unrelated values code generates 
    # permutations of all USER_INPUT VALUES to save time a little. And then compares those values to user expected value
        if (min(output_voltages_list) >= min_voltage-(min_voltage*0.05)): #check weather divider does not go out of bounds
            if (max(output_voltages_list) <= max_voltage+(max_voltage*0.05)):
                #Generate all permutations of output voltages
                all_permutations_output_voltages = generate_all_permutations(output_voltages_list) 
                #print("Found combination within tolerances "+ str(output_voltages_list) + " : checking for similarity")
                for permutations_of_output_voltages in all_permutations_output_voltages :
                    #distance calculation
                    dist = 1
                    prev_voltage1 = permutations_of_output_voltages[1]
                    prev_voltage2 = expected_voltages_list[1]
                    it = 0 
                    for single_voltages in expected_voltages_list:
                        dist = round(dist + it*get_change(prev_voltage1, prev_voltage2),2)
                        if dist > best_distance:
                            break
                        prev_voltage1 = single_voltages
                        prev_voltage2 = permutations_of_output_voltages[it]
                    #    print("dist1:" + str(dist1) )
                        it = it + 1
                    
                    #it = 0
#                    for single_voltages_in_permutations in permutations_of_voltages:
#                        dist2 = dist2 * get_change(prev_voltage2, single_voltages_in_permutations)
#                        prev_voltage2 = single_voltages_in_permutations
                    #    print("dist2:" + str(dist2) )
#                        it = it + 1
                    #dist = np.linalg.norm(permutations_of_voltages - np.array(expected_voltages_list))
                    if (best_distance >= dist):
                        best_distance = dist
                        best_decade_values = all_possible_permutations
                        best_voltages = permutations_of_output_voltages
                        expedted_voltages_permutation = expected_voltages_list
                        R1_best_value = R1
                        print("==================== FOUND EVEN BETTER COMBINATION ========================")
                        print("new best distance " + str(dist))
                        print("for voltages " + str(dist))
                        print("With \"R1\" resistor values: " + str(R1_best_value))
                        print("With \"R2\" resistor values: " + str(best_decade_values))
                        print("For desired voltages   : " + str(expedted_voltages_permutation ))
                        print("Closest i could get is : " + str(best_voltages))
                        print("==========================================================================")
#Wizard by Shanaka Dias



print("==========================  WIZARD FINISHED ==============================")
print("     __/\\__       ________ ___  ________      ")
print(". _  \\\\'//       |\\  _____\\  \\|\\   ___  \\    ")
print("-( )-/_||_\\      \\ \\  \\__/\\ \\  \\ \\  \\ \\  \\   ")
print(" .'. \\_()_/       \\ \\   __\\\\ \\  \\ \\  \\ \\  \\  ")
print("  |   | . \\        \\ \\  \\_| \\ \\  \\ \\  \\ \\  \\ ")
print("  |mrf| .  \\        \\ \\__\\   \\ \\__\\ \\__\\\\ \\__\\")
print(" .'. ,\\_____'.       \\|__|    \\|__|\\|__| \\|__|")
print("                            ")
print("================           BEST COMBINATION         =====================")
print("For desired voltages: " + str(expected_voltages_list))
print("Closest i could get is:" + str(best_voltages))
print("With \"R1\" resistor values: " + str(R1_best_value))
print("With \"R2\" resistor values: " + str(best_decade_values))
print("==========================================================================")
print("==================================================================================")
print("                 .----------------------.")
print("                 |                      |")
print("          VIN o---------   - -----------|---o--------------o  VOUT")
print("                 |      \\ ^             |   |")
print("                 |      ---             |  .-.")
print("                 |       |              |  |R|")
print("                 |       |              |  |1|")
print("                 |       |              |  '-'")
print("                 |       |      /|      |   |")
print("                 |       |     /+|- ----|---o------o------o")
print("                 |       |----<  |      |   |      |      |")
print("                 |             \\-|- |   |  .-.    .-.    .-.")
print("                 |              \\|  |   |  |R|    |R|    |R|")
print("                 |                  |   |  |2|    |3|    |4|")
print("                 |       .--------. |   |  '-'    '-'    '-'")
print("                 |       |  VREF  |-|   |   |      |      |")
print("                 |       '--------'     |   |      |      |")
print("                 |                      |   |    |/     |/")
print("                 '-----------o----------'   |  o-|    o-|")
print("                             |              |    |>     |>")
print("                             |              |      |      |")
print("                             |              |      |      |")
print("                             |              |      |      |")
print("                            ---            ---    ---    ---")
print("==================================================================================")
#                         Artem Horiunov 08-2024