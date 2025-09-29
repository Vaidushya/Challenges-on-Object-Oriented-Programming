class RomanConverter:
    def int_to_roman(self, num):
        if not (0 < num < 4000):
            return "Number out of range (must be 1-3999)"
        
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        roman_num = ""
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num

if __name__ == "__main__":
    try:
        user_input = int(input("Enter an integer (1-3999): "))
        converter = RomanConverter()
        roman_value = converter.int_to_roman(user_input)
        print(f"Roman numeral: {roman_value}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")