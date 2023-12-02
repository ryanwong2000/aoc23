with open("./1/input.in", "r", encoding="utf-8") as f:
    lines = f.readlines()
    values = []
    for line in lines:
        for char in line:
            if char.isdigit():
                l = char
                break
        for char in line[::-1]:
            if char.isdigit():
                r = char
                break
        values.append(int(l + r))
    # print(values)
    print(sum(values))
