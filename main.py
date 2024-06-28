import os

# Current title, color, and options stored within the script
current_title = "made by ynb21"
current_color = "4"
menu_options = [
    "enter in 37834 to change title color etc",
]

def print_art():
    print("YYYYYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNBBBBBBBBBBBBBBBBBBBBB")
    print("Y:::::Y       Y:::::YN:::::::N       N::::::NB::::::::::::::::BB B") 
    print("Y:::::Y       Y:::::YN::::::::N      N::::::NB::::::BBBBBB:::::B B") 
    print("Y::::::Y     Y::::::YN:::::::::N     N::::::NBB:::::B     B:::::BB")
    print("YYY:::::Y   Y:::::YYYN::::::::::N    N::::::N  B::::B     B:::::BB")
    print("Y  Y:::::Y Y:::::Y   N:::::::::::N   N::::::N  B::::B     B:::::BB")
    print("Y   Y:::::Y:::::Y    N:::::::N::::N  N::::::N  B::::BBBBBB:::::B B") 
    print("Y    Y:::::::::Y     N::::::N N::::N N::::::N  B:::::::::::::BB  B")
    print("Y     Y:::::::Y      N::::::N  N::::N:::::::N  B::::BBBBBB:::::B B") 
    print("Y     Y:::::Y       N::::::N   N:::::::::::N  B::::B     B:::::BBB")
    print("Y      Y:::::Y       N::::::N    N::::::::::N  B::::B     B:::::BB")
    print("Y      Y:::::Y       N::::::N     N:::::::::N  B::::B     B:::::BB")
    print("Y      Y:::::Y       N::::::N      N::::::::NBB:::::BBBBBB::::::BB")
    print("Y   YYYY:::::YYYY    N::::::N       N:::::::NB:::::::::::::::::B B") 
    print("Y   Y:::::::::::Y    N::::::N        N::::::NB::::::::::::::::BB B") 
    print("YYYYYYYYYYYYYYYYYYNNNNNNNNNNNNNNNNNNNNNNNNNNNNBBBBBBBBBBBBBBBBBBBBB")

def show_menu():
    print()
    print("Made by ynb21 (discord), socials: https://guns.lol/gangbang")
    for i, option in enumerate(menu_options, start=1):
        print(f"{i}) {option}")
    print()

def main():
    global current_title, current_color, menu_options
    os.system('mode con: cols=130 lines=35')  # Sets the console size
    os.system(f'title {current_title}')  # Sets the title
    os.system(f'color {current_color}')  # Sets the color

    print_art()
    show_menu()
    
    user_input = input("Choose: ")
    if user_input == "37834":
        new_title = input("What should the title be? ")
        os.system(f'title {new_title}')  # Sets the new title
        current_title = new_title

        new_color = input("What should the color be? (Enter a single digit for the color code) ")
        os.system(f'color {new_color}')  # Sets the new color
        current_color = new_color

        num_options = int(input("How many menu options? "))
        new_menu_options = []
        for i in range(1, num_options + 1):
            option_text = input(f"Enter text for option {i}: ")
            new_menu_options.append(option_text)
        menu_options = new_menu_options

        update_script(new_title, new_color, new_menu_options)
    
    input("Press Enter to exit...")  # Keeps the console window open

def update_script(new_title, new_color, new_menu_options):
    try:
        with open(__file__, 'r') as file:
            lines = file.readlines()
        
        with open(__file__, 'w') as file:
            in_menu_options = False
            for line in lines:
                if line.startswith("current_title ="):
                    file.write(f'current_title = "{new_title}"\n')
                elif line.startswith("current_color ="):
                    file.write(f'current_color = "{new_color}"\n')
                elif line.startswith("menu_options ="):
                    file.write('menu_options = [\n')
                    for option in new_menu_options:
                        file.write(f'    "{option}",\n')
                    file.write(']\n')
                    in_menu_options = True
                elif in_menu_options:
                    if line.strip() == "]":
                        in_menu_options = False
                    continue
                else:
                    file.write(line)
        print("Script updated successfully.")
    except Exception as e:
        print(f"An error occurred while updating the script: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")
