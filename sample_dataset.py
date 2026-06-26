import os
import random
import shutil

# EDIT THESE PATHS to match your actual folders
SOURCE_DIR = r"D:\Kidney-disease-Classification\kidney-ct-scan-image"      # the big folder with Normal/ and Tumor/
DEST_DIR = r"D:\Kidney-disease-Classification\kidney-ct-scan-image-small"  # new trimmed folder to create

SAMPLES_PER_CLASS = 200
CLASSES = ["Normal", "Tumor"]

random.seed(42)  # for reproducibility

for class_name in CLASSES:
    src_class_dir = os.path.join(SOURCE_DIR, class_name)
    dest_class_dir = os.path.join(DEST_DIR, class_name)
    os.makedirs(dest_class_dir, exist_ok=True)

    all_files = [
        f for f in os.listdir(src_class_dir)
        if os.path.isfile(os.path.join(src_class_dir, f))
    ]

    sample_size = min(SAMPLES_PER_CLASS, len(all_files))
    sampled_files = random.sample(all_files, sample_size)

    for fname in sampled_files:
        shutil.copy2(
            os.path.join(src_class_dir, fname),
            os.path.join(dest_class_dir, fname)
        )

    print(f"{class_name}: copied {sample_size} files to {dest_class_dir}")

print("Done. Trimmed dataset ready at:", DEST_DIR)