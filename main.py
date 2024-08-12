# # folder path ---------> C:\Users\Om enterprises\pyt-port

# --------------------------------------------import section start-------------------------------------------
import pathlib as Path
import streamlit as st
import google.generativeai as genai
from streamlit_option_menu import option_menu
from PIL import Image
import time
import pandas as pd
import pydeck as pdk
import streamlit.components.v1 as components
import requests
# --------------------------------------------import section end------------------------------------

# ---------------------------------------------GENERAL SETTINGS ------------------------------------------


# ------------------css import start--------------------

# current_dir = "C:\Users\Om enterprises\pyt-port"

PAGE_TITLE = "Portfolio | Shivansh Chauhan"
PAGE_ICON = ":wave:"
NAME = "Shivansh Chauhan"
DESCRIPTION = """
Dynamic Electronics Engineer with hands-on experience in IoT, embedded systems, and PCB design. Passionate about innovation and continuous improvement in technology. 🌟🔧
"""
EMAIL = "shivanshchauhan@email.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/@electronicsnoob?si=YydMrmLal3k5RsWK",
    "LinkedIn": "https://www.linkedin.com/in/shivanshchauhan2001",
    "GitHub": "https://github.com/Shivansh21git",
    "Superprof": "https://www.superprof.co.in/dashboard.html/my-profile/",
}   
PROJECTS = {
    "🏆 ATVS - It is an anti theft system for 2 wheelers": "https://github.com/Shivansh21git/Anti-theft-vehicle-system-.git",
    "🏆 Krishi Sarthi - IoT based soil testing device ": "https://github.com/Shivansh21git/IoT-Based-project-krishi-sarthi-.git",
    "🏆 PCB Designs - PCB designs of different modules": "https://github.com/Shivansh21git/PCB-Designs.git",
    "🏆 Minor Projects - Projects involving Arduino interfacing with different sensors     and actuators": "https://github.com/Shivansh21git/Arduino_Projects.git",
}

css_file = "styles/style.css"
resume_file = "info/shivansh_Iot_Embedded_resume.pdf"

st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON,layout="centered",initial_sidebar_state="auto")
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --------------------css import end----------------------

# ---------------------------------------------GENERAL SETTINGS End------------------------------------------




# --------------------------------------------contact variables start-------------------------------------------

# Define the recipient email address
email_address = "shivanshchauhan.228@gmail.com"
# Create the mailto link
mailto_link = f"mailto:{email_address}"
linkd = "https://www.linkedin.com/in/shivanshchauhan2001"
# Defining phone no
phone_number = "+1234567890"
# Create the tel link
tel_link = f"tel:{phone_number}"

# --------------------------------------------contact variables end-------------------------------------------


# --------------------------------------------Performa start-------------------------------------------

performa = ''' you are an answering bot and will answer on belhalf of me (i.e, shivansh chauhan). you will answer questions ask by page visitors on my portfolio website as first person and if you dont know about something then just answer 'That's a secret🤫, contact me for this information'.     
I am shivansh chauhan i am an electronics and communication engineer completed my bachelors of technology from moradabad institute of technology, moradabad(mit) which is affiliated from AKTU i.e., Dr. APJ Abdul Kalam Technology lucknow previously known as 
uttar pradesh technical university. i have completed my degree in 2023. it was a 4 year course in which i have studied core electronics along with it i have gained knowledge in related technologies like Embedded, IOT, PCB Designing, #d printing, Digital electronics, etc and i have made varous 
electronics projects in academic life. i havwe worked with various microcontroller and developement boards like arduino famiy boards, esp boards and raspberrypi. 









'''


# --------------------------------------------Performa end-------------------------------------------


#------------------------------------------------All HTML CODES---------------------------------------------

html_code_name = """
<div class="typewriter">
  <h1>I am Shivansh Chauhan</h1>
</div>

<style>
.typewriter h1 {
  color: #ffffff; /* Change text color if necessary */
  font-family: monospace;
  overflow: hidden; /* Ensures the content is hidden outside the element's area */
  border-right: .15em solid orange; /* Creates the cursor effect */
  white-space: nowrap; /* Keeps the text in a single line */
  margin: 0; /* Adjust as needed */
  letter-spacing: .02em; /* Adjusts the spacing between characters */
  animation:
    typing 1.5s steps(40, end),
    blink-caret .75s step-end infinite;
}

@keyframes typing {
  from { width: 0 }
  to { width: 80% }
}

@keyframes blink-caret {
  from, to { border-color: transparent }
  50% { border-color: orange }
}
</style>
"""




