class UserMainCode(object):
    @classmethod
    def bitwise(cls, input1):
        bits = "{0:b}".format(int(input1))
        set_bits_count = 0
        least_significant_bit_index = 0
        most_significant_bit_index = 0

        for i in range(0, len(bits)):
            if bits[i] == "1":
                if most_significant_bit_index == 0:
                    most_significant_bit_index = len(bits) - i - 1
                else:
                    least_significant_bit_index = len(bits) - i - 1
                set_bits_count += 1

        return (
            str(set_bits_count)
            + "#"
            + str(least_significant_bit_index)
            + "#"
            + str(most_significant_bit_index)
        )


obj = UserMainCode()
output = obj.bitwise(10)
print(output)
