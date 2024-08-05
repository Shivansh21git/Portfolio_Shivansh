# # folder path ---------> C:\Users\Om enterprises\pyt-port

# --------------------------------------------import section start-------------------------------------------
import pathlib as Path
import streamlit as st
import google.generativeai as genai
from streamlit_option_menu import option_menu
from PIL import Image
# --------------------------------------------import section end------------------------------------

# ---------------------------------------------GENERAL SETTINGS ------------------------------------------


# ------------------css import start--------------------

# current_dir = "C:\Users\Om enterprises\pyt-port"

PAGE_TITLE = "Portfolio | Shivansh Chauhan"
PAGE_ICON = ":wave:"
NAME = "Shivansh Chauhan"
DESCRIPTION = """
IoT & Embedded enthusiast, Working hard to excel in Industry with my knowledge and 21 centuary skills.
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
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
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










'''


# --------------------------------------------Performa end-------------------------------------------




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
    st.success('Downloaded Successfully!',icon="✔")

         
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
        options=["Home", "Resume","Projects","Gallary","Contact"],
        icons=["house", "book", "phone"],
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
    col1, col2 = st.columns(2,gap='medium',vertical_alignment='center')
    with col1:
        st.title(" ")
        st.subheader("Hi :wave:")
        st.title(":rainbow[I am Shivansh Chauhan]")
        if st.button("📬Contact me!"):
            cont()
         
        
    with col2:
        st.title(" ")
        st.image("images/pc1.png",width=300)

    
    # about me -------
    st.title("About me")
    st.markdown(''':blue-background[As an :red[Electrical and Computer Engineering] (ECE) professional
                with a  strong focus on embedded systems and IoT, I am passionate about creating innovative solutions that push the boundaries of technology. With a solid background in designing and implementing smart electronic devices, I thrive on tackling complex challenges and driving technological advancements. My hands-on experience, combined with a commitment to continuous learning, allows me to contribute effectively 
                to cutting-edge projects and deliver impactful results. I am dedicated
                to leveraging my skills and knowledge to advance in the dynamic field
                of embedded systems and IoT.]''')
    

    # about me end -------------

    st.write(" ")
    st.title("Shivansh's AI Bot")
    st.subheader("Curious About Shivansh? 🤔 Ask me anything! 🗨️")
    prompt = st.text_input("What's on your mind? 💭 just write here :point_down:","")
    if st.button("ASK", use_container_width=400) : 
      ques = prompt
      response = model.generate_content(performa+'this is the question visitor ask'+ques)
      expander=st.expander("Answer")
      expander.write(response.text)
    st.write(" ")  
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
    profile_pic = Image.open("images/pcwb.png")


    # --- HERO SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
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
    st.subheader("Hard Skills")
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
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Hardware Engineer**")
    st.write("June23 - Present")
    st.write(
        """
    - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
    - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
    - ► Redesigned data model through iterations that improved predictions by 12%
    """
    )

    # --- JOB 2
    st.write('\n')
    st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
    st.write("01/2018 - 02/2022")
    st.write(
        """
    - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
    - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
    - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
    """
    )

    # --- JOB 3
    st.write('\n')
    st.write("🚧", "**PCB Department (Intern)**")
    st.write("Jul22 - Aug22")
    st.write(
        """
    - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
    - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
    - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
    """
    )


    # --- Projects & Accomplishments ---
    st.write('\n')
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")

















elif selected == "Contact":
    st.title("Contact")
    if st.button("Email :"):
     st.markdown(f"""
    <script>
        window.location.href = "{mailto_link}";
    </script>
""", unsafe_allow_html=True)
    






