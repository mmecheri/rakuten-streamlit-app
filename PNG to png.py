# # # import os
# # # from PIL import Image

# # # # Dossier à traiter
# # # folder_path = './doc'

# # # # Parcours des fichiers dans le dossier
# # # for filename in os.listdir(folder_path):
# # #     if filename.endswith('.PNG'):
# # #         old_path = os.path.join(folder_path, filename)
# # #         new_filename = filename[:-4] + '.png'
# # #         new_path = os.path.join(folder_path, new_filename)

# # #         try:
# # #             # Ouvre et réenregistre l'image
# # #             with Image.open(old_path) as img:
# # #                 img.save(new_path)
# # #             print(f"[✔] Converted {filename} → {new_filename}")
# # #         except Exception as e:
# # #             print(f"[✘] Failed to convert {filename}: {e}")
# # import os

# # folder = './doc'

# # for f in os.listdir(folder):
# #     if f.endswith('.PNG'):
# #         png_version = f.replace('.PNG', '.png')
# #         if png_version in os.listdir(folder):
# #             print(f"🔍 Pair found: {f} ↔ {png_version}")
# import os
# from PIL import Image

# # Dossiers source et destination
# source_folder = "./PNG"
# target_folder = "./png_folder"

# # Crée le dossier de destination s'il n'existe pas
# os.makedirs(target_folder, exist_ok=True)

# # Parcours des fichiers dans le dossier source
# for filename in os.listdir(source_folder):
#     if filename.endswith(".PNG"):
#         source_path = os.path.join(source_folder, filename)
#         target_name = filename.replace(".PNG", ".png")
#         target_path = os.path.join(target_folder, target_name)

#         try:
#             with Image.open(source_path) as img:
#                 img.save(target_path)
#                 print(f"[✔] Converted {filename} → {target_name}")
#         except Exception as e:
#             print(f"[✘] Failed to convert {filename}: {e}")
import os

def find_png_references(directory):
    print("Searching for .PNG references in .py files...\n")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if 'PNG' in content:
                            print(f"[✔] Found 'PNG' in: {path}")
                except Exception as e:
                    print(f"[!] Could not read {path}: {e}")

# Utilisation
project_directory = "."  # ou remplace par ton chemin absolu
find_png_references(project_directory)
