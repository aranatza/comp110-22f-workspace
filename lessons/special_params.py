"""Examples of optional parameters and Union types."""

from typing import Union

def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += name
    elif isinstance(name, int):
        greeting += "COMP" + str(name)
    else: 
        greeting += "Alied Life from Sector " + str(name)
    return greeting


# Single Argument
print(hello("Sally"))

# No arguments
print(hello())

# int argument works too
print(hello(110))