#------------------------------------------------HTML CODES END----------------------------------------------

# --------------------------------------------Dialogue/Function section start---------------------------------------

@st.dialog("How would you like to Connect with me")
def cont():
 col1,col2,col3 =st.columns(3,gap="medium",vertical_alignment="center")
 with col1:   
    st.markdown(f"""
    <a href="{mailto_link}">
        <button style="background-color:orange;color:white;border:none;padding:10px 20px;text-align:center;text-decoration:none;display:inline-block;font-size:15px;margin:4px 2px;cursor:pointer;border-radius:16px;">
           Email Me ✉
        </button>
    </a>
""", unsafe_allow_html=True)
 with col2:
              st.markdown(f"""
    <a href="{tel_link}">
        <button style="background-color:orange;color:white;border:none;padding:10px 20px;text-align:center;text-decoration:none;display:inline-block;font-size:16px;margin:4px 2px;cursor:pointer;border-radius:16px;">
            Call Me   ☎
        </button>
    </a>
""", unsafe_allow_html=True)
              
 with col3:
         st.markdown(f"""
    <a href="{linkd}">
        <button style="background-color:orange;color:white;border:none;padding:10px 20px;text-align:center;text-decoration:none;display:inline-block;font-size:16px;margin:4px 2px;cursor:pointer;border-radius:16px;">
            Linkdin   💻
        </button>
    </a>
""", unsafe_allow_html=True)
         
         
def downRes():
    st.balloons()
    # Create a placeholder
    placeholder = st.empty()

    # Show success message
    placeholder.success('Downloaded Successfully!',icon="✔")

    # # Wait for 3 seconds
    time.sleep(3)

    # # Clear the placeholder
    placeholder.empty()

         
# --------------------------------------------Dialogue/Functions section end---------------------------------------
        



# --------------------------------------------AI config start-------------------------------------------  
api=st.secrets["key"]
genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-1.5-flash')

# --------------------------------------------AI config end-------------------------------------------



# if 'selected' not in st.session_state:
#     st.session_state.selected = "Home"

# Define a function to synchronize the selected option
# def synchronize_selection(selected):
#     st.session_state.selected = selected_option
with st.sidebar:
    selected = option_menu(
        menu_title="Portfolio",
        options=["Home", "Resume","Contact"],
        icons=["house", "book", "bi bi-person-lines-fill"],
        menu_icon="cast",
        default_index=0,
        key="sidebar_menu",
        styles={
            "container": {"padding": "0!important", "background-color": "#33555e"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "red"},
        }
       
    )
    st.write(" ")
    st.write("Made With :heart: By Shivansh")

# Top menu
# selected_top = option_menu(
#     menu_title=None,
#     options=["Home", "Resume","Projects","Contact"],
#     icons=["house", "book", "phone"],
#     menu_icon="cast",
#     default_index=0,
#     orientation="horizontal",
#     key="top_menu",
#     styles={
#         "container": {"padding": "0!important", "background-color": "#fafafa"},
#         "icon": {"color": "orange", "font-size": "25px"},
#         "nav-link": {"font-size": "20px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "red"},
#     }
    
# )

# --------------------------------------------Pages Selection start-------------------------------------------

# # Update session state based on menu selection
# if selected_sidebar != st.session_state.selected:
#     synchronize_selection(selected_sidebar)
# elif selected_top != st.session_state.selected:
#     synchronize_selection(selected_top)

# # Ensure both menus reflect the same state
# selected = st.session_state.selected

# --------------------------------------------Pages selection end-------------------------------------------






# --------------------------------------------Home section start-------------------------------------------

