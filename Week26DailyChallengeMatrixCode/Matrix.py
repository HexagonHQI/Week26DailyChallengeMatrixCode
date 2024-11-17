def decode_matrix(matrix):
    # Initialize an empty string to store the decoded message
    decoded_message = ""

    # Loop column (index)
    for col in range(len(matrix[0])):  # matrix[0
        # Loop
        for row in range(len(matrix)):
            
            char = matrix[row][col]
            
            if char.isalpha():
                decoded_message += char
            
            elif decoded_message and decoded_message[-1] != " ":
                decoded_message += " " 

    return decoded_message

# Matrix provided
matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

# Function to call
message = decode_matrix(matrix)
print(message)
