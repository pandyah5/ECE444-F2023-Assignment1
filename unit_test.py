import math
from math import log

class utils:
    def reversed(number):
        number = int(number)
        if (number >= 0):
            return int(str(number)[::-1])
        else:
            return -1 * int(str(-1 * number)[::-1])

    def formatter(num):
        number = int(num)

        # Negative numbers
        neg = number < 0
        if (neg):
            number = -1 * number

        # For base 2
        limit = int(log(number) / log(2))
        if (neg):
            base2_string = "-"
        else:
            base2_string = ""

        base2_number = number

        while (limit >= 0):
            if (base2_number >= math.pow(2, limit)):
                base2_number -= math.pow(2, limit)
                limit -= 1
                base2_string += "1"
            else:
                limit -= 1
                base2_string += "0" 
        
        # For base 8 
        if (neg):
            base8_string = "-"
        else:
            base8_string = ""
        
        base8_number = number
        limit = int(log(number) / log(8))

        while (limit >= 0):
            if (base8_number >= math.pow(8, limit)):
                base8_quotient = int(base8_number / math.pow(8, limit))
                base8_number -= math.pow(8, limit) * base8_quotient
                limit -= 1
                base8_string += str(base8_quotient)
            else:
                limit -= 1
                base8_string += "0"

        return int(base2_string), int(base8_string)

