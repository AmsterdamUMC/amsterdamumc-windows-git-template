import requests

# URL to your central forbidden extension list
EXT_URL = "https://raw.githubusercontent.com/AmsterdamUMC/amsterdamumc-windows-git-template/refs/heads/main/.amsterdamumc-scripts/forbidden-extensions.txt"

def fetch_forbidden_extensions():
    response = requests.get(EXT_URL)
    response.raise_for_status()
    return response.text.splitlines()


def generate_gitignore(extensions):
    lines = [
        "#",
        "# AmsterdamUMC .gitignore file",
        "#",
        "#",
        "# Auto-generated from forbidden-extensions.txt",
        "#",
        "",
        "",
        "# The 'data' directory is where all data should be placed which must",
        "# ** NOT ** be included in Git and GitHub.",
        "# These include for example output of runs, secrets ( API-keys, ",
        "# passwords, private-keys ) and all patient data.",
        "",
        "data/**",
        "",
        "# Ignore everthing in the .amsterdamumc-scripts directory. This line",
        "# was uncommented by the installation script which researchers",
        "# ran to setup their research software environment.",
        "",
        "# .amsterdamumc-scripts/**",
        ".amsterdamumc-scripts/.gitignore",
        ""
    ]
    for ext in extensions:
        ext = ext.strip()
        if not ext or ext.startswith("#"):
            continue
        lines.append(f"*.{ext}")
    return "\n".join(lines)


if __name__ == "__main__":
    extensions = fetch_forbidden_extensions()
    gitignore = generate_gitignore(extensions)

    with open(".gitignore", "w") as f:
        f.write(gitignore)

    print("✅ .gitignore file generated based on forbidden-extensions.txt")
