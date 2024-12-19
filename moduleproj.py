def formatting_iteneries(traveler):
    for element in traveler:
        name, origin, destination = element
        print(f"travel: {name} - from {origin} to {destination}")
                

formatting_iteneries([("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")])



ibrary = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def adding_new_book():
    new_book = [("Harry Potter", "That One Woman")]
    grand_library = ibrary + new_book
    print(grand_library)



adding_new_book()


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]
def unpacking_tuple():
    for tuple in orders:
        name, device, number = tuple
        print(f"number {number} - {name} - device: {device}")

unpacking_tuple()