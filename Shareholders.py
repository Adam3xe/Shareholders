class Apartment:
    def __init__(self, apartment_type, apartment_id, shares, apartment_number):
        self.apartment_type = apartment_type  # 'sponsor' or 'shareholder'
        self.apartment_id = apartment_id
        self.shares = shares
        self.apartment_number = apartment_number  # Unique apartment number

    def __repr__(self):
        return f"{self.apartment_type.capitalize()} {self.apartment_number} (Shares: {self.shares})"


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

# Manually specify apartment numbers for sponsor apartments (16 sponsor apartments)
sponsors = [
    Apartment("sponsor", i, shares=1000 + i * 10, apartment_number="3F,3B") for i in range(1, 17)
]

# Manually specify apartment numbers for shareholder apartments (61 shareholder apartments)
shareholders = [
    Apartment("shareholder", i, shares=500 + i * 5, apartment_number=201 + i) for i in range(1, 62)
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
