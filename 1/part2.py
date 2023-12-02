with open("./1/input.in", "r", encoding="utf-8") as f:
    lines = f.readlines()
    values = []
    digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"}

    def digit_in_word(word: str) -> str | None:
        for key in digits:
            if key in word:
                # print("key", word)
                return digits[key]
        return None

    for line in lines:
        for i, char in enumerate(line):
            digit = digit_in_word(line[:i])
            if digit:
                l = digit
                # print(f"l {i} {l} {line}")
                break
            elif char.isdigit():
                l = char
                break
        reversed_line = line[::-1]
        for j, char in enumerate(reversed_line):
            digit = digit_in_word(line[len(line) - j :])  # gross
            if digit:
                r = digit
                # print(f"r {j} {r} {line}")
                break
            if char.isdigit():
                r = char
                break
        values.append(int(l + r))

    print(sum(values))
