import os

OUTPUT = "README.md"

def main():
    icons = [f for f in os.listdir(".") if f.lower().endswith(".ico")]
    icons.sort()

    with open(OUTPUT, "w", encoding="utf-8") as fp:
        line = " ".join(f"![{f}](./{f})" for f in icons)
        fp.write(line)

    print("README.md generated.")

if __name__ == "__main__":
    main()
