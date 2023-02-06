"""
    Modular Arithmetic
    For this project we are going to implement a special Mod class to implement some concepts in modular arithmetic

    -> assume n is a positive integer, also a and b are integers
    -> the residue of a number a modulo n, is simply a % n

    Two numbers, a and b, are said to be congruent modulo n: a = b (mod n)
            if their resdidues are equal i.e  a % n == b % n

    Example:
        7 % 12 -> 7 
                        -> 7 is congruent to 19 modulo
        19 % 12 -> 7


    Project:
    -> Create a class called Mod
    ->initialize with values  and modulus arguements
        -> ensure modulus and value are both integers
        -> moreover, modulus should be positive

    -> store the value as the residue
        i.e if value = 8 and modulus = 3, store value as 2 (8 % 3)

    -> implement congruence for the == operator
      -> allow comparison of a Mod object to an int (in which case use the residue of the int)
      -> allow comparison of two Mod objects only if they have the same modulus
      -> ensure objects remain hashable

    -> provide an implementation so that int(mod_object) will return the residue
    -> provide a proper representation (repr)
    -> implement the operators: +, -, *, **
            ->support other operand to be Mod (with same modulus only)
            ->support other operand to be an integer (and use the same modulus)
            -> always return a Mod instance
                perform the +, - *, ** operations on th values (so there's nothing complicated here)
                    i.e Mod(2, 3) + 16 -> Mod(2 + 16, 3) -> Mod(0, 3)
    -> implement the corresponding in-place arithmetic operators

    -> implement ordering (makes sense we are comparing residues)
        -> support other operand to be a Mod(with same modulus), or an integer
"""

#Project 2 Solution

from functools import total_ordering

@total_ordering
class Mod:
    def __init__(self, value, modulus):
        if not isinstance(modulus, int):
            raise TypeError("Unsupported type for modulus")
        if not isinstance(value, int):
            raise TypeError("Unsupported type for value")
        if modulus <=0:
            raise ValueError("modulus must be positive")
        self._modulus = modulus
        self._value = value % modulus

    @property
    def modulus(self):
        return self._modulus

    @property
    def value(self):
        return self._value

    def __repr__(self) -> str:
        return f"Mod({self.value}, {self.modulus})"

    def __int__(self):
        return self.value

    def __eq__(self, other):
        other_value = self._get_values(other)
        return other_value == self.value
        # if isinstance(other, Mod):
        #     if self.modulus != other.modulus:
        #         return NotImplemented
        #     else:
        #         return self.value == other.value 
        # elif isinstance(other, int):
        #     return other % self.modulus == self.value 
        # else:
        #     return NotImplemented

    def __hash__(self) -> int:
        return hash(self.value, self.modulus)

    def __neg__(self):
        return Mod(-self.value, self.modulus)

    def __add__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return Mod(self.value + other.value, self.modulus)
        if isinstance(other, int):
            return Mod(self.value + other, self.modulus)
        return NotImplemented

    def __sub__(self, other):
        # if isinstance(other, Mod) and self.modulus == other.modulus:
        #     return Mod(self.value - other.value, self.modulus)
        # if isinstance(other, int):
        #     return Mod(self.value - other, self.modulus)
        # return NotImplemented

        other_value = self._get_values(other)
        return Mod(self.value - other_value, self.modulus)

    def __mul__(self, other):
        other_value = self._get_values(other)
        return Mod(self.value * other_value, self.modulus)
        # if isinstance(other, Mod) and other.modulus == self.modulus:
        #     return Mod(self.value * other.value, self.modulus)
        # if isinstance(other, int):
        #     return Mod(self.value*other, self.modulus)
        # return NotImplemented

    def __pow__(self, other):
        other_value = self._get_values(other)
        return Mod(self.value ** other_value, self.modulus)

    def __iadd__(self, other):
        other_value = self._get_values(other)
        self.value = (self.value + other_value) % self.modulus
        return self 
        # if isinstance(other, Mod) and self.modulus == other.modulus:
        #     self.value = (self.value + other.value) % self.modulus 
        #     return self 
        
        # if isinstance(self, int):
        #     self.value = (self.value + other) % self.modulus
        #     return self 
        # return NotImplemented
    
    def __isub__(self, other):
        other_value = self._get_values(other)
        self.value = (self.value - other_value) % self.modulus
        return self 
        # if isinstance(other, Mod) and self.modulus == other.modulus:
        #     self.value = (self.value - other.value) % self.modulus
        #     return self 
        # if isinstance(other, int):
        #     self.value = (self.value - other) % self.modulus
        #     return self 
        # return NotImplemented

    def __imul__(self, other):
        other_value = self._get_values(other)
        self.value = (self.value * other_value) % self.modulus
        return self 
        # if isinstance(other, Mod) and self.modulus == other.modulus:
        #     self.value = (self.value * other.value) % self.modulus
        #     return self 
        # if isinstance(other, int):
        #     self.value = (self.value * other) % self.modulus
        #     return self 

    def __ipow__(self, other):
        other_value = self._get_values(other)
        self.value = (self.value ** other_value) % self.modulus
        return self 
        # if isinstance(other, Mod) and self.value == other.modulus:
        #     self.value = (self.value ** other.value) % self.modulus
        #     return self 
        # if isinstance(other, int):
        #     self.value = (self.value ** other) % self.modulus
        #     return self 
        # return NotImplemented

    def __lt__(self, other):
        # if isinstance(other, Mod)  and other.modulus == self.value:
        #     return self.value < other.value
        # if isinstance(other, int):
        #     return self.value < other % self.modulus
        # return NotImplemented
        try:
            other_value = self._get_values(other)
            return self.value < other_value.value 
        except TypeError:
            return NotImplemented

    def _is_compatible(self, other):
        return isinstance(other, int) or (isinstance(other, Mod)  and self.modulus == other.modulus)

    def _get_values(self, other):
        if isinstance(other, int):
            return other % self.modulus

        if isinstance(other, Mod) and self.modulus == other.modulus:
            return other.value
        raise TypeError('Incompatible types.')


print(Mod(3, 12) == Mod(15, 12))

print(Mod(3, 12) + 12)

print(Mod(3, 12) + 25)

print(Mod(3, 12) + Mod(25, 12))

print(Mod(3, 12) + Mod(3, 5))


        





        


        