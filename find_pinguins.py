import numpy as np
import cv2
import pandas as pd

def make_coord_list(csv_path):
    # Leer el archivo CSV
    df = pd.read_csv(csv_path)

    # Obtener las primeras 10 filas
    primeras_10_filas = df.head(10)
    
    # Mostrar las primeras 10 filas
    print(primeras_10_filas)

    # Convertir a un array de NumPy
    array_numpy = primeras_10_filas.values.tolist()


    return array_numpy

def find_pinguins(half_heigth, half_weigth, image_path, coordinates_list, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Could not open or find the image: {image_path}")
    img_height, img_width = img.shape
    
    for coordinates in coordinates_list:
        print(coordinates)
        x_center, y_center = coordinates[1], coordinates[2]
        
        # Calculate the crop boundaries
        x_start = max(x_center - half_heigth, 0)
        x_end = min(x_center + half_heigth, img_width)
        y_start = max(y_center - half_weigth, 0)
        y_end = min(y_center + half_weigth, img_height)
        
        img_cropped = img[y_start:y_end, x_start:x_end]
        
        # Save the cropped image
        output_file = f"{output_path}/cropped_{x_center}_{y_center}.tiff"
        cv2.imwrite(output_file, img_cropped, [cv2.IMWRITE_TIFF_COMPRESSION, 1])
    
    return
