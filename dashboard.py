import streamlit as st
import pandas as pd
import numpy as np
import time

# Função para simular a obtenção de dados em tempo real
def get_realtime_data():
    # Substitua por sua própria lógica de aquisição de dados
    return {
        'O2': np.random.uniform(0, 10),
        'CACE': np.random.uniform(0, 0.2),
        'Sodium': np.random.uniform(0, 2),
        'SiO2': np.random.uniform(0, 10),
        'SC': np.random.uniform(0, 5),
        'pH': np.random.uniform(9.6, 10),
        'Temperature': np.random.uniform(20, 30),
        'Timestamp': pd.Timestamp.now()
    }

# Verifique se 'data_history' está na sessão; se não estiver, inicialize-o
if 'data_history' not in st.session_state:
    st.session_state['data_history'] = pd.DataFrame()

# Atualize os dados automaticamente a cada 10 segundos
refresh_rate = 10  # Tempo em segundos para a atualização dos dados
if 'last_update' not in st.session_state or (time.time() - st.session_state['last_update']) > refresh_rate:
    new_data = get_realtime_data()
    st.session_state['data_history'] = st.session_state['data_history'].append(new_data, ignore_index=True)
    st.session_state['last_update'] = time.time()
    st.experimental_rerun()

st.title('Painel de Monitoramento Industrial')

# Exibe os dados mais recentes
st.header('Últimas Métricas')
if not st.session_state['data_history'].empty:
    latest_data = st.session_state['data_history'].iloc[-1]
    st.metric(label="TOD (O2 ≤ 10ppb)", value=f"{latest_data['O2']:.3f} ppb")
    st.metric(label="CACE (≤0,2 µS/cm)", value=f"{latest_data['CACE']:.3f} µS/cm")
    # Adicione métricas adicionais conforme necessário

# Gráfico de linha do histórico de dados
st.subheader('Histórico de Métricas de O2')
if not st.session_state['data_history'].empty:
    st.line_chart(st.session_state['data_history'].set_index('Timestamp')['O2'])

# Rodapé
st.text('Painel de controle para monitoramento de parâmetros industriais críticos.')
import streamlit as st
import pandas as pd
import numpy as np
import time

# Função para simular a obtenção de dados em tempo real
def get_realtime_data():
    # Substitua por sua própria lógica de aquisição de dados
    return {
        'O2': np.random.uniform(0, 10),
        'CACE': np.random.uniform(0, 0.2),
        'Sodium': np.random.uniform(0, 2),
        'SiO2': np.random.uniform(0, 10),
        'SC': np.random.uniform(0, 5),
        'pH': np.random.uniform(9.6, 10),
        'Temperature': np.random.uniform(20, 30),
        'Timestamp': pd.Timestamp.now()
    }

# Verifique se 'data_history' está na sessão; se não estiver, inicialize-o
if 'data_history' not in st.session_state:
    st.session_state['data_history'] = pd.DataFrame(columns=['Timestamp', 'O2', 'CACE', 'Sodium', 'SiO2', 'SC', 'pH', 'Temperature'])

# Atualize os dados automaticamente a cada intervalo definido
refresh_rate = 10  # Tempo em segundos para a atualização dos dados
if 'last_update' not in st.session_state or (time.time() - st.session_state['last_update']) > refresh_rate:
    new_data = get_realtime_data()
    new_data_df = pd.DataFrame([new_data])
    st.session_state['data_history'] = pd.concat([st.session_state['data_history'], new_data_df], ignore_index=True).tail(100)  # Mantém apenas os últimos 100 registros
    st.session_state['last_update'] = time.time()
    st.experimental_rerun()

st.title('Painel de Monitoramento Industrial')

# Exibe os dados mais recentes
st.header('Últimas Métricas')
if not st.session_state['data_history'].empty:
    latest_data = st.session_state['data_history'].iloc[-1]
    st.metric(label="TOD (O2 ≤ 10ppb)", value=f"{latest_data['O2']:.3f} ppb")
    st.metric(label="CACE (≤0,2 µS/cm)", value=f"{latest_data['CACE']:.3f} µS/cm")
    # Adicione métricas adicionais conforme necessário

# Gráfico de linha do histórico de dados
st.subheader('Histórico de Métricas de O2')
if not st.session_state['data_history'].empty:
    st.line_chart(st.session_state['data_history'].set_index('Timestamp')['O2'])

# Rodapé
st.text('Painel de controle para monitoramento de parâmetros industriais críticos.')
