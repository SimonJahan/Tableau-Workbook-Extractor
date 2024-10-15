import zipfile
import os
from xml.etree import ElementTree as ET
import base64
from pathlib import Path
import tkinter as tk
from tkinter.filedialog import askopenfilename
from typing import Optional

def extract_zip_file(zip_file_path: str, extract_to: Path) -> bool:
    """
    Extracts the contents of a ZIP file to a specified directory.

    Args:
        zip_file_path (str): The path to the ZIP file.
        extract_to (Path): The directory to extract the contents to.

    Returns:
        bool: True if extraction was successful, False otherwise.
    """
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    except zipfile.BadZipFile:
        print("Fichier ZIP invalide.")
        return False
    return True

def parse_twb_file(twb_file_path: Path) -> Optional[ET.ElementTree]:
    """
    Parses the .twb file as XML.

    Args:
        twb_file_path (Path): The path to the .twb file.

    Returns:
        Optional[ET.ElementTree]: The root of the parsed XML tree if successful, None otherwise.
    """
    try:
        return ET.parse(twb_file_path)
    except ET.ParseError:
        print(f"Erreur lors du parsing du fichier TWB: {twb_file_path}")
        return None

def decode_shape_images(shapes: list[ET.Element], extract_dir: Path) -> None:
    """
    Decodes and saves the base64-encoded shape images from a list of XML elements.

    Args:
        shapes (list[ET.Element]): List of XML elements representing shape nodes.
        extract_dir (Path): The directory where the decoded images will be saved.
    """
    for shape_element in shapes:
        img_name = shape_element.attrib.get('name', '')
        img_directory = extract_dir / f"Shape/{img_name.split('/')[0]}"
        img_path = extract_dir / f"Shape/{img_name}"
        
        try:
            img_data = base64.b64decode(shape_element.text.encode("utf-8"))
        except base64.binascii.Error as e:
            print(f"Erreur lors du décodage de l'image {img_name}: {e}")
            continue

        img_directory.mkdir(parents=True, exist_ok=True)
        with open(img_path, "wb") as img_file:
            img_file.write(img_data)

def main() -> None:
    """
    Main function to extract a .twbx file, parse the .twb file within, and decode shape images.
    """
    tk.Tk().withdraw()
    path_to_zip_file = askopenfilename(filetypes=[("Tableau Workbook", "*.twbx")])
    
    if not path_to_zip_file:
        print("Aucun fichier sélectionné.")
        return
    
    twbx_file = Path(path_to_zip_file).stem
    extract_dir = Path.cwd() / twbx_file
    
    if not extract_zip_file(path_to_zip_file, extract_dir):
        return

    # Trouver le fichier .twb
    twb_file = next(extract_dir.glob("*.twb"), None)
    
    if twb_file is None:
        print("Fichier TWB introuvable.")
        return
    
    root = parse_twb_file(twb_file)
    
    if root is None:
        return

    # Extraction des images
    shapes = root.findall("./external/shapes/shape")
    decode_shape_images(shapes, extract_dir)