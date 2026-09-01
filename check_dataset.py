#  inspect dataset
import os

dataset_path = "."

image_extensions = (".jpg", ".jpeg", ".png", ".webp")

for class_name in os.listdir(dataset_path):

    class_path = os.path.join(dataset_path, class_name)

    if os.path.isdir(class_path):

        count = 0

        for root, folders, files in os.walk(class_path):

            for file in files:

                if file.lower().endswith(image_extensions):
                    count += 1

        print(f"{class_name}: {count} images")

        #   read images

        from PIL import Image
        



