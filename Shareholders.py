class Apartment:
    def __init__(self, apartment_type, apartment_name, shares):
        self.apartment_type = apartment_type  # 'sponsor' or 'shareholder'
        self.apartment_name = apartment_name  # e.g., '1A', '2B', etc.
        self.shares = shares  # Number of shares for the apartment

    def __repr__(self):
        return f"{self.apartment_type.capitalize()} {self.apartment_name} (Shares: {self.shares})"


def outrank_sponsor_apartments(sponsor_apartments, shareholder_apartments, outrank_count):
    """
    This function simulates outranking a set number of sponsor apartments
    by shareholder apartments based on the number of shares.

    Args:
    - sponsor_apartments (list): List of sponsor apartment objects.
    - shareholder_apartments (list): List of shareholder apartment objects.
    - outrank_count (int): Number of sponsor apartments to be outranked.

    Returns:
    - list: Updated list of apartments after outranking.
    """
    # Check that the outrank count is not more than the number of sponsor apartments
    if outrank_count > len(sponsor_apartments):
        raise ValueError("Outrank count cannot be more than the number of sponsor apartments.")

    # Sort shareholder apartments by the number of shares in descending order
    sorted_shareholders = sorted(shareholder_apartments, key=lambda x: x.shares, reverse=True)

    # "Outrank" the sponsor apartments by placing the shareholder apartments before them
    outranked_sponsor_apartments = sorted_shareholders[:outrank_count]
    remaining_shareholders = sorted_shareholders[outrank_count:]

    # Create a new list where outranked shareholder apartments are placed ahead of sponsor apartments
    updated_apartments = outranked_sponsor_apartments + sponsor_apartments[outrank_count:] + remaining_shareholders
    return updated_apartments


# Example usage:

# Sponsor apartments
sponsors = [
    Apartment("sponsor", "1A", shares=1000),
    Apartment("sponsor", "1D", shares=1010),
    Apartment("sponsor", "1L", shares=1020),
    Apartment("sponsor", "2B", shares=1030),
    Apartment("sponsor", "2E", shares=1040),
    Apartment("sponsor", "2G", shares=1050),
    Apartment("sponsor", "3D", shares=1060),
    Apartment("sponsor", "3E", shares=1070),
    Apartment("sponsor", "3G", shares=1080),
    Apartment("sponsor", "4B", shares=1090),
    Apartment("sponsor", "4D", shares=1100),
    Apartment("sponsor", "4J", shares=1110),
    Apartment("sponsor", "5E", shares=1120),
    Apartment("sponsor", "5H", shares=1130),
    Apartment("sponsor", "6K", shares=1140),
    Apartment("sponsor", "7F", shares=1150),
]

# Shareholder apartments
shareholders = [
    Apartment("shareholder", "1B", shares=510),
    Apartment("shareholder", "1E", shares=520),
    Apartment("shareholder", "1F", shares=530),
    Apartment("shareholder", "1G", shares=540),
    Apartment("shareholder", "1H", shares=550),
    Apartment("shareholder", "1J", shares=570),
    Apartment("shareholder", "1K", shares=580),
    Apartment("shareholder", "2A", shares=590),
    Apartment("shareholder", "2C", shares=600),
    Apartment("shareholder", "2D", shares=610),
    Apartment("shareholder", "2F", shares=620),
    Apartment("shareholder", "2H", shares=630),
    Apartment("shareholder", "2J", shares=650),
    Apartment("shareholder", "2K", shares=660),
    Apartment("shareholder", "3A", shares=670),
    Apartment("shareholder", "3B", shares=680),
    Apartment("shareholder", "3C", shares=690),
    Apartment("shareholder", "3F", shares=700),
    Apartment("shareholder", "3H", shares=710),
    Apartment("shareholder", "3J", shares=730),
    Apartment("shareholder", "3K", shares=740),
    Apartment("shareholder", "4A", shares=750),
    Apartment("shareholder", "4C", shares=760),
    Apartment("shareholder", "4E", shares=770),
    Apartment("shareholder", "4F", shares=780),
    Apartment("shareholder", "4G", shares=790),
    Apartment("shareholder", "4H", shares=800),
    Apartment("shareholder", "4K", shares=820),
    Apartment("shareholder", "4L", shares=830),
    Apartment("shareholder", "5A", shares=840),
    Apartment("shareholder", "5B", shares=850),
    Apartment("shareholder", "5C", shares=860),
    Apartment("shareholder", "5D", shares=870),
    Apartment("shareholder", "5F", shares=880),
    Apartment("shareholder", "5G", shares=890),
    Apartment("shareholder", "5J", shares=910),
    Apartment("shareholder", "5K", shares=920),
    Apartment("shareholder", "5L", shares=930),
    Apartment("shareholder", "6A", shares=940),
    Apartment("shareholder", "6B", shares=950),
    Apartment("shareholder", "6C", shares=960),
    Apartment("shareholder", "6D", shares=970),
    Apartment("shareholder", "6E", shares=980),
    Apartment("shareholder", "6F", shares=990),
    Apartment("shareholder", "6G", shares=1000),
    Apartment("shareholder", "6H", shares=1010),
    Apartment("shareholder", "6J", shares=1030),
    Apartment("shareholder", "6L", shares=1040),
    Apartment("shareholder", "7A", shares=1050),
    Apartment("shareholder", "7B", shares=1060),
    Apartment("shareholder", "7C", shares=1070),
    Apartment("shareholder", "7E", shares=1080),
    Apartment("shareholder", "7H", shares=1090),
    Apartment("shareholder", "7J", shares=1110),
    Apartment("shareholder", "7K", shares=1120),
    Apartment("shareholder", "7L", shares=1130),
]

# Set how many sponsor apartments to outrank (let's say 5 shareholder apartments will outrank)
outrank_count = 5

# Outrank sponsor apartments with shareholder apartments
updated_apartments = outrank_sponsor_apartments(sponsors, shareholders, outrank_count)

# Separate shareholder apartments and sponsor apartments for comparison
shareholder_apartments = [apartment for apartment in updated_apartments if apartment.apartment_type == 'shareholder']
sponsor_apartments = [apartment for apartment in updated_apartments if apartment.apartment_type == 'sponsor']

# Display the comparison results
print("Shareholder Apartments:")
for apartment in shareholder_apartments:
    print(apartment)

print("\nSponsor Apartments:")
for apartment in sponsor_apartments:
    print(apartment)
