*Number & Logic Tester*

Small Python script I wrote for CDA 3103C to work through number systems and logic gates. Converts a few test numbers to binary and hex, then builds full truth tables for AND, OR, XOR, and NOT gates.

The two things that took the longest and most research: format(num, 'b') and format(num, 'x') doing the actual binary/hex conversion, and using != as a stand-in for XOR since Python doesn't have a built-in xor keyword.
