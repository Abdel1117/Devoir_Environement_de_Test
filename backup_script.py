import os
import platform
import shutil


def detect_os():
    """
    Détecte le système d'exploitation de la machine.
    Retourne une chaîne de caractères (par ex. 'Windows', 'Linux', 'Darwin').
    """
    return platform.system()


def get_home_directory():
    """
    Retourne le chemin du répertoire personnel de l'utilisateur.
    """
    return os.path.expanduser("~")


def create_backup(archive_name="home_backup"):
    """
    Crée une archive zip du répertoire personnel de l'utilisateur.
    Retourne le chemin du fichier archive créé.
    """
    home_dir = get_home_directory()
    archive_path = shutil.make_archive(archive_name, "zip", home_dir)
    return archive_path


def main():
    """
    Point d'entrée : propose à l'utilisateur de créer une sauvegarde.
    """
    current_os = detect_os()
    print(f"Votre système d'exploitation est : {current_os}")

    proceed = input(
        "Souhaitez-vous créer une sauvegarde de votre répertoire personnel ? (O/N) : "
    )
    if proceed.strip().lower() == "o":
        archive_file = create_backup()
        print(f"Sauvegarde créée : {archive_file}")
    else:
        print("Opération annulée.")


if __name__ == "__main__":
    main()
