from pathlib import Path

def create_project_structure(project_name):
    base = Path(project_name)

    # 🔎 Vérification si le projet existe déjà
    if base.exists() and base.is_dir():
        print(f"Erreur : Le dossier '{project_name}' existe déjà. Création annulée.")
        return
    
    # 📁 Création dossiers
    folders = [
        "src",
        "tests",
        "docs",
        "data",
        "config",
        "images"
    ]

    # 📄 Création fichiers
    files = [
        "requirements.txt",
        "src/__init__.py",
        "tests/__init__.py"
    ]

    # 📁 Création dossiers
    for folder in folders:
        (base / folder).mkdir(parents=True, exist_ok=True)

    # 📄 Création fichiers
    for file in files:
        (base / file).touch()

    # 📝 README
    with open(base / "README.md", "w") as readme:
        readme.write(f"# Projet : {project_name}\n\n"
                     f"↓ Description du projet ↓\n\n")

    # 🚫 .gitignore
    with open(base / ".gitignore", "w") as gitignore:
        gitignore.write("venv/\n"
                        ".env\n"
                        "__pycache__/\n"
                        "*.pyc\n"
                        "*.pyo\n"
                        "*.pyd\n")

    # ▶ main.py
    with open(base / "src" / "main.py", "w") as main_file:
        main_file.write(
            "def main():\n"
            "    print(\"Projet demarre avec succes!\")\n\n"
            "if __name__ == \"__main__\":\n"
            "    main()\n"
        )

    print(f"Projet → {project_name} ← créé avec succès !")

if __name__ == "__main__":
    name = input("Entrer le nom du nouveau projet : ")
    create_project_structure(name)
