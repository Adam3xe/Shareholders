class Apartment:
    def __init__(self, apartment_type, apartment_id):
        self.apartment_type = apartment_type  # 'sponsor' or 'shareholder'
        self.apartment_id = apartment_id

    def __repr__(self):
        return f"{self.apartment_type.capitalize()} {self.apartment_id}"


def outrank_sponsor_apartments(sponsor_apartments, shareholder_apartments, outrank_count):
    """
    This function simulates outranking a set number of sponsor apartments
    by shareholder apartments.

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

    # "Outrank" the sponsor apartments by placing the shareholder apartments before them
    outranked_sponsor_apartments = shareholder_apartments[:outrank_count]
    remaining_shareholders = shareholder_apartments[outrank_count:]

    # Create a new list where outranked shareholder apartments are placed ahead of sponsor apartments
    updated_apartments = outranked_sponsor_apartments + sponsor_apartments[outrank_count:] + remaining_shareholders
    return updated_apartments


# Example usage:
# Create sponsor apartments (16 sponsor apartments)
sponsors = [Apartment("sponsor", i) for i in range(1, 17)]

# Create shareholder apartments (61 shareholder apartments)
shareholders = [Apartment("shareholder", i) for i in range(1, 62)]

# Set how many sponsor apartments to outrank (let's say 5 shareholder apartments will outrank)
outrank_count = 5

# Outrank sponsor apartments with shareholder apartments
updated_apartments = outrank_sponsor_apartments(sponsors, shareholders, outrank_count)

# Print the updated list of apartments
for apartment in updated_apartments:
    print(apartment)
