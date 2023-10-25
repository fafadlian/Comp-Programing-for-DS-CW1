from medals import CountryMedals, parse_medals, get_sorted_country_names, print_help
import csv

fileName = 'Act1/medals.csv'

if __name__ == '__main__':
    data = parse_medals(fileName)

    print('The program has started.')
    print('Insert your next command (H for help):')
    terminated = False

    while True:

        user_input = input('Insert a command: ').strip().lower()


        if user_input in ['h', 'help']:
            print_help()

        elif user_input in ['q', 'quit']:
            print("Exiting the program.")
            break
        else:
            print("Invalid command. Type 'H' or 'h' for help.")

# italy = data.get("Italy")
# print(italy)
# if italy:
#     italy.print_summary()


# sorted_country_names = get_sorted_country_names(data)
# print("List of Countries:")
# for name in sorted_country_names:
#     print(name)