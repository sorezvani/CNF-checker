import re

# Initialize lists for variables, terminals, and grammar rules, and a string for the start variable
variables = []
terminals = []
start_Var = ''
grammar = []

# Define the path to the grammar file
path = "Grammar.txt"


# Function to split a line based on given name and return cleaned parts
def split(line, name):
    parts = re.split(r"[, :\n]+", line)
    return [part for part in parts if part and part != name]


# Open the file and read its content
with open(path, "r") as f:
    variables = split(f.readline(), "Variables")
    terminals = split(f.readline(), "Terminals")
    start_Var = split(f.readline(), "Start_Var")[0]

    # Skip the empty line
    f.readline()

    # Read and process grammar rules
    rules = f.readlines()
    for rule in rules:
        rule_parts = re.split(r"[\s\n,]+", rule.strip())
        if rule_parts:
            grammar.append(rule_parts)
