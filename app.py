import streamlit as st

# Configuração da página (título na aba do navegador e ícone)
st.set_page_config(
    page_title="Calculadora Simples",
    page_icon="🧮",
    layout="centered"
)

# 1. Título principal com ícone amigável
st.title("🧮 Calculadora Interativa")
st.write("Boas-vindas! Insira os números, escolha a operação e clique em **Calcular**.")

st.divider()  # Linha divisória para organizar o visual

# Criando duas colunas na interface para colocar os números lado a lado
col1, col2 = st.columns(2)

# 2. Dois campos de entrada numérica com valor padrão 0.0
with col1:
    numero_1 = st.number_input("Primeiro número:", value=0.0, step=1.0, format="%.2f")

with col2:
    numero_2 = st.number_input("Segundo número:", value=0.0, step=1.0, format="%.2f")

# 3. Componente de seleção para escolher a operação
operacao = st.radio(
    "Escolha a operação desejada:",
    options=["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"],
    horizontal=True
)

st.divider()

# 4. Botão de ação
if st.button("Calcular", type="primary", use_container_width=True):
    # 5. Lógica de cálculo com animação de balões em casos de sucesso
    if operacao == "Soma (+)":
        resultado = numero_1 + numero_2
        st.balloons()  # Animação de balões subindo na tela
        st.success("Cálculo realizado com sucesso!")
        st.metric(label="Resultado da Soma", value=f"{resultado:.2f}")

    elif operacao == "Subtração (-)":
        resultado = numero_1 - numero_2
        st.balloons()  # Animação de balões subindo na tela
        st.success("Cálculo realizado com sucesso!")
        st.metric(label="Resultado da Subtração", value=f"{resultado:.2f}")

    elif operacao == "Multiplicação (*)":
        resultado = numero_1 * numero_2
        st.balloons()  # Animação de balões subindo na tela
        st.success("Cálculo realizado com sucesso!")
        st.metric(label="Resultado da Multiplicação", value=f"{resultado:.2f}")

    elif operacao == "Divisão (/)":
        # Validação para evitar divisão por zero
        if numero_2 == 0:
            st.error("⚠️ Ops! Não é possível dividir por zero. Por favor, escolha outro valor para o segundo número.")
        else:
            resultado = numero_1 / numero_2
            st.balloons()  # Animação de balões subindo na tela
            st.success("Cálculo realizado com sucesso!")
            st.metric(label="Resultado da Divisão", value=f"{resultado:.4f}")
            # Feito
