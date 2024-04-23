import streamlit as st
import time

# Função para simular a progressão em "tempo real"
def simulacao_progressiva(texto, duracao=3, passos=6):
    placeholder = st.empty()
    for _ in range(passos):
        placeholder.text(f"{texto} {'.' * (_ % passos)}")
        time.sleep(duracao / passos)
    placeholder.empty()

# Inicializa o estado se ainda não estiver definido
if 'oleo_lubrificacao' not in st.session_state:
    st.session_state['oleo_lubrificacao'] = False

if 'oleo_hidraulico' not in st.session_state:
    st.session_state['oleo_hidraulico'] = False

if 'turning_gear' not in st.session_state:
    st.session_state['turning_gear'] = False

if 'velocidade_rpm' not in st.session_state:
    st.session_state['velocidade_rpm'] = 0

st.title("Simulador de Partida de Turbina a Gás")

def iniciar_sistemas():
    simulacao_progressiva("Iniciando sistemas de óleo de lubrificação e hidráulico", 5)
    st.session_state['oleo_lubrificacao'] = True
    st.session_state['oleo_hidraulico'] = True
    st.success("Sistemas de óleo de lubrificação e hidráulico iniciados.")

def ativar_turning_gear():
    simulacao_progressiva("Ativando Turning Gear", 3)
    st.session_state['turning_gear'] = True
    st.session_state['velocidade_rpm'] = 76
    st.success("Turning Gear ativado. Rotor a 76 RPM.")

def aumentar_velocidade():
    simulacao_progressiva("Aumentando velocidade do rotor", 4, passos=st.session_state['velocidade_rpm'] // 100)
    st.session_state['velocidade_rpm'] += 100
    if st.session_state['velocidade_rpm'] < 1800:
        st.write(f"Velocidade do Rotor: {st.session_state['velocidade_rpm']} RPM")
    else:
        st.success("Turbina alcançou a velocidade operacional.")

if st.button("Iniciar Sistemas"):
    iniciar_sistemas()

if st.session_state['oleo_lubrificacao'] and st.session_state['oleo_hidraulico']:
    if st.button("Ativar Turning Gear"):
        ativar_turning_gear()

if st.session_state['turning_gear']:
    if st.button("Aumentar Velocidade"):
        aumentar_velocidade()

# Informações adicionais sobre o processo
st.sidebar.header("Informações da Turbina")
st.sidebar.text(f"Sistema de Óleo de Lubrificação: {'Ativo' if st.session_state['oleo_lubrificacao'] else 'Inativo'}")
st.sidebar.text(f"Sistema de Óleo Hidráulico: {'Ativo' if st.session_state['oleo_hidraulico'] else 'Inativo'}")
st.sidebar.text(f"Turning Gear: {'Ativo' if st.session_state['turning_gear'] else 'Inativo'}")
st.sidebar.text(f"Velocidade Atual: {st.session_state['velocidade_rpm']} RPM")
