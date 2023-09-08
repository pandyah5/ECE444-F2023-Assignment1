import math
from math import log

class utils:
    def reversed(number):
        if (number >= 0):
            return int(str(number)[::-1])
        else:
            return -1 * int(str(-1 * number)[::-1])

    def formatter(number):
        # For base 2
        limit = int(log(number) / log(2))
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

