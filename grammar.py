from input import terminals, start_Var, grammar as gr


# Function to find variables that can generate a given string using the CYK algorithm
def cyk(string, computed=None, grammar=gr):
    # Initialize the computed dictionary if it is not provided
    if computed is None:
        computed = {}

    # If the string is already computed, return the computed dictionary
    if string in computed:
        return computed
    else:
        # Base case: if the string length is 1, check which variables can generate this terminal directly
        if len(string) == 1:
            computed[string] = []
            for notation in grammar:
                if notation[1] == string:
                    computed[string].append(notation[0])
            computed[string] = sorted(computed[string])  # Sort the results for consistency
            return computed
        else:
            # Recursive case: if the string length is greater than 1
            computed[string] = []
            for i in range(1, len(string)):
                # Split the string into two parts
                split1 = string[:i]
                split2 = string[i:]

                # Recursively compute the possible variables for each split part
                computed1 = cyk(split1, computed)[split1]
                computed2 = cyk(split2, computed)[split2]

                # Combine the results from the two split parts
                if computed1 and computed2:
                    for var1 in computed1:
                        for var2 in computed2:
                            for notation in grammar:
                                # Check if the combination of variables matches any production rule
                                if var1 + var2 == notation[1] and notation[0] not in computed[string]:
                                    computed[string].append(notation[0])
            computed[string] = sorted(computed[string])  # Sort the results for consistency
            return computed


# Function to check if the string is accepted by the grammar and print the result
def print_cyk(string):
    # Check if all symbols in the string are terminals
    for char in string:
        if char not in terminals:
            print(f"'{string}' contains symbols not in the terminals.")
            return "wrong"

    # Find all possible ways to generate the string and its substrings
    result = cyk(string)
    if start_Var in result.get(string, []):
        print(f"'{string}' is accepted")
        # Print the ways the string and its substrings were generated
        for i in range(1, len(string) + 1):
            for j in range(len(string) - i + 1):
                substr = string[j:j + i]
                if substr in result:
                    print(f"{substr} : {result[substr]} , ", end="")
                else:
                    print(f"{substr} : [] , ", end="")
            print()
        return True
    else:
        print(f"'{string}' is not accepted")
        return False
