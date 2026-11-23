import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Profile", page_icon="👤", layout="centered")

st.title("My Profile")

default_photo = Path(__file__).with_name("images.jpg")

with st.container(border=True):
    photo_column, details_column = st.columns([1, 2], vertical_alignment="center")

    with photo_column:
        if default_photo.exists():
            st.image(
                str(default_photo),
                caption="Profile picture",
                use_container_width=True,
            )
        else:
            st.markdown(
                """
                <div style="
                    aspect-ratio: 1;
                    border-radius: 50%;
                    background: #e8eef5;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 64px;
                ">👤</div>
                """,
                unsafe_allow_html=True,
            )

    with details_column:
        st.subheader("Inspector Minks")
        st.write("**Age:** 39")
        st.write("**Address:** Purok bisan asa, basta maka laag")
        st.write("**Job:** SEcreto para Bibo")
        st.write("**About:** Gwapo ko basta gwapo ko...")
        st.write("**Skills:** kanang bahala dili kaayo kabalo basta gwapo ko")
        st.write("**Contact:** secretoparabibo@gmail.com / 123456789")

st.subheader("Location")
st.markdown(
    """
    <iframe
        src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d829.7210810926367!2d126.27649515159014!3d8.360921382310044!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sph!4v1795401218978!5m2!1sen!2sph"
        width="100%"
        height="450"
        style="border:0;"
        allowfullscreen=""
        loading="lazy"
        referrerpolicy="strict-origin-when-cross-origin">
    </iframe>
    """,
    unsafe_allow_html=True,
)
