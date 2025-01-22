import os
import platform
import subprocess
from dotenv import load_dotenv

def open_directory_in_explorer():
    """
    Öffnet einen Ordner im Dateiexplorer, unabhängig vom Betriebssystem.
    """
    load_dotenv(dotenv_path=os.path.join(os.getcwd(), 'configurations', 'config.env'))
    DIR_ABSOLUT = os.getenv("REPORT_PATH_ABSOLUT")
    DIR_RELATIVE = os.getenv("REPORT_PATH_RELATIVE")

    folder_path = DIR_ABSOLUT if DIR_ABSOLUT else DIR_RELATIVE

    try:
        if not folder_path or not os.path.isdir(folder_path):
            raise FileNotFoundError(f"Der Ordner '{folder_path}' wurde nicht gefunden.")

        system_platform = platform.system()

        if system_platform == "Windows":
            os.startfile(DIR_ABSOLUT)
        elif system_platform == "Darwin":  # macOS
            subprocess.run(["open", DIR_ABSOLUT], check=True)
        elif system_platform == "Linux":
            subprocess.run(["xdg-open", DIR_ABSOLUT], check=True)
        else:
            raise OSError(f"Das Betriebssystem '{system_platform}' wird nicht unterstützt.")

        print(f"Der Ordner '{DIR_ABSOLUT}' wurde im Explorer geöffnet.")
    except Exception as e:
        print(f"Fehler beim Öffnen des Ordners: {e}")
