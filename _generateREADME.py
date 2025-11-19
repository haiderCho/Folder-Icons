import os

SIZE = 64
FILENAME = "README.md"

def generate_readme(path, icons):
    content = " ".join(
        f'<img src="./{icon}" width="{SIZE}" height="{SIZE}">'
        for icon in icons
    )
    with open(os.path.join(path, FILENAME), "w", encoding="utf-8") as f:
        f.write(content)

def main():
    for root, dirs, files in os.walk("."):
        icons = [f for f in files if f.lower().endswith(".ico")]
        if icons:
            icons.sort()
            generate_readme(root, icons)
            print(f"Created README.md in {root}")

if __name__ == "__main__":
    main()
