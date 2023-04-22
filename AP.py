import streamlit as st
import json
import pandas as pd
import streamlit as st
import calendar
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import random 


#Hauptseite

#Hauptseite

def main():
    st.write('<style>h1{ text-align: center; }</style>', unsafe_allow_html=True)
    Titel = st.title("To Do List")
    
    st.markdown("<h2 style='text-align: center; font-size: 15px;'>Heute: " + datetime.today().strftime('%Y-%m-%d') + "</h2>", unsafe_allow_html=True)
    
    menu = ["Main", "Statistiken", "Test"]
    choice = st.selectbox("Menu", menu)
    
    if choice == "Main":

        col1,col2 = st.columns(2)
        
        #Für das schreiben der Aufgabe
        with col1:
            task = st.text_area("Aufgabe")

        with col2:
            Wochentag = st.selectbox("Wochentag",["Montag", "Dienstag", "Mittwoch", "Donnerstag","Freitag", "Samstag", "Sonntag"])
    
        if not 'todolist_montag' in st.session_state:
            st.session_state.todolist_montag = []
        if not 'todolist_dienstag' in st.session_state:
            st.session_state.todolist_dienstag = []
        if not 'todolist_mittwoch' in st.session_state:
            st.session_state.todolist_mittwoch = []
        if not 'todolist_donnerstag' in st.session_state:
            st.session_state.todolist_donnerstag = []
        if not 'todolist_freitag' in st.session_state:
            st.session_state.todolist_freitag = []
        if not 'todolist_samstag' in st.session_state:
            st.session_state.todolist_samstag = []
        if not 'todolist_sonntag' in st.session_state:
            st.session_state.todolist_sonntag = []
    
        if st.button("add"):
            if Wochentag == "Montag":
                st.session_state.todolist_montag.append(task)
            elif Wochentag == "Dienstag":
                st.session_state.todolist_dienstag.append(task)
            elif Wochentag == "Mittwoch":
                st.session_state.todolist_mittwoch.append(task)
            elif Wochentag == "Donnerstag":
                st.session_state.todolist_donnerstag.append(task)
            elif Wochentag == "Freitag":
                st.session_state.todolist_freitag.append(task)
            elif Wochentag == "Samstag":
                st.session_state.todolist_samstag.append(task)
            elif Wochentag == "Sonntag":
                st.session_state.todolist_montag.sonntag(task)


            
 

        #Ich habe hier die Wochentage in Tabellen aufgeteilt
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Montag", "Dienstag", "Mittwoch", "Donnerstag","Freitag", "Samstag", "Sonntag",])
           
       #c steht für conatiner, die buchstaben danach für die jeweilige woche 
        with tab1:
            if Wochentag == "Montag":
                cm = st.container()
                for i, task in enumerate(st.session_state.todolist_montag):
                    cm.checkbox(label=f'{task}', key=i)
        
        with tab2:
            cdi = st.container()
            if Wochentag == "Dienstag":
                for i, task in enumerate(st.session_state.todolist_dienstag):
                    cdi.checkbox(label=f'{task}', key=i)
        
        with tab3:
            cmi = st.container()
            if Wochentag == "Mittwoch":
                for i, task in enumerate(st.session_state.todolist_mittwoch):
                    cmi.checkbox(label=f'{task}', key=i)
        with tab4:
            cdo = st.container()
            if Wochentag == "Donnerstag":
                for i, task in enumerate(st.session_state.todolist_donnerstag):
                    cdo.checkbox(label=f'{task}', key=i)
        with tab5:
            cfr= st.container()
            if Wochentag == "Freitag":
                for i, task in enumerate(st.session_state.todolist_freitag):
                    cfr.checkbox(label=f'{task}', key=i)
        with tab6:
            csa = st.container()
            if Wochentag == "Samstag":
                for i, task in enumerate(st.session_state.todolist_Samstag):
                    csa.checkbox(label=f'{task}', key=i)
        with tab7:
            cso = st.container()
            if Wochentag == "Sonntag":
                for i, task in enumerate(st.session_state.todolist_sonntag):
                    cso.checkbox(label=f'{task}', key=i)
        
        
        
        
        #my_list = st.session_state.todolist
        
        # Füge einen "Delete" Button hinzu
        if st.button("Aufgaben löschen"):
            # Lösche alle Einträge in der To-Do-Liste
            st.session_state.todolist_montag = []
            st.session_state.todolist_dienstag = []
            st.session_state.todolist_mittwoch = []
            st.session_state.todolist_donnerstag = []
            st.session_state.todolist_freitag = []
            st.session_state.todolist_samstag = []
            st.session_state.todolist_sonntag = []
            
        st.checkbox('Json hinzufügen')
        st.checkbox('Gameification -> Animation')
        st.checkbox('Delet Button ausbessern')
        st.checkbox('Design allgemein')
        st.checkbox('Gnaueri und evt meh statistike')
            
     
        
    elif choice == "Statistiken":
        # CSS für Textausrichtung und Positionierung
        style = """
        <style>
            .text-centered {
                st.subheader("Statistik")
                display: flex;
                justify-content: center;
                align-items: center;
                height: 12vh;
                text-align: center;
                }
            </style>
            """

        # Streamlit-Anwendung
        st.markdown(style, unsafe_allow_html=True)
        st.markdown("<div class='text-centered'> <h2>Statistik</h2></div>", unsafe_allow_html=True)
        
        A,B = st.columns(2)
        
        def my_widget(label, default_value):
            return st.sidebar.slider(label, 0, 100, default_value)
        
        with A:
            Pause = st.number_input('Pause', value = 1.0)
            
        with B:
            Arbeit = st.number_input('Arbeit', value = 1.0)

        st.empty()
        st.empty()
        st.empty()
        st.empty()
        st.empty()
        st.empty()

        Chart1, Chart2 = st.columns(2)
        
        with Chart1:
            fig, ax = plt.subplots()
            ax.bar(['Pause', 'Arbeit'], [Pause, Arbeit])
            ax.set_ylabel('Stunden')
            ax.set_title('Bar Plot')
        
            # Display the plot in Streamlit
            st.pyplot(fig)
        

        with Chart2:
            total_Pause_hours = Pause
            total_Arbeit_hours = Arbeit
            
            Pause_hours_percent = (total_Pause_hours /24) * 100
            Arbeit_hours_percent = (total_Arbeit_hours /24) * 100
            

            labels = ['Pause', 'Arbeit']
            sizes = [Pause_hours_percent, Arbeit_hours_percent] # Größen der Sektoren in Prozent

            # Pie-Chart erstellen
            
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Sorgt dafür, dass das Diagramm kreisförmig ist
            ax.set_title('Verteilung der Arbeits- und Pausenzeiten')

            # Diagramm in Streamlit anzeigen
            st.pyplot(fig)
          
            
        if Pause < 1.0 and Arbeit > 8.0:
            Text = 'Du hast mehr gearbeitet und weniger Pause gemacht als per ORF erlaubt wäre'
            info_text = ('Arbeitswissenschaftliche Empfehlungen: Die tägliche Arbeitszeit sollte etwa 8 Stunden liegen und 10 Stunden nicht überschreiten. Die wöchentliche Arbeitszeit sollte im Durchschnitt 40 Stunden nicht überschreiten und eher auf fünf als auf sechs Arbeitstage verteilt werden. Pausen sollten genommen werden, bevor ein Gefühl der Erschöpfung eintritt. Mehrere kurze Pausen statt einer langen sind zu empfehlen.')
             
            st.markdown(
                """
                <style>
                .info-box {
                    background-color: light yellow;
                    }
                </style>
                """,
                unsafe_allow_html=True
                )
            
            with  st.container():
                st.info(Text)
                st.info(info_text)
                st.markdown("---")
                
            
    elif choice == "Test":
            st.subheader("Testing")
            
            
            import random 
  
            class flashcard: 
                def __init__(self): 
        
                    self.fruits={'apple':'red', 
                     'orange':'orange', 
                     'watermelon':'green', 
                     'banana':'yellow'} 
          
                def quiz(self): 
                    while (True): 
            
                        fruit, color = random.choice(list(self.fruits.items())) 
                        print("What is the color of {}".format(fruit)) 
                        user_answer = input()    
                        if(user_answer.lower() == color): 
                            print("Correct answer") 
                        else: 
                            print("Wrong answer") 
                  
                        option = int(input("enter 0 , if you want to play again : ")) 
                        if (option): 
                            break
  
                    print("welcome to fruit quiz ") 
                    fc=flashcard() 
                    fc.quiz()

            
            
                     
if __name__ == '__main__':
	main()