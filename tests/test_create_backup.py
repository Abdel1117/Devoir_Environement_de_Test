import os
from unittest.mock import patch
from backup_script import create_backup


def test_create_backup(tmp_path):
    # Création d'un dossier temporaire pour émuler un "home directory"
    dummy_home_dir = tmp_path / "home"
    dummy_home_dir.mkdir()

    # On y place un fichier bidon
    dummy_file = dummy_home_dir / "fichier.txt"
    dummy_file.write_text("Contenu de test")

    archive_name = "test_backup"

    # On "patch" la fonction get_home_directory pour qu'elle renvoie le dossier temporaire.
    with patch("backup_script.get_home_directory", return_value=str(dummy_home_dir)):
        archive_file = create_backup(archive_name)

    # Vérification que l'archive a bien été créée.
    assert os.path.exists(archive_file), "Le fichier de sauvegarde n'a pas été créé."

    # Nettoyage en fin de test
    if os.path.exists(archive_file):
        os.remove(archive_file)
