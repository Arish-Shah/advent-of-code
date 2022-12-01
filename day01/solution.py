def main():
    file = open("./input")

    cal = []
    for elf in file.read().strip().split("\n\n"):
        cal.append(sum([int(n) for n in elf.split("\n")]))
    cal.sort(reverse=True)
    
    print(cal[0])
    print(sum(cal[0:3]))

    file.close()

if __name__ == "__main__":
    main()