if selected == "Home":
    col1, col2 = st.columns(2,gap="medium",vertical_alignment= "top")
    with col2:
        st.title(" ")
        st.image("images/dp.png",width=300)
    with col1:
        st.title(" ")
        st.subheader("Hi :wave:")
        st.markdown(html_code_name, unsafe_allow_html=True)
        if st.button("📬Contact me!"):
            cont()
         
        
    st.write("---")
    # about me -------
    st.title("🚀 About Me")
    st.markdown(
        '''
        <style>
            .justified-text {
                text-align: justify;
            }
        </style>
        <div class="justified-text">
            As an passionate <span style="background-color: green;">Electronics and Communication</span> Engineer with a strong focus 
            on IoT, embedded systems, and smart devices. Skilled in using development boards like 
            Arduino, Raspberry Pi, ESP8266, and ESP32, along with Python and C++. My innovative projects have been 
            recognized with government funding and awards in various competitions.
            <br><br>
            As an enthusiastic educator, I teach IoT, embedded systems, and PCB design to students globally (USA, Philippines, etc.) through 
            project-based learning. I thrive on creating practical, hands-on learning experiences that inspire and empower.
            <br><br>
            Let's innovate and build the future together! 🌟
        </div>
        ''', 
        unsafe_allow_html=True
    )

    # about me end -------------
    st.write("---")
    st.write(" ")
    # st.title("Shivansh's AI Bot")
    # st.subheader("Curious About Shivansh? 🤔 Ask me anything! 🗨️")
    # prompt = st.text_input("What's on your mind? 💭 just write here :point_down:","")
    # if st.button("ASK", use_container_width=400) : 
    #   ques = prompt
    #   response = model.generate_content(performa+'this is the question visitor ask'+ques)
    #   expander=st.expander("Answer")
    #   expander.write(response.text)
    # st.write(" ")  
    st.title("What I'm Doing")
    col1,col2,col3 = st.columns(3)
    st.write(" ")
    with col1:
        t1 =st.container(height=310)
        t1.header("PCB Designing")
        t1.image("images/pcb.png")
        t12 =st.container(height=310)
        t12.header("Embedded Sys.")
        t12.image("images/emb.png")       
    with col2:
        t2=st.container(height=310)
        t2.header("IoT Develop.")
        t2.image("images/iot.png")
        t21=st.container(height=310)
        t21.header("Trainer")
        t21.image("images/tc.png")
    with col3:    
        t3= st.container(height=310)
        t3.header("3D Printing")
        t3.image("images/3drem.png")
        t31= st.container(height=310)
        t31.header("Computer Vision")
        t31.image("images/eye.png") 
    st.write("---")
    st.write(" ")
    st.title(":red[Checkout My Youtube]")
    st.write(" ")
    col1,col2 = st.columns(2,gap="large")
    with col1:

        st.header("'Electronics noob'")
        st.write("")

        st.subheader("Channel link :point_down:")
        st.link_button("Go to Youtube","https://youtube.com/@electronicsnoob?si=YydMrmLal3k5RsWK",use_container_width=270)
        st.write("")
        st.write(":point_right:  :red[Content Focus:] *Tutorials and projects related to electronics and embedded systems.*")
        st.write(":point_right:  :red[Target Audience:] *Beginners and enthusiasts interested in learning electronics.*")
        st.markdown(''':point_right:  :red[Video Types:]"  
                    *:red_circle: Step-by-step guides on building electronic projects.  
                     :red_circle: Demonstrations of various electronic components and modules.  
                     :red_circle: Coding tutorials related to microcontrollers such as Arduino and Raspberry Pi.*''')



    with col2:
        st.video("https://youtu.be/RNbX_6oACS0?si=n1Po6FXXobvNoqaA")
        st.video("https://youtu.be/wTDsaaoLAdo?si=HShryxhvBDBLkFO8")
        

# --------------------------------------------Home section end--------------------------------------------------




# --------------------------------------------Resume section start----------------------------------------------

