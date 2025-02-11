import pytest
import os
from backup_script import get_home_directory


def test_get_home_directory():
    home_dir = get_home_directory()
    assert os.path.exists(home_dir), "Le répertoire personnel n'existe pas."
    assert os.path.isdir(
        home_dir
    ), "Le chemin du répertoire personnel ne pointe pas vers un dossier."
