import pandas as pd
import os

def extract_data():
    print("Iniciando extracción de datos...")
    
    url_ventas = 'https://raw.githubusercontent.com/karenymorel/analisis-exploratorio-datos-python/main/data/ventas.csv'
    url_marketing = 'https://raw.githubusercontent.com/karenymorel/analisis-exploratorio-datos-python/main/data/marketing.csv'
    url_clientes = 'https://raw.githubusercontent.com/karenymorel/analisis-exploratorio-datos-python/main/data/clientes.csv'
    
    df_ventas = pd.read_csv(url_ventas)
    df_marketing = pd.read_csv(url_marketing)
    df_clientes = pd.read_csv(url_clientes)
    
    return df_ventas, df_clientes, df_marketing

def transform_data(df_ventas, df_clientes, df_marketing):
    print("Iniciando transformación de datos...")
    
    ventas = df_ventas.copy()
    clientes = df_clientes.copy()
    marketing = df_marketing.copy()

    if 'precio_unitario' in ventas.columns:
        ventas['precio_unitario'] = ventas['precio_unitario'].replace(
            {r'\$': '', ',': ''}, regex=True).astype(float)
        
    if 'inversion_total' in marketing.columns:
         marketing['inversion_total'] = marketing['inversion_total'].replace(
             {r'\$': '', ',': ''}, regex=True).astype(float)

    ventas.dropna(inplace=True)
    ventas.drop_duplicates(inplace=True)

    df_unificado = pd.merge(ventas, clientes, on='id_cliente', how='inner')
    
    print("Transformación completada con éxito.")
    return df_unificado

def load_data(df_final, output_path="data/dataset_analitico_final.csv"):
    print(f"Cargando datos procesados en: {output_path}")
    
    # Crear carpeta si no existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Exportar a CSV
    df_final.to_csv(output_path, index=False)
    print("Pipeline ETL ejecutado exitosamente. ✅")


if __name__ == "__main__":
  print("--- Iniciando Data Pipeline ---")

  # Extract
  df_v, df_c, df_m = extract_data()

  # Transform
  dataset_final = transform_data(df_v, df_c, df_m)

  # Load
  load_data(dataset_final)