# Create a function using `**kwargs`.


def display_kwargs(**kwargs):
    print(kwargs)


display_kwargs(name="Dev Verse", age=20, city="Kushi Nagar")

#  *args vs **kwargs
# *args    → multiple positional arguments → tuple
# **kwargs → multiple keyword arguments   → dictionary
