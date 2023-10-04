import streamlit as st
import webbrowser
import time

st.title("Het Sevalia Welcomes You <3!!")

def play_music(track_url):
    st.write("Playing your selected music...")
    webbrowser.open_new_tab(track_url)

def show_quote(quote):
    st.write(quote)
    
def main():
    no = st.radio("Are you a new user?", ["Yes", "No"])
    if no == "Yes":
        st.write("User Manual:")
        st.write("1. You will get a list of moods/feelings to select from.")
        st.write("2. Select the mood/feeling from the list.")
        st.write("3. You will get a quote.")
        st.write("4. You will be redirected to songs related to the mood/feeling.")
        st.write("Note: The application will be running in the background.")
        st.write("5. Answer the questions to proceed or exit.")
    else:
        st.write("Happy to have you back. We hope you are having a good experience.")

    smul = st.radio("Are you going through mixed feelings?", ["Yes", "No"])
    
    mood_dict = {
        "Happy": "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
        "Sad": "Even the darkest night will end and the sun will rise. - Victor Hugo",
        "Anger": "When anger rises, think of the consequences. - Confucius",
        "Anxiety": "You don't have to control your thoughts. You just have to stop letting them control you. - Dan Millman",
        "Excitement": "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Enthusiastic": "Enthusiasm is the electricity of life. - Gordon Parks",
        "Love": "The best thing to hold onto in life is each other. - Audrey Hepburn",
        "Jealousy": "Jealousy is a disease, love is a healthy condition. The immature mind often mistakes one for the other. - Robert A. Heinlein",
        "Frustration": "Frustration, although quite painful at times, is a very positive and essential part of success. - Bo Bennett",
        "Boredom": "Boredom is the feeling that everything is a waste of time; serenity, that nothing is. - Thomas Szasz",
        "Moodswings": "Emotions are like waves, you can't stop them from coming but you can choose which ones to surf. - Anonymous",
        "Depressed": "Depression is like a heaviness that you can't ever escape. It crushes down on you, making even the smallest things like tying your shoes or chewing on toast seem like a twenty-mile hike uphill. Depression is a part of you; it's in your bones and your blood. - Jasmine Warga, My Heart and Other Black Holes",
        "Lonely": "Loneliness is not the absence of people, but the absence of purpose. - Dr. Wayne Dyer",
        "Affectionate": "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage. - Lao Tzu",
        "Disappointed": "Disappointment is a temporary obstacle on the road to success. - Unknown",
        "Miss Someone": "Missing someone is your heart's way of reminding you that you love them. - Unknown",
        "Exhausted": "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "Self Doubt": "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Special": "You're feeling special because either you have worked for it or someone else worked for you. - Unknown",
        "Gujju Kick In": "Jetla ae dur jata rev ane khush reilav , chele toh ghar jevu sukh kase nai madee. - Unknown"
    }

    selected_mood = st.selectbox("Select Mood/Feeling:", list(mood_dict.keys()))
    
    if smul == "Yes":
        while True:
            x = st.number_input("Enter mood/feeling number (Enter -1 to exit):", min_value=-1, value=0)
            if x == -1:
                break
            if x in range(1, 21):
                show_quote(mood_dict[selected_mood])
                if x != 0:
                    play_music(get_track_url(x))
            else:
                st.write("Invalid input")
    else:
        x = st.number_input("Enter mood/feeling number:", min_value=1, max_value=20, value=0)
        if x in range(1, 21):
            show_quote(mood_dict[selected_mood])
            if x != 0:
                play_music(get_track_url(x))
        else:
            st.write("Invalid input")

    st.write("Contact Us:")
    st.write("Het Sevalia")
    st.write("Call Us: +919909984896")
    st.write("Email Us: hetsevalia84@gmail.com")
    st.write("Feel free to contact us for anything.")

if __name__ == "__main__":
    main()
