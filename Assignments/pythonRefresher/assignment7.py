def person_dict(first_name: str, last_name: str, age: int) -> dict:
    """
    Create a dictionary representing a person with keys 'first_name', 'last_name', and 'age'.
    """
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }

ren = person_dict("Renata", "Rodriguez", 30)
print(ren)