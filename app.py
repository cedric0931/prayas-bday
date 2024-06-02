import streamlit as st
# from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(
    page_title="Happy Birthday, Pookie! 🎉",
    page_icon="🎂",
    layout="centered"
)


if st.button("Click me for a surprise! 🎁"):
    st.balloons()
    
    st.title("🎂 Happy Birthday, Pookie! ")
    st.subheader("Wishing you the best birthday ever! 🎉")

    st.image("prayas1.jpg", caption="Have a blast on your special day! 🎈")

    st.write("Hey Pookie,")
    st.write("I'm so grateful to have you in my life. You're the best thing that's ever happened to me, and I hope this day is as amazing as you are! 🌟")
    st.write("Here's to many more birthdays together! 💖")

    # add_vertical_space(2)

    st.write("Surprise! I love you so much! 😘")

    st.video("https://youtu.be/NhHb9usKy6Q?si=nb_p7WylGqsHpx8V")

    # Footer
    st.write("With all my love, 💕")
    st.write("Your Boo")



