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

    if 'precio' in ventas.columns:
        ventas['precio'] = ventas['precio'].astype(str).replace(
            {r'\$': '', ',': ''}, regex=True).astype(float)
        

    ventas.dropna(inplace=True)
    ventas.drop_duplicates(inplace=True)

    print("Transformación completada con éxito.")
    
    return ventas, clientes, marketing


def load_data(df_v_limpio, df_c_limpio, df_m_limpio):
    print("Cargando datos procesados...")
    
    # Crear carpeta si no existe
    os.makedirs("data", exist_ok=True)
    
    df_v_limpio.to_csv("data/ventas_limpio.csv", index=False)
    df_c_limpio.to_csv("data/clientes_limpio.csv", index=False)
    df_m_limpio.to_csv("data/marketing_limpio.csv", index=False)
    
    print("Pipeline ETL ejecutado exitosamente. ✅")


if __name__ == "__main__":
    print("--- Iniciando Data Pipeline ---")

    # Extract
    df_v, df_c, df_m = extract_data()

    # Transform
    ventas_limpio, clientes_limpio, marketing_limpio = transform_data(df_v, df_c, df_m)

    # Load
    load_data(ventas_limpio, clientes_limpio, marketing_limpio)