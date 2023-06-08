#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    n = dir(hidden_4)
    for name in n:
        if not name.startswith("__"):
            print(name)
"""
if-name=main-> To only run the code inside the if statement,
When the program is run directly by the Python interpreter.
From..import..->when u need 2 use its code many times in your code project.
"""
