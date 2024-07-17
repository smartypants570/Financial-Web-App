import streamlit as st
tab1,tab2,tab3=st.tabs(["About Me","My Hobbies","Contacts"])
with tab1:
    col1,col2,col3=st.columns([0.25,0.25,0.5])
    with col1:
        st.image("images/rebirth_snake.jpg")
        st.write("My name is :rainbow[Adyah Addagulla]:thumbsup")
    with col2:
        st.image("images/Norse.jpg")
    with col3:
        st.write("My name is Adyah Addagulla and I love building stuff:hammer_and_pick:. Also I love Norse mythology and mythology in general. My chinese zodiac sign is a dragon.:dragon:")
with tab2:
    st.write("I play tennis:tennis: and four square. I love reading:book: and science:male-scientist:.")
    st.image("images/science.jpg")
with tab3:
    st.write("adyahacademy@gmail.com")
    st.write("xxx-xxx-xxxx")