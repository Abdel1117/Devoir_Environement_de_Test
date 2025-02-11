import pytest
from backup_script import detect_os


def test_detect_os():
    os_detected = detect_os()
    # On vérifie simplement que la fonction renvoie l'une des valeurs attendues
    assert os_detected in [
        "Windows",
        "Linux",
        "Darwin",
    ], "Le système d'exploitation détecté n'est pas reconnu."
