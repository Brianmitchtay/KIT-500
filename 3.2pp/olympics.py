"""
3.2PP Fill in the Blanks: Paris Olympics
"""

__author__ = "Brian Taylor"


def main():
    print("2024 Olympic headline generator")

    first_place: str = input("Enter the name of the country with the most gold medals currently : ")
    capital_city: str = input("What's the capital city of the country that's got the most gold medals? : ")
    second_place: str = input("Enter the name of the country in with the second most gold medals: ")
    gold_medals_1: int = int(input("How many gold medals has the first-placed country won? : "))
    gold_medals_2: int = int(input("How many gold medals has the second-placed country won? "))
    margin: int = gold_medals_1 - gold_medals_2

    print(f"{first_place} currently tops the 2024 Paris Olympics' medal tally with {gold_medals_1} gold.\nCitizens of {capital_city} are overjoyed at beating arch-rivals {second_place}. \nTheir lead of {margin} gold looks secure with only competitive programming left.")



if __name__ == "__main__":
    main()