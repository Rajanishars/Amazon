def longest_unique_substring(s: str) -> int:
    char_map = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        # If character is in the current window, move start pointer
        if s[end] in char_map and char_map[s[end]] >= start:
            start = char_map[s[end]] + 1
        
        # Update last seen index
        char_map[s[end]] = end
        # Track max length
        max_length = max(max_length, end - start + 1)

    return max_length

# Get dynamic string input from the user
user_input = input("Enter the string S: ")
result = longest_unique_substring(user_input)

# Display the output
print(result)
