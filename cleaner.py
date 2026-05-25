
def clean_data(data):
    """Clean raw data read from a text file.
 
    Steps:
    1. Accept a list of strings (from readlines()).
    2. Skip the first element (header row).
    3. Typecast each remaining string to float and append to a new list.
    4. Return the cleaned list of floats.
    """
    cleaned = []
 
    for value in data[1:]:          # skip header
        cleaned.append(float(value.strip()))
 
    return cleaned
   