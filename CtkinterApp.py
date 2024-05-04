from datetime import date
from Human import Human
import customtkinter
import tkinter as tk
import sys
import math

class Ctkinter_App():  
   
    def __init__(self):
        self.root = customtkinter.CTk()    
        self.open_main_window()
        self.root.mainloop()  

    def open_main_window(self): 
        
        # specify window dimensions
        window_width = 850
        window_height = 900
        
        # Setting-up mode and theme
        customtkinter.set_appearance_mode("System")  
        customtkinter.set_default_color_theme("blue")  
        
        # establish main window characteristics
        self.root.title(f"BMR & BMI Calculator App | {date.today()}")
        self.root.geometry(f"{window_width}x{window_height}+400+160")
        self.root.resizable(False, False)    
        
        # window closing protocol
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Root Frame configuration
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=2)
        
        # Frame initialization
        self.sidebar_frame = customtkinter.CTkFrame(self.root, 
                                                    width = 130,
                                                    fg_color="transparent",
                                                    corner_radius=0)
        self.working_frame = customtkinter.CTkFrame(self.root, 
                                                    corner_radius=0)
        self.title_frame = customtkinter.CTkFrame(self.working_frame, 
                                                  fg_color="transparent")
        self.input_frame = customtkinter.CTkFrame(self.working_frame, 
                                                  corner_radius=0, 
                                                  fg_color="transparent")
        self.output_frame = customtkinter.CTkFrame(self.working_frame, 
                                                   corner_radius=0, 
                                                   fg_color="transparent")
        
        # Frame configuration
        self.sidebar_frame.grid_columnconfigure(0, weight=1)
        self.sidebar_frame.grid_rowconfigure(3, weight=1)

        # block frame grid propagation (resizing)
        self.sidebar_frame.grid_propagate(0) 
        self.working_frame.grid_propagate(0) 

        # Frame placement
        self.sidebar_frame.grid(row=0, column=0, sticky="news")
        self.working_frame.grid(row=0, column=1, sticky="news")
        self.title_frame.grid(row=0, column=0, sticky="news")
        self.input_frame.grid(row=1, column=0, sticky="news")
        self.output_frame.grid(row=2, column=0, sticky="news")
        
        # Widget initialization
        self.app_title = customtkinter.CTkLabel(self.sidebar_frame, 
                                                text="Body Tracker App", 
                                                fg_color="transparent", 
                                                text_color=("black", "white"), 
                                                font = ("Helvetica", 30))
        
        self.bmr_calculator_button = customtkinter.CTkButton(master=self.sidebar_frame,
                                                             corner_radius=0,
                                                             height = 70,
                                                             text="BMR Calculator", 
                                                             text_color= "white", 
                                                             font = ("Helvetica", 20),
                                                             command = self.bmr_button_command)
        
        self.bmi_calculator_button = customtkinter.CTkButton(master=self.sidebar_frame, 
                                                             corner_radius=0,
                                                             height = 70,
                                                             text="BMI Calculator",
                                                             text_color= "white", 
                                                             font = ("Helvetica", 20),
                                                             command = self.bmi_button_command)
        
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, 
                                                                       values=["Light", "Dark"],
                                                                       font = ("Helvetica", 15),
                                                                       anchor="center",
                                                                       command=self.change_appearance_mode_event)
        
        # Widget placement
        self.app_title.grid(row=0, column=0, pady = (30, 10), sticky="new")
        self.bmr_calculator_button.grid(row=1, column=0, pady = (30, 0), sticky="ew")
        self.bmi_calculator_button.grid(row=2, column=0, pady = (0, 0), sticky="ew")
        self.appearance_mode_optionemenu.grid(row=3, column=0, pady = 20, sticky="s")
    
    
    def bmr_button_command(self): 
        self.clear_frames(self.title_frame, self.input_frame, self.output_frame)
        self.open_bmr_calculator()
    
    
    def bmi_button_command(self): 
        self.clear_frames(self.title_frame, self.input_frame, self.output_frame)
        self.open_bmi_calculator()
    
    
    def open_bmr_calculator(self): 
    
        def equation_on_select(event): 
            
            if self.input_equation.get() in ["Katch-McArdle", "Cunningham"]: 
                try:
                    # Attempt to access the attributes
                    self.body_fat_pct_title
                    self.input_body_fat_pct
                except AttributeError:
                    self.body_fat_pct_value = customtkinter.StringVar() 
                    
                    self.body_fat_pct_title = customtkinter.CTkLabel(self.input_frame, 
                                                                     width = 170,
                                                                     text="*Body Fat (%):", 
                                                                     fg_color="transparent", 
                                                                     text_color=("black", "white"), 
                                                                     font = ("Helvetica", 18))
                    self.input_body_fat_pct = customtkinter.CTkEntry(self.input_frame, 
                                                                     textvariable = self.body_fat_pct_value)
                    
                    self.body_fat_pct_title.grid(row=7, column=0, padx=10, pady=(0, 20))
                    self.input_body_fat_pct.grid(row=7, column=1, padx=10, pady=(0, 20))
           
            else:
                try:
                    # Attempt to access the attributes
                    self.body_fat_pct_title
                    self.input_body_fat_pct
                except AttributeError:
                    pass
                else:
                    self.body_fat_pct_title.destroy()
                    self.input_body_fat_pct.destroy()
                    delattr(self, "body_fat_pct_title")
                    delattr(self, "input_body_fat_pct")
           
        input_field_width = 200   

        # Input variable initialization
        self.age_value = tk.StringVar() 
        self.height_value = tk.StringVar() 
        self.weight_value = tk.StringVar() 
        self.equation_value = tk.StringVar()
        self.body_fat_pct_value = tk.StringVar() 
        
        # Widget initialization        
        self.title_label = customtkinter.CTkLabel(self.title_frame, 
                                                  text="BMR (Basal Metabolic Rate) Calculator", 
                                                  fg_color="transparent", 
                                                  text_color=("black", "white"), 
                                                  font = ("Helvetica", 28, "bold"))
        
        self.gender_title = customtkinter.CTkLabel(self.input_frame, 
                                                   text="Gender:", 
                                                   fg_color="transparent", 
                                                   text_color=("black", "white"), 
                                                   font = ("Helvetica", 18))
        
        self.input_gender = customtkinter.CTkOptionMenu(self.input_frame, 
                                                        width = input_field_width,
                                                        values = ["male", "female"], 
                                                        anchor = "center",
                                                        font = ("Helvetica", 18),
                                                        text_color= "white")
        
        self.age_title = customtkinter.CTkLabel(self.input_frame, 
                                                text="Age:", 
                                                fg_color="transparent", 
                                                font = ("Helvetica", 18),
                                                text_color=("black", "white")) 
        
        self.input_age = customtkinter.CTkEntry(self.input_frame, 
                                                width = input_field_width,
                                                font = ("Helvetica", 18),
                                                text_color=("black", "white"),
                                                textvariable = self.age_value)  
        
        self.unit_title = customtkinter.CTkLabel(self.input_frame, 
                                                text="Units:", 
                                                fg_color="transparent", 
                                                font = ("Helvetica", 18),
                                                text_color=("black", "white"))
        
        self.input_unit = customtkinter.CTkOptionMenu(self.input_frame, 
                                                      width = input_field_width,
                                                      values = ["metric [kg, cm]", "imperial [lb, ft]"], 
                                                      font = ("Helvetica", 18),
                                                      text_color = "white",
                                                      anchor = "center")
        
        self.height_title = customtkinter.CTkLabel(self.input_frame, 
                                                text="Height:", 
                                                fg_color="transparent", 
                                                text_color=("black", "white"), 
                                                font = ("Helvetica", 18))
        
        self.input_height = customtkinter.CTkEntry(self.input_frame,
                                                   width = input_field_width,
                                                   font = ("Helvetica", 18),
                                                   text_color=("black", "white"),
                                                   textvariable = self.height_value)
        
        self.weight_title = customtkinter.CTkLabel(self.input_frame, 
                                                text="Weight:", 
                                                fg_color="transparent", 
                                                text_color=("black", "white"), 
                                                font = ("Helvetica", 18))
        
        self.input_weight = customtkinter.CTkEntry(self.input_frame,
                                                   width = input_field_width,
                                                   font = ("Helvetica", 18),
                                                   text_color=("black", "white"),
                                                   textvariable = self.weight_value)
        
        
        self.activity_level_title = customtkinter.CTkLabel(self.input_frame, 
                                                           text="Activity Level:", 
                                                           fg_color="transparent", 
                                                           text_color=("black", "white"), 
                                                           font = ("Helvetica", 18))
        
        self.input_activity_level = customtkinter.CTkOptionMenu(self.input_frame, 
                                                                width = input_field_width,
                                                                values=["sedentary", 
                                                                        "lightly active",
                                                                        "moderatetely active",
                                                                        "very active",
                                                                        "extra active"], 
                                                                font = ("Helvetica", 18),
                                                                text_color= "white",
                                                                anchor = "center")
        
        self.equation_title = customtkinter.CTkLabel(self.input_frame, 
                                                     text="BMR Equation:", 
                                                     fg_color="transparent", 
                                                     text_color=("black", "white"), 
                                                     font = ("Helvetica", 18))
        
        self.input_equation = customtkinter.CTkOptionMenu(self.input_frame, 
                                                          width = input_field_width,
                                                          values=["Harris-Benedict", 
                                                                  "Harris Benedict (Revised)",
                                                                  "Mifflin-St Jeor",
                                                                  "Schofield",
                                                                  "Oxford", 
                                                                  "Katch-McArdle",
                                                                  "Cunningham"], 
                                                          font = ("Helvetica", 18),
                                                          text_color= "white",
                                                          anchor = "center")
        
        self.body_fat_pct_title = customtkinter.CTkLabel(self.input_frame, 
                                                         text="*Body Fat Percenage:", 
                                                         fg_color="transparent", 
                                                         text_color=("black", "white"), 
                                                         font = ("Helvetica", 18))
        
        self.input_body_fat_pct = customtkinter.CTkEntry(self.input_frame, 
                                                         width = input_field_width,
                                                         textvariable = self.body_fat_pct_value,
                                                         font = ("Helvetica", 18),
                                                         text_color=("black", "white"))
        
        self.note_label = customtkinter.CTkLabel(self.input_frame, 
                                                 text="*For 'Katch-McArdle' and 'Cunningham' equations only.", 
                                                 fg_color="transparent", 
                                                 text_color=("black", "white"), 
                                                 font = ("Helvetica", 15))
        
        self.run_button = customtkinter.CTkButton(master=self.input_frame,
                                                  corner_radius=5,
                                                  width = 200,
                                                  height = 70,
                                                  hover_color = "#003400",
                                                  fg_color= "green",
                                                  text="RUN Calculator", 
                                                  text_color="white", 
                                                  font = ("Helvetica", 20),
                                                  command = self.run_bmr_calculator)
        
        # Widget placement
        self.title_label.grid(row=0, column=0, columnspan = 2, padx=20, pady=(20, 10), sticky = "ew")
        self.gender_title.grid(row=0, column=0, padx=10, pady=(30, 20), sticky = "e")
        self.input_gender.grid(row=0, column=1, padx=10, pady=(30, 20))
        self.age_title.grid(row=1, column=0, padx=10, pady=(0, 20), sticky = "e")
        self.input_age.grid(row=1, column=1, padx=10, pady=(0, 20))
        self.unit_title.grid(row=2, column=0, padx=10, pady=(0, 20), sticky = "e")
        self.input_unit.grid(row=2, column=1, padx=10, pady=(0, 20))
        self.height_title.grid(row=3, column=0, padx=10, pady=(0, 20), sticky = "e")
        self.input_height.grid(row=3, column=1, padx=10, pady=(0, 20))
        self.weight_title.grid(row=4, column=0, padx=10, pady=(0, 20), sticky = "e")
        self.input_weight.grid(row=4, column=1, padx=10, pady=(0, 20))
        self.activity_level_title.grid(row=5, column=0, padx=10, pady=(0, 20), sticky = "e")
        self.input_activity_level.grid(row=5, column=1, padx=10, pady=(0, 20))
        self.equation_title.grid(row=6, column=0, padx=10, pady=(0, 20), sticky = "e")
        self.input_equation.grid(row=6, column=1, padx=10, pady=(0, 20))
        self.body_fat_pct_title.grid(row=7, column=0, padx=10, pady=(0, 20), sticky = "e")
        self.input_body_fat_pct.grid(row=7, column=1, padx=10, pady=(0, 20))
        self.note_label.grid(row=8, column=0, columnspan = 2, padx=10, pady=(0, 20), sticky = "w")
        self.run_button.grid(row=9, column=0, columnspan = 2, padx=10, pady=(20, 20))
        
        
        
    def open_bmi_calculator(self): 
        input_field_width = 230
        
        # Input variable initialization
        self.height_value = tk.StringVar() 
        self.weight_value = tk.StringVar() 
        
        # Widget initialization
        self.title_label = customtkinter.CTkLabel(self.title_frame, 
                                                  text="BMI (Body Mass Index) Calculator", 
                                                  fg_color="transparent", 
                                                  text_color=("black", "white"), 
                                                  font = ("Helvetica", 28, "bold"))
        
        self.unit_title = customtkinter.CTkLabel(self.input_frame, 
                                                text="Units:".rjust(20, " "), 
                                                fg_color="transparent", 
                                                font = ("Helvetica", 18),
                                                text_color=("black", "white"))
        
        self.input_unit = customtkinter.CTkOptionMenu(self.input_frame, 
                                                      width = input_field_width,
                                                      values = ["metric [kg, cm]", "imperial [lb, ft]"], 
                                                      font = ("Helvetica", 18),
                                                      text_color = "white",
                                                      anchor = "center")
        
        self.height_title = customtkinter.CTkLabel(self.input_frame, 
                                                   text="Height:".rjust(20, " "), 
                                                   fg_color="transparent", 
                                                   text_color=("black", "white"), 
                                                   font = ("Helvetica", 18))
        
        self.input_height = customtkinter.CTkEntry(self.input_frame,
                                                   width = input_field_width,
                                                   font = ("Helvetica", 18),
                                                   text_color=("black", "white"),
                                                   textvariable = self.height_value)
        
        self.weight_title = customtkinter.CTkLabel(self.input_frame, 
                                                text="Weight:".rjust(20, " "), 
                                                fg_color="transparent", 
                                                text_color=("black", "white"), 
                                                font = ("Helvetica", 18))
        
        self.input_weight = customtkinter.CTkEntry(self.input_frame,
                                                   width = input_field_width,
                                                   font = ("Helvetica", 18),
                                                   text_color=("black", "white"),
                                                   textvariable = self.weight_value)
        
        self.run_button = customtkinter.CTkButton(master=self.input_frame,
                                                  corner_radius=5,
                                                  width = 200,
                                                  height = 70,
                                                  hover_color = "#003400",
                                                  fg_color= "green",
                                                  text="RUN Calculator", 
                                                  text_color="white", 
                                                  font = ("Helvetica", 20),
                                                  command = self.run_bmi_calculator)
        
        # Widget placement
        self.title_label.grid(row=0, column=0, columnspan = 2, padx=20, pady=(20, 10), sticky = "ew")
        self.unit_title.grid(row=1, column=0, padx=10, pady=(30, 20), sticky = "e")
        self.input_unit.grid(row=1, column=1, padx=10, pady=(30, 20))
        self.height_title.grid(row=2, column=0, padx=10, pady=(0, 20), sticky = "e")
        self.input_height.grid(row=2, column=1, padx=10, pady=(0, 20))
        self.weight_title.grid(row=3, column=0, padx=10, pady=(0, 20), sticky = "e")
        self.input_weight.grid(row=3, column=1, padx=10, pady=(0, 20))
        self.run_button.grid(row=4, column=0, columnspan = 2, padx=10, pady=(20, 20))
    
    
    def run_bmr_calculator(self):
        if self.bmr_input_validation():
         
            # get the units
            if self.input_unit.get() == "metric [kg, cm]":
                h_unit = "cm"
                w_unit = "kg"
            else: 
                h_unit = "ft"
                w_unit = "lb"
            
            try:
                self.body_fat_pct_value
            except AttributeError:
                self.body_fat_pct_value = None
                
            # create human_test instance of Human class
            human_test = Human(gender = self.input_gender.get(),
                               age = self.age_value, 
                               height_unit = h_unit, 
                               weight_unit = w_unit, 
                               height = self.height_value, 
                               weight = self.weight_value, 
                               activity_level = self.input_activity_level.get(),
                               bmr_equation = self.equation_value,
                               body_fat_pct = self.body_fat_pct_value)
            
            # run required Human class methods to elaborate results
            human_test.calculate_bmr()
            human_test.calculate_caloric_need()
            
            self.results_title = customtkinter.CTkLabel(self.output_frame, 
                                                        text="Results", 
                                                        fg_color="transparent", 
                                                        text_color=("black", "white"), 
                                                        font = ("Helvetica", 30, "bold"))
            self.result = customtkinter.CTkLabel(self.output_frame, 
                                                 text=f"BMR: {math.ceil(human_test.bmr)} kcal/day\nDaily Caloric Need for current Activity Level: {math.ceil(human_test.daily_caloric_need)} kcal/day", 
                                                 fg_color="transparent", 
                                                 font = ("Helvetica", 18),
                                                 text_color=("black", "white"))
            
            self.results_title.grid(row = 0, column = 0, columnspan = 2, padx=10, pady=(20, 20), sticky = "news")
            self.result.grid(row = 1, column = 0, columnspan = 2, padx=20, pady=(10, 20), sticky = "news")
            
            
    def run_bmi_calculator(self):
        if self.bmi_input_validation():
         
            # get the units
            if self.input_unit.get() == "metric [kg, cm]":
                h_unit = "cm"
                w_unit = "kg"
            else: 
                h_unit = "ft"
                w_unit = "lb"
            
            try:
                self.body_fat_pct_value
            except AttributeError:
                self.body_fat_pct_value = None
                
            # create human_test instance of Human class
            human_test = Human(gender = "unknown",
                               age = 100, 
                               height_unit = h_unit, 
                               weight_unit = w_unit, 
                               height = self.height_value, 
                               weight = self.weight_value, 
                               activity_level = "unknown",
                               bmr_equation = "unknown",
                               body_fat_pct = 1)
            
            # run required Human class methods to elaborate results
            human_test.calculate_bmi()
            human_test.classify_bmi()
            
            self.results_title = customtkinter.CTkLabel(self.output_frame, 
                                                        text="Results", 
                                                        fg_color="transparent", 
                                                        text_color=("black", "white"), 
                                                        font = ("Helvetica", 30, "bold"))
            self.result = customtkinter.CTkLabel(self.output_frame, 
                                                 text=f"BMI: {human_test.bmi} kg/m²\nBMI Classification: {human_test.bmi_classification}", 
                                                 fg_color="transparent", 
                                                 text_color=("black", "white"), 
                                                 font = ("Helvetica", 18))
            
            self.results_title.grid(row = 0, column = 0, columnspan = 2, padx=10, pady=(20, 20), sticky = "news")
            self.result.grid(row = 1, column = 0, columnspan = 2, padx=20, pady=(10, 20), sticky = "news")
            

    def bmr_input_validation(self): 
        
        try: 
            self.age_value = int(self.input_age.get())
        except:
            tk.messagebox.showerror(title = "Error", 
                                    message = "The age must be a number.", 
                                    icon = 'error')
            return False
        else: 
            if self.age_value < 0: 
                tk.messagebox.showerror(title = "Error", 
                                        message = "The age must be non-negative.", 
                                        icon = 'error')
                return False
        
        try: 
            self.height_value = int(self.input_height.get())
        except:
            tk.messagebox.showerror(title = "Error", 
                                    message = "The height must be a number.", 
                                    icon = 'error')
            return False
        else: 
            if self.height_value < 0: 
                tk.messagebox.showerror(title = "Error", 
                                        message = "The height must be non-negative.", 
                                        icon = 'error')
                return False
        
        try: 
            self.weight_value = int(self.input_weight.get())
        except:
            tk.messagebox.showerror(title = "Error", 
                                    message = "The weight must be a number.", 
                                    icon = 'error')
            return False
        else: 
            if self.height_value < 0: 
                tk.messagebox.showerror(title = "Error", 
                                        message = "The weight must be non-negative.", 
                                        icon = 'error')
                return False
        
        self.equation_value = str(self.input_equation.get())
        
        if self.input_equation.get() in ["Katch-McArdle", "Cunningham"]:
            
            if self.input_body_fat_pct.get() == "":
                tk.messagebox.showerror(title = "Error", 
                                        message = "For this equation the body fat percentage must be a specified.", 
                                        icon = 'error')
                return False
        
            try: 
                self.body_fat_pct_value = float(self.input_body_fat_pct.get())
            except:
                tk.messagebox.showerror(title = "Error", 
                                        message = "The body fat percentage must be a number.", 
                                        icon = 'error')
                return False
            else: 
                if self.body_fat_pct_value <= 0 or self.body_fat_pct_value >= 1: 
                    tk.messagebox.showerror(title = "Error", 
                                            message = "The body fat percentage must be between 0 and 1.", 
                                            icon = 'error')
                    return False
        
        return True
        
        
    def bmi_input_validation(self): 

        try: 
            self.height_value = int(self.input_height.get())
        except:
            tk.messagebox.showerror(title = "Error", message = "The height must be a number.", icon = 'error')
            return False
        else: 
            if self.height_value < 0: 
                tk.messagebox.showerror(title = "Error", message = "The height must be non-negative.", icon = 'error')
                return False
        
        try: 
            self.weight_value = int(self.input_weight.get())
        except:
            tk.messagebox.showerror(title = "Error", message = "The weight must be a number.", icon = 'error')
            return False
        else: 
            if self.height_value < 0: 
                tk.messagebox.showerror(title = "Error", message = "The weight must be non-negative.", icon = 'error')
                return False
        
        return True
    
    
    def clear_frames(self, *frames):
        for frame in frames:
            for widget in frame.winfo_children():
                widget.destroy()
    
    
    def clear_fields_entry_form(self):
        # delete the content of the data entry fields
        for widget in self.input_frame.winfo_children():
            if isinstance(widget, customtkinter.CTkEntry):
                widget.delete(0, tk.END)
    
    
    def on_closing(self):
        self.root.destroy()  # Close the tkinter window
        sys.exit()  # stop the script from running
        
        
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)