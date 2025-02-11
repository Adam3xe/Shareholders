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
    # Ensure that the number of sponsor apartments is at least the outrank_count
    if len(sponsor_apartments) < outrank_count:
        raise ValueError("The number of sponsor apartments cannot be less than the outrank count.")

    # Sort shareholder apartments by the number of shares in descending order
    sorted_shareholders = sorted(shareholder_apartments, key=lambda x: x.shares, reverse=True)

    # "Outrank" the sponsor apartments by placing the shareholder apartments before them
    outranked_sponsor_apartments = sorted_shareholders[:outrank_count]
    remaining_shareholders = sorted_shareholders[outrank_count:]

    # Create a new list where outranked shareholder apartments are placed ahead of sponsor apartments
    updated_apartments = outranked_sponsor_apartments + sponsor_apartments + remaining_shareholders
    return updated_apartments


def compare_sponsor_and_shareholder(sponsor_apartments, shareholder_apartments):
    """
    This function compares sponsor apartments with shareholder apartments based on their share count.

    It shows which shareholder apartments outrank a sponsor apartment.

    Args:
    - sponsor_apartments (list): List of sponsor apartment objects.
    - shareholder_apartments (list): List of shareholder apartment objects.
    """
    used_shareholders = []  # Track used shareholder apartments

    # Iterate through each sponsor apartment to compare with shareholders
    for sponsor in sponsor_apartments:
        total_shareholder_shares = 0
        outranking_shareholders = []

        # Exclude the used shareholders from the list of available shareholders
        available_shareholders = [shareholder for shareholder in shareholder_apartments if shareholder not in used_shareholders]

        # For each sponsor apartment, collect shareholders whose sum of shares outranks the sponsor
        for shareholder in available_shareholders:
            total_shareholder_shares += shareholder.shares
            outranking_shareholders.append(shareholder)

            # If the total shareholder shares outrank the sponsor, stop adding more shareholders
            if total_shareholder_shares > sponsor.shares:
                break

        # If total shareholder shares outrank sponsor, show the output
        if total_shareholder_shares > sponsor.shares:
            outranking_names = [apartment.apartment_name for apartment in outranking_shareholders]
            print(f"Shareholders {', '.join(outranking_names)} outrank Sponsor apartment {sponsor.apartment_name} "
                  f"with sum {total_shareholder_shares} > {sponsor.shares}.")

            # Add the outranking shareholders to the used list
            used_shareholders.extend(outranking_shareholders)


# Example usage:

# Sponsor apartments (initial 16 sponsors as per your list)
sponsors = [
    Apartment("sponsor", "1A", shares=300),
    Apartment("sponsor", "1B", shares=400),
    Apartment("sponsor", "1L", shares=500),
    Apartment("sponsor", "2B", shares=600),
    Apartment("sponsor", "2E", shares=700),
    Apartment("sponsor", "2G", shares=800),
    Apartment("sponsor", "3D", shares=900),
    Apartment("sponsor", "3E", shares=999),
    Apartment("sponsor", "3G", shares=1000),
    Apartment("sponsor", "4B", shares=300),
    Apartment("sponsor", "4D", shares=500),
    Apartment("sponsor", "4J", shares=700),
    Apartment("sponsor", "5E", shares=400),
    Apartment("sponsor", "5H", shares=800),
    Apartment("sponsor", "6K", shares=970),
    Apartment("sponsor", "7F", shares=850),
]

# Shareholder apartments
shareholders = [
    Apartment("shareholder", "1C", shares=100),
    Apartment("shareholder", "1D", shares=200),
    Apartment("shareholder", "1E", shares=300),
    Apartment("shareholder", "1F", shares=400),
    Apartment("shareholder", "1G", shares=540),
    Apartment("shareholder", "1H", shares=100),
    Apartment("shareholder", "1I", shares=200),
    Apartment("shareholder", "1J", shares=300),
    Apartment("shareholder", "1K", shares=400),
    Apartment("shareholder", "2A", shares=500),
    Apartment("shareholder", "2C", shares=900),
    Apartment("shareholder", "2D", shares=100),
    Apartment("shareholder", "2F", shares=600),
    Apartment("shareholder", "2H", shares=630),
    Apartment("shareholder", "2I", shares=640),
    Apartment("shareholder", "2J", shares=650),
    Apartment("shareholder", "2K", shares=660),
    Apartment("shareholder", "3A", shares=670),
    Apartment("shareholder", "3B", shares=680),
    Apartment("shareholder", "3C", shares=100),
    Apartment("shareholder", "3F", shares=200),
    Apartment("shareholder", "3H", shares=300),
    Apartment("shareholder", "3I", shares=400),
    Apartment("shareholder", "3J", shares=500),
    Apartment("shareholder", "3K", shares=600),
    Apartment("shareholder", "4A", shares=500),
    Apartment("shareholder", "4C", shares=500),
    Apartment("shareholder", "4E", shares=500),
    Apartment("shareholder", "4F", shares=500),
    Apartment("shareholder", "4G", shares=790),
    Apartment("shareholder", "4H", shares=500),
    Apartment("shareholder", "4I", shares=810),
    Apartment("shareholder", "4K", shares=820),
    Apartment("shareholder", "4L", shares=830),
    Apartment("shareholder", "5A", shares=840),
    Apartment("shareholder", "5B", shares=850),
    Apartment("shareholder", "5C", shares=860),
    Apartment("shareholder", "5D", shares=870),
    Apartment("shareholder", "5F", shares=880),
    Apartment("shareholder", "5G", shares=890),
    Apartment("shareholder", "5I", shares=900),
    Apartment("shareholder", "5J", shares=910),
    Apartment("shareholder", "5K", shares=920),
    Apartment("shareholder", "5L", shares=930),
    Apartment("shareholder", "6A", shares=940),
    Apartment("shareholder", "6B", shares=950),
    Apartment("shareholder", "6C", shares=960),
    Apartment("shareholder", "6D", shares=970),
    Apartment("shareholder", "6E", shares=980),
    Apartment("shareholder", "6F", shares=990),
    Apartment("shareholder", "6G", shares=60),
    Apartment("shareholder", "6H", shares=150),
    Apartment("shareholder", "6I", shares=90),
    Apartment("shareholder", "6J", shares=320),
    Apartment("shareholder", "6L", shares=340),
    Apartment("shareholder", "7A", shares=900),
    Apartment("shareholder", "7B", shares=200),
    Apartment("shareholder", "7C", shares=200),
    Apartment("shareholder", "7E", shares=120),
    Apartment("shareholder", "7H", shares=200),
    Apartment("shareholder", "7I", shares=90),
    Apartment("shareholder", "7J", shares=80),
    Apartment("shareholder", "7K", shares=80),
    Apartment("shareholder", "7L", shares=100),
]

# Set how many sponsor apartments to outrank (let's say 16 for this example)
outrank_count = 16

# Ensure sponsors are at least as many as outrank_count
if len(sponsors) >= outrank_count:
    # Outrank sponsor apartments with shareholder apartments
    updated_apartments = outrank_sponsor_apartments(sponsors, shareholders, outrank_count)

    # Separate shareholder apartments and sponsor apartments for comparison
    shareholder_apartments = [apartment for apartment in updated_apartments if
                              apartment.apartment_type == 'shareholder']
    sponsor_apartments = [apartment for apartment in updated_apartments if apartment.apartment_type == 'sponsor']

    # Perform the comparison and show the results
    compare_sponsor_and_shareholder(sponsor_apartments, shareholder_apartments)
else:
    print(f"Error: The number of sponsor apartments ({len(sponsors)}) is less than the outrank count ({outrank_count}).")
