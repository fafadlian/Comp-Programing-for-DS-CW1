import json
import csv


class CountryMedals:
    def __init__(self, name, gold, silver, bronze, total):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
        self.total = total

    def to_dict(self):
        country_dict = {
            'name': self.name,
            'gold': self.gold,
            'silver': self.silver,
            'bronze': self.bronze,
            'total': self.total
        }
        return country_dict

    def to_json(self):
        country_dict = self.to_ditc()
        country_json = json.dumps(country_dict, indent=4)
        return country_json
    
    def get_medals(self, medal_type):
        if medal_type == "gold":
            return self.gold
        elif medal_type == "silver":
            return self.silver
        elif medal_type == "bronze":
            return self.bronze
        elif medal_type == "total":
            return self.total
        else:
            return None
        
    def print_summary(self):
        print(f"{self.name} received {self.total} medals in total; {self.gold} gold, {self.silver} silver, and {self.bronze} bronze.")

    
    
def get_sorted_country_names(countries):
    return sorted(countries.keys())

def parse_medals(filename):
    countries = {}
    with open(filename, 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        # next(csv_reader)  # Skip the header row 
        for row in csv_reader:
            name = row['Team/NOC']
            gold = int(row['Gold'])
            silver = int(row['Silver'])
            bronze = int(row['Bronze'])
            total = int(row['Total'])
            country = CountryMedals(name, int(gold), int(silver), int(bronze), int(total))
            countries[name] = country
    return countries

def get_sorted_country_names(countries):
    return sorted(countries.keys())

def sort_countries_by_medal_type_ascending(countries, medal_type):
    return sorted(countries.values(), key=lambda x: getattr(x, medal_type))

def sort_countries_by_medal_type_descending(countries, medal_type):
    return sorted(countries.values(), key=lambda x: getattr(x, medal_type), reverse=True)

def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive integer (0 or greater).")
        except ValueError:
            print("Please enter a valid positive integer.")

def read_country_name(countries, prompt):
    while True:
        country_name = input(prompt)
        if country_name in countries:
            return country_name
        else:
            print("Country not found. Choose from the following countries:")
            for country in countries:
                print(country)

def read_medal_type(prompt):
    valid_medal_types = ["gold", "silver", "bronze", "total"]
    while True:
        medal_type = input(prompt)
        if medal_type in valid_medal_types:
            return medal_type
        else:
            print("Invalid medal type. Please choose from 'gold', 'silver', 'bronze', or 'total'.")

def print_help():
    print("Available Commands:")
    print("  H/h (Help): Print available commands and their descriptions.")
    print("  L/l (List): List the countries present in the dataset.")
    print("  S/s (Sort): Sort countries by a specific medal type in ascending or descending order.")
    print("  C/c (Compare): Compare medals of two countries.")
    print("  Q/q (Quit): Quit the program.")

def list_countries_with_more_medals_than_threshold(countries, medal_type, threshold):
    filtered_countries = [country for country in countries.values() if getattr(country, medal_type) > threshold]
    return filtered_countries


#Program Loop
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
        elif user_input in ['m', 'more']:
            medal_type = read_medal_type('Insert the medal type (gold, silver, bronze): ')
            threshold = read_positive_integer('Insert medal threshold: ')
            filtered_countries = [country for country in data.values() if getattr(country, medal_type) > threshold]
            print(filtered_countries)

        else:
            print("Invalid command. Type 'H' or 'h' for help.")

    