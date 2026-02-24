import os
import shutil
from pathlib import Path

# Definimos categorías para agrupar extensiones
DIRECTORIOS = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Comprimidos": [".zip", ".rar", ".tar", ".gz"],
    "Ejecutables": [".exe", ".msi", ".dmg"]
}

def organizar_carpeta(ruta_str):
    ruta = Path(ruta_str)
    
    if not ruta.exists():
        print("La ruta especificada no existe.")
        return

    for item in ruta.iterdir():
        if item.is_dir():
            continue
        
        extension = item.suffix.lower()
        destino = "Otros"

        for categoria, extensiones in DIRECTORIOS.items():
            if extension in extensiones:
                destino = categoria
                break
        
        # Crear carpeta de destino si no existe
        ruta_destino = ruta / destino
        ruta_destino.mkdir(exist_ok=True)
        
        try:
            shutil.move(str(item), str(ruta_destino / item.name))
            print(f"✅ Movido: {item.name} -> {destino}/")
        except Exception as e:
            print(f"❌ Error moviendo {item.name}: {e}")

if __name__ == "__main__":
    carpeta = input("Introduce la ruta completa de la carpeta: ")
    organizar_carpeta(carpeta)
