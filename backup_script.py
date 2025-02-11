import os
import platform
import zipfile


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
    Crée une archive ZIP du répertoire personnel de l'utilisateur,
    en ignorant certains fichiers protégés (ex: NTUSER.DAT sous Windows).
    Retourne le chemin du fichier archive créé.
    """
    home_dir = get_home_directory()
    zip_filename = f"{archive_name}.zip"

    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(home_dir):
            dirs[:] = [d for d in dirs if d not in ("AppData", "Downloads")]
            for file in files:
                # Ignore le fichier NTUSER.DAT (et variantes NTUSER.DAT.LOG1, etc.)
                if file.startswith("NTUSER.DAT"):
                    continue

                full_path = os.path.join(root, file)
                # Chemin relatif pour que l'arborescence dans le zip ne commence pas à la racine du disque
                relative_path = os.path.relpath(full_path, start=home_dir)

                # On peut aussi ignorer d'autres fichiers/dossiers ici si besoin...

                # Tenter d'ajouter le fichier
                try:
                    zf.write(full_path, arcname=relative_path)
                except PermissionError:
                    # Si on n'a pas la permission de lire ce fichier, on l'ignore
                    pass

    return os.path.abspath(zip_filename)


def main():
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
