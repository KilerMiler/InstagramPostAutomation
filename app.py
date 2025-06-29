import streamlit as st
import tempfile
import os
import time
from main import config
from main import login
from main import posting
from main import logout
from main import closing
from main import checkPosting
from main import checkLogin

def main():
    st.set_page_config(page_title="Instagram Auto-Poster")
    st.title("Welcome to Instagram Auto-Poster!")

    # ── SIDEBAR: CREDENTIALS ────────────────────────────────────────────────────
    st.sidebar.header("🔑 Instagram Credentials")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    st.markdown(
        """
        Welcome the new way of posting things on Instagram.
        """
    )

    with st.form(key="post_form"):
        uploaded_file = st.file_uploader(
            label="Select an image or video",
            type=["jpg", "jpeg", "png", "mp4"],
            help="Upload a JPG/PNG image or MP4 video"
        )
        caption = st.text_area(
            "Caption",
            placeholder="Write your caption here…",
            help="Supports emojis and hashtags"
        )
        submit = st.form_submit_button("Post to Instagram")

    # ── HANDLER ────────────────────────────────────────────────────────────────
    if submit:
        if not username or not password:
            st.error("❌ Please enter your Instagram username and password in the sidebar.")
        elif not uploaded_file:
            st.error("❌ Please upload a media file to post.")
        else:
            with st.spinner("Opening Instagram"):
                driver = config.get_driver()
                wait_driver = config.get_wait_driver(driver)
                driver.get("https://instagram.com")
                login.login_account(username,password, wait_driver)
                time.sleep(2)
                if checkLogin.is_user_logged_in_successfully(driver):
                    if uploaded_file:
                        isVideo=False
                        if os.path.splitext(uploaded_file.name)[1] in ['.mp4', '.mov']:
                            isVideo=True
                        with tempfile.NamedTemporaryFile(
                            suffix=os.path.splitext(uploaded_file.name)[1],
                            prefix="streamlit_",
                            delete=True,
                            dir='./temp'
                        ) as tmp:
                            tmp.write(uploaded_file.read())
                            tmp.flush()

                            posting.post_content(tmp.name, wait_driver, isVideo)
                        if (checkPosting.is_posted_successfully(wait_driver)):
                            closing.close_shared_sub_window(wait_driver)
                            logout.logout(wait_driver)
                            driver.quit()
                        else:
                            driver.quit()
                            st.error("Not successfull")
                    else:
                        st.error("Not Uploaded")

                else:
                    driver.quit()
                    st.sidebar.error("❌ Invalid username or password")


 
if __name__ == "__main__":
    main()