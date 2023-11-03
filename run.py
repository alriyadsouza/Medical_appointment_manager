import pandas as pd
from tkinter import *
from datetime import datetime, timedelta

# Your existing code

# Integration of Chat UI code
from tkinter import *
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

disease_specialty_map = {
    "Cardiologist": ["Coronary artery disease", "Arrhythmia"],
    "Dermatologist": ["Acne", "Eczema"],
    "Orthopedic Surgeon": ["Fractures", "Osteoarthritis"],
    "Gynecologist": ["Polycystic ovary syndrome (PCOS)", "Endometriosis"],
    "Neurologist": ["Migraine", "Multiple sclerosis"],
    "Psychiatrist": ["Depression", "Anxiety disorders"],
    "Oncologist": ["Chemotherapy", "Radiation therapy"],
    "Gastroenterologist": ["Irritable bowel syndrome (IBS)", "Gastroesophageal reflux disease (GERD)"],
    "Pediatrician": ["Childhood vaccinations", "Asthma in children"],
    "Ophthalmologist": ["Cataracts", "Glaucoma"]
}

questions = [
    "Hi! How can I assist you today? What is your gender?",
    "Great! Could you please tell me your age?" ,
    "What is your neighborhood?",
    "Another random question",
    "Do you have any scholarship? If yes, please provide the details.",
    "Please select your disease type from the options provided.",
]

def get_questions():
    for q in questions:
        yield q

question = get_questions()

def get_response(message):
    return next(question)

bot_name = "Sam"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        #self._ask_questions()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
     
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        question_number=0
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        question_number+=1
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
        
    def _ask_questions(self):
        Label(self.window, text='Welcome! Please provide the following details:').pack()

        Label(self.window, text='Gender:').pack()
        self.gender_entry = Entry(self.window)
        self.gender_entry.pack()

        Label(self.window, text='Age:').pack()
        self.age_entry = Entry(self.window)
        self.age_entry.pack()

        Label(self.window, text='Neighbourhood:').pack()
        self.neighborhood_entry = Entry(self.window)
        self.neighborhood_entry.pack()

        Label(self.window, text='Scholarship:').pack()
        self.scholarship_entry = Entry(self.window)
        self.scholarship_entry.pack()

        Label(self.window, text='Select Disease Type:').pack()
        self.variable = StringVar(self.window)
        self.variable.set("Select Disease")
        w = OptionMenu(self.window, self.variable, *sum(disease_specialty_map.values(), []))
        w.pack()

        Button(self.window, text="Book Appointment", command=self.book_appointment).pack()

    def book_appointment(self):
        gender = self.gender_entry.get()
        age = self.age_entry.get()
        neighborhood = self.neighborhood_entry.get()
        scholarship = self.scholarship_entry.get()
        selected_disease = self.variable.get()
        today = datetime.today()
        available_dates = [(today + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(14)]
        available_doctors = df[df['speciality'] == selected_disease]['Doctor_id'].unique()
        selected_date = available_dates[0]
        data = {
            'PatientId': [1],
            'AppointmentID': [1],
            'Gender': [gender],
            'ScheduledDay': [today.strftime('%Y-%m-%d')],
            'AppointmentDay': [selected_date],
            'Age': [age],
            'Neighbourhood': [neighborhood],
            'Scholarship': [scholarship],
            'Hipertension': [None],
            'Diabetes': [None],
            'Alcoholism': [None],
            'Handcap': [None],
            'SMS_received': [None],
            'No-show': [None],
            'Doctor_id': [None],
            'Doctor\'s Name': [None],
            'speciality': [selected_disease]
        }
        new_df = pd.DataFrame(data)
        new_df.to_csv('filtered_doc_details.csv', mode='a', header=False, index=False)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()