def min_distance(s: str, t: str) -> int:
    m, n = len(s), len(t)
    
    # Create a 2D DP table initialized with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the base cases
    for i in range(m + 1):
        dp[i][0] = i  # Deleting all characters from s to match empty t
    for j in range(n + 1):
        dp[0][j] = j  # Inserting all characters into empty s to match t
        
    # Fill the rest of the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Characters match, no operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],    # Insert operation
                    dp[i - 1][j],    # Remove operation
                    dp[i - 1][j - 1] # Replace operation
                )
                
    return dp[m][n]

# Get dynamic inputs from the user
s_input = input("Enter the first string s: ")
t_input = input("Enter the second string t: ")

# Calculate and display the result
result = min_distance(s_input, t_input)
print(result)
