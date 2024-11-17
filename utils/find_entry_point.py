import os
import re

def find_entry_point(zip_path):
    makefile_path = None
    entry_point_path = None
    entry_point_type = None

    # Dictionnaire associant les extensions de fichier aux expressions régulières pour trouver des points d'entrée
    entry_points = {
        "Makefile": (None, "Makefile"),  # Ajoute un tuple pour Makefile sans expression régulière
        ".py": (r'if __name__ == "__main__":', "Python main"),
        ".c": (r'int\s+main\s*\(', "C main"),
        ".cpp": (r'int\s+main\s*\(', "C++ main"),
        ".rs": (r'fn\s+main\s*\(', "Rust main")
    }

    # Parcourir les fichiers dans le répertoire extrait
    for root, dirs, files in os.walk(zip_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            # Vérifier la présence d'un Makefile sans expression régulière
            if file_name == "Makefile":
                print("    [+] Makefile trouvé :", file_path)
                makefile_path = file_path
                entry_point_type = "Makefile"
                break
            
            # Vérifier la présence des points d'entrée dans les autres types de fichiers
            for ext, (pattern, type_desc) in entry_points.items():
                if pattern and file_name.endswith(ext):
                    with open(file_path, "r", encoding="utf-8") as f:
                        try:
                            content = f.read()
                            if re.search(pattern, content):
                                print(f"    [+] Point d'entrée '{type_desc}' trouvé dans {file_name} :", file_path)
                                entry_point_path = file_path
                                entry_point_type = type_desc
                                break  # Arrête la recherche si un point d'entrée est trouvé
                        except UnicodeDecodeError:
                            print(f"   [-] Impossible de lire le fichier {file_path} en tant que texte.")
            if makefile_path or entry_point_path:
                break

    # Retourner un tuple contenant le chemin et le type de point d'entrée
    if makefile_path:
        return makefile_path, entry_point_type
    elif entry_point_path:
        return entry_point_path, entry_point_type
    else:
        print("    [-] Aucun Makefile ou fichier avec un point d'entrée trouvé.")
        return None, None
