import streamlit as st
import pandas as pd
import plotly.express as px

# Configurações do pandas
pd.set_option('display.max_colwidth', None)

# Dados das turbinas
data = pd.DataFrame({
    'Modo': ['Ignition ~ Warm up', 'Mode 3', 'Mode 2', 'Mode 1', 'Mode 6B', 'Mode 6A', 'Mode 6AQ'],
    'Temperatura': ['-', '842–888', '842–999', '999–1138', '1138–1149', '1149–1343', '-'],
    'Potencia': ['-', '~10', '10–20', '20–37', '37–42', '42–50', '-'],
})

# Título e descrição
st.title("Painel de Controle da Turbina a Gás")
st.write("")

# Função para simular a partida da turbina
def simulate_turbine_startup(mode_data, speed):
    st.write("Simulando a partida da turbina...")
    progress_bar = st.progress(0)
    for i, mode in enumerate(mode_data):
        st.write(f"Modo: {mode['Modo']} | Temperatura: {mode['Temperatura']} °C | Potência: {mode['Potencia']} MW")
        time.sleep(1 / speed)
        progress_bar.progress((i + 1) / len(mode_data))
    st.success("A turbina está totalmente operacional!")

# Slider para velocidade da simulação
speed = st.slider('Velocidade da Simulação', 0.1, 5.0, 1.0, 0.1)

# Botão para iniciar a simulação
if st.button('Iniciar Partida da Turbina'):
    simulate_turbine_startup(data.to_dict('records'), speed)

# Gráfico interativo de Potência
st.subheader('Gráfico Interativo de Potência por Modo')
filtered_data = data[data['Potencia'] != '-'].copy()
filtered_data['Potencia'] = filtered_data['Potencia'].str.replace('~', '').str.split('–').apply(lambda x: (float(x[0]) + float(x[-1])) / 2)
fig = px.line(filtered_data, x='Modo', y='Potencia', markers=True, title="Potência por Modo")
st.plotly_chart(fig, use_container_width=True)

# Tabela com detalhes dos modos de operação
st.subheader('Detalhes dos Modos de Operação')
st.table(data)

# Detalhes dos Modos em um expander
with st.expander("Ver Detalhes dos Modos"):
    for _, row in data.iterrows():
        st.text(f"Modo: {row['Modo']}")
        st.text(f"Temperatura: {row['Temperatura']} °C")
        st.text(f"Potência: {row['Potencia']} MW")

# Exibição das imagens ou GIFs na horizontal
st.write("Visualização das Câmaras de Combustão:")
image_urls = [
    "https://j.gifs.com/n55l0W.gif",
    "https://gifs.eco.br/wp-content/uploads/2022/05/gifs-de-turbo-3.gif",
    # Adicione quantas URLs você precisar
]

# Exibe as imagens ou GIFs na horizontal
cols = st.beta_columns(len(image_urls))  # Cria uma coluna para cada URL
for col, url in zip(cols, image_urls):
    col.image(url, use_column_width=True)  # Exibe a imagem/GIF na coluna correspondente
