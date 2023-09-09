from unit_test import utils 

# Test for reversed function
def testReversed(number, golden):
    return golden == utils.reversed(number)

print("Input: 100, Result:", testReversed(100, 1))
print("Input: -100, Result:", testReversed(-100, -1))
print("Input: \"125\", Result:", testReversed("125", 521)) # Strings are translated to int before reversing
print("Input: 13.2, Result:", testReversed(13.2, 31)) # Floats are truncated, before reversing

def testFormatter(number, golden_bin, golden_oct):
    actual_bin, actual_oct = utils.formatter(number)
    return actual_bin == golden_bin and actual_oct == golden_oct

print("Input: 100, Result:", testFormatter(100, 1100100, 144))
print("Input: -100, Result:", testFormatter(-100, -1100100, -144)) # Negative numbers should be handled well
print("Input: 64, Result:", testFormatter(64, 1000000, 100))
print("Input: \"100\", Result:", testFormatter("100", 1100100, 144)) # Strings are translated to int
print("Input: 12.3, Result:", testFormatter(12.3, 1100, 14)) # Floats are truncated
