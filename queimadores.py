import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import plotly.express as px




    
# Garantindo que o pandas não abrevie as sequências longas
pd.set_option('display.max_colwidth', None)

# Dados simulados das turbinas
data = pd.DataFrame({
    'Modo': ['Ignition ~ Warm up', 'Mode 3', 'Mode 2', 'Mode 1', 'Mode 6B', 'Mode 6A', 'Mode 6AQ'],
    'Temperatura': ['-', '842–888', '842–999', '999–1138', '1138–1149', '1149–1343', '-'],
    'Potencia': ['-', '~10', '10–20', '20–37', '37–42', '42–50', '-'],
})

# Adiciona uma explicação inicial sobre o dashboard
st.write("""
    
""")
# Simulação de imagens como GIF
def simulate_images_as_gif(image_paths, delay=0.5):
    st.write("Visualização das Câmaras de Combustão:")
    # Cria containers para as imagens lado a lado
    cols = st.columns(len(image_paths))
    images_containers = [cols[i].container() for i in range(len(cols))]

    # Loop para simular um GIF exibindo as imagens em sequência
    for img_path, container in zip(image_paths, images_containers):
        container.image(img_path, use_column_width=True)
        time.sleep(delay)
        
# Simulação de imagens como GIF
def simulate_images_as_gif(image_paths, delay=0.5):
    st.write("Visualização das Câmaras de Combustão:")
    # Cria containers para as imagens lado a lado
    cols = st.columns(len(image_paths))
    images_containers = [cols[i].container() for i in range(len(cols))]

    # Loop para simular um GIF exibindo as imagens em sequência
    for img_path, container in zip(image_paths, images_containers):
        container.image(img_path, use_column_width=True)
        time.sleep(delay)
                
# Função para simular o processo de partida de uma turbina
def simulate_turbine_startup(mode_data, speed):
    st.write("Simulando a partida da turbina...")
    progress_bar = st.progress(0)
    log_area = st.empty()

    for i, mode in enumerate(mode_data):
        log_area.write(f"Modo: {mode['Modo']} | Temperatura: {mode['Temperatura']} °C | Potência: {mode['Potencia']} MW")
        time.sleep(1 / speed)  # Ajusta a velocidade da simulação
        progress_bar.progress((i + 1) / len(mode_data))

    st.success("A turbina está totalmente operacional!")

# Slider para ajustar a velocidade da simulação
speed = st.slider('Velocidade da Simulação', min_value=0.1, max_value=5.0, value=1.0, step=0.1)

# Botão para iniciar a simulação da partida da turbina
if st.button('Iniciar Partida da Turbina'):
    simulate_turbine_startup(data.to_dict('records'), speed)

# Gráfico interativo de Potência
st.subheader('Gráfico Interativo de Potência por Modo')
# Usando plotly para gráficos interativos
filtered_data = data[data['Potencia'] != '-'].copy()
filtered_data['Potencia'] = filtered_data['Potencia'].str.replace('~', '').str.split('–').apply(lambda x: (float(x[0]) + float(x[-1])) / 2)
fig = px.line(filtered_data, x='Modo', y='Potencia', markers=True, title="Potência por Modo")
st.plotly_chart(fig, use_container_width=True)

# Mostrando os dados da turbina em uma tabela
st.subheader('Detalhes dos Modos de Operação')
st.table(data)

# Detalhes dos Modos em Expander
with st.expander("Ver Detalhes dos Modos"):
    for index, row in data.iterrows():
        st.markdown(f"**Modo:** {row['Modo']}")
        st.write(f"**Temperatura:** {row['Temperatura']} °C")
        st.write(f"**Potência:** {row['Potencia']} MW")

# Simulação de imagens como GIF
def simulate_images_as_gif(image_paths, delay=0.5):
    st.write("Visualização das Câmaras de Combustão:")
    image_container = st.empty()  # Cria um container vazio para as imagens

    # Loop para simular um GIF exibindo as imagens em sequência
    while True:
        for img_path in image_paths:
            image_container.image(img_path, use_column_width=True)
            time.sleep(delay)

    
def show_image_from_url(url):
    st.image(url)

# URLs das imagens ou GIFs que você deseja exibir
image_urls = [
    
    "https://j.gifs.com/n55l0W.gif",
    "https://gifs.eco.br/wp-content/uploads/2022/05/gifs-de-turbo-3.gif",
    
    # Adicione quantas URLs você precisar
]

# Para exibir as imagens ou GIFs diretamente
for url in image_urls:
    show_image_from_url(url)