elif selected == "Resume":
    click = False
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open("images/dp.png")


    # --- HERO SECTION ---
    col1, col2 = st.columns(2,gap="small",vertical_alignment="center")
    with col1:
        st.image(profile_pic, width=270)

    with col2:
        
        st.header(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name="shivansh_Iot_Embedded_resume.pdf",
            mime="application/octet-stream",on_click=downRes)
        
        st.write("📫", EMAIL)


    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qulifications")
    st.write(
        """
    - ✔️ Bachelors Degree in :green-background[ECE] from Moradabad Institute Of Technology
    - ✔️ Completed Bachelors with Aggregate of 8.2 CGPA
    - ✔️ Good understanding of Electronics fundamentals and Advanced Technologies
    - ✔️ Excellent in hand project experience on :green-background[Embedded, IoT and PCB Designing] 
    """
    )


    # --- SKILLS ---
    st.write('\n')
    st.subheader("🛠️ Skills & Expertise")
    st.write(
        """
    - 👩‍💻 :blue-background[Programming:]      :green[Python (Opencv), Embedded C/C++]
    - 📊 :blue-background[Microcontrollers:] :green[Arduino, Esp32, Esp8266, Raspberrypi, Stm(learning, beginer)]
    - 📚 :blue-background[Modeling:]         :green[Fusion360]
    - 🗄️ :blue-background[PCB Designig:]     :green[Ki-Cad, Eagle(Autodesk), Easyeda]
    """
    )



    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("📈 Professional Experience")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Hardware Engineer**")
    st.write("June23 - Present")
    st.write(
        """
    - ► Worked with 5g enabled system  modules for LBTS and BTS
    - ► Responsible for debugging, troubleshooting and testing of multilayer pcbs  
    - ► Engaging and coordination with Multiple teams like R&D and QC. 
    """
    )

    # --- JOB 2
    st.write('\n')
    st.write("🚧", "**Freelancer & Educator**")
    st.write("Online")
    st.write(
        """

    - ► I teach IoT, embedded systems, and PCB designing through project-based learning.
    - ► I make projects based on client requirement 
    """
    )

    # --- JOB 3
    st.write('\n')
    st.write("🚧", "**PCB Department (Intern)**")
    st.write("Jul22 - Aug22")
    st.write(
        """
    - ► Surya Roshini pvt. ltd is India's leading Led manufacturing company with global presence
    - ► Worked in SMD and Manual PCB assembling sections 
    - ► learned and worked with Pcb fabrication, component soldering and component selection 
    """
    )


    # --- Projects & Accomplishments ---
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")



elif selected == "Contact":
 with st.container():
  st.header("Contact Me!📬",divider=True)
  components.html("""<div class="container" style="max-width: 700px; margin: 0 auto; padding: 20px; background-color: #f8f9fa; border-radius: 10px; box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.1);">
  <h1 style="text-align: center; color: #343a40; margin-bottom: 20px;">Contact Me</h1>
  <form target="_blank" action="https://formsubmit.co/shivanshchauhan.228@gmail.com" method="POST">
    <div class="form-group">
      <div class="form-row" style="display: flex; gap: 10px;">
        <div class="col" style="flex: 1;">
          <input type="text" name="name" class="form-control" placeholder="Full Name" required style="padding: 10px; border-radius: 5px; border: 1px solid #ced4da;">
        </div>
        <div class="col" style="flex: 1;">
          <input type="email" name="email" class="form-control" placeholder="Email Address" required style="padding: 10px; border-radius: 5px; border: 1px solid #ced4da;">
        </div>
      </div>
    </div>
    <div class="form-group" style="margin-top: 15px;">
      <textarea placeholder="Your Message" class="form-control" name="message" rows="5" required style="width: 97%; padding: 10px; border-radius: 5px; border: 1px solid #ced4da;"></textarea>
    </div>
    <button type="submit" class="btn btn-lg btn-dark btn-block" style="background-color: #0dedc0; color: #ffffff; padding: 12px; border: none; border-radius: 5px; width: 100%; margin-top: 20px;">Submit Form</button>
  </form>
</div>
""",width=750, height=400)





 with st.container():
     st.header("Location 📍",divider=True)

     google_map_url = """
     <<div style="border: 2px solid #4CAF50; border-radius: 10px; box-shadow: 0px 0px 20px #FFFFFF; overflow: hidden;">
<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1747.636249576419!2d78.7535779!3d28.8307461!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390afbf35076ff39%3A0x776f6777e59bbce6!2s825%2C%20Prakash%20Nagar%2C%20Prem%20Nagar%2C%20Line%20Par%2C%20Moradabad%2C%20Uttar%20Pradesh%20244001!5e0!3m2!1sen!2sin!4v1723144200234!5m2!1sen!2sin" width="700" height="480" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>"""

     components.html(google_map_url, width=700, height=500)