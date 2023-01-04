password = "hepxxyzz"

inc = [chr(i) + chr(i+1) + chr(i+2) for i in range(ord("a"), ord("z")-1)]
not_allowed = ["i", "o", "l"]
doubles = [chr(i) + chr(i) for i in range(ord("a"), ord("z")+1)]

def next_password(current_password: str) -> str:
    temp = [ord(ch) for ch in list(current_password)[::-1]]
    
    for i in range(len(temp)):
        n = temp[i] + 1
        if n > ord("z"):
            temp[i] = ord("a")
            continue
        else:
            temp[i] = n
            break

    return "".join(chr(n) for n in temp[::-1])

while True:
    password = next_password(password)

    # condition 1
    inc_flag = False
    for item in inc:
        if item in password:
            inc_flag = True
            break
    if not inc_flag:
        continue

    # condition 2
    for na in not_allowed:
        if na in password:
            continue

    # condition 3
    oc = 0
    for d in doubles:
        if d in password:
            oc += 1
    if oc < 2:
        continue

    break

print(password)
