def convert_hex_to_binary(hex_string):
    """Convert a hexadecimal string to a binary string."""
    try:
        # Convert hex to binary, remove '0b' prefix, and ensure correct length by padding
        binary_string = bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)
        return binary_string
    except ValueError:
        raise ValueError(f"Invalid input: {hex_string} is not a hexadecimal string.")

def break_binary_string(binary_string):
    """Break a binary string into segments based on changes from 0 to 1 and vice versa."""
    if all(c in '01' for c in binary_string):
        output = ''
        for i in range(len(binary_string)):
            output += binary_string[i]
            if i < len(binary_string) - 1 and binary_string[i] != binary_string[i + 1]:
                output += '\n'
        return output
    else:
        raise ValueError(f"Invalid input: {binary_string} is not a binary string.")

def calculate_rf_raw(binary_signal_array, sample_rate):
    """Calculate the RF raw signal from the binary signal array."""
    rf_raw_signal = []
    for line in binary_signal_array.split('\n'):
        length = len(line)
        if '1' in line:
            rf_raw_signal.append(str(length * sample_rate))
        else:
            rf_raw_signal.append(str(length * -sample_rate))
    
    rf_raw_string = '[' + ', '.join(rf_raw_signal) + ']'
    return rf_raw_string

def convert_to_esp_home_raw(input_string, sample_rate, name='test'):
    """Convert a hexadecimal or binary string to ESPHome raw format."""
    # Determine if the input is a binary or hexadecimal string
    if all(c in '01' for c in input_string):
        binary_string = input_string
    else:
        binary_string = convert_hex_to_binary(input_string)
    
    print(f"BinaryString: {binary_string}")
    
    binary_array = break_binary_string(binary_string)
    
    rf_raw_result = calculate_rf_raw(binary_array, sample_rate)
    print(f"code: {rf_raw_result}")

# Examples of how to use the function
if __name__ == "__main__":
    # Example usage with hex input:
    #convert_to_esp_home_raw("b6492d924964b6", 300)
    
    # Example usage with binary input:
    convert_to_esp_home_raw("1011011001001001001011011001001001001001011001011001011", 300)
