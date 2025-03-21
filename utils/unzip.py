import zipfile
import os

def unzip_file(zip_path, extract_to):
    zip_path = "./download/" + zip_path + ".zip"
    if not os.path.isfile(zip_path):
        print(f"    [-] Le fichier {zip_path} n'existe pas.")
        return
    
    os.makedirs(extract_to, exist_ok=True)
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Extraire tous les fichiers et récupérer la liste des fichiers extraits
            extracted_files = zip_ref.namelist()
            zip_ref.extractall(extract_to)
        print(f"    [+] Fichier décompressé avec succès dans {extract_to}")
        path = "./pwn/" + extracted_files[0]
        return path
    except zipfile.BadZipFile:
        print("     [-] Le fichier n'est pas un fichier ZIP valide.")