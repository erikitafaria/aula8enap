import streamlit as st
st.write('sou servidora pública')

st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
st.slider('grau de satisfação', 0, 100)
resposta_cliente = st.slider('Qual o seu grau de satisfação?', 0, 100)
st.write(str(resposta_cliente))
