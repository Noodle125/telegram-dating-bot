def is_valid_name(name):
    return name.isalpha() and len(name) > 0

def is_valid_age(age):
    try:
        age = int(age)
        return 18 <= age <= 65
    except ValueError:
        return False
