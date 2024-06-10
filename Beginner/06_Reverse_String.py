def ReverseStr(str):
    return str[::-1]

result = ReverseStr("hello")
print(result)


def reverse_string(s: str) -> str:
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"
