from BMRcalculator import BMRcalculator
from UnitTransform import UnitTransform
from BMIcalculator import BMIcalculator


class Human:
    
    def __init__(self, gender, age, height_unit, weight_unit, height, weight, activity_level, bmr_equation, body_fat_pct = None):
        self.gender = gender
        self.age = age
        self.height_unit = height_unit
        self.weight_unit = weight_unit

        if self.height_unit == "ft":
            self.height = UnitTransform.feet_to_cm(height) 
            self.height_unit = "cm"
        else:
            self.height = height

        if self.weight_unit == "lb":
            self.weight = UnitTransform.lbs_to_kg(weight) 
            self.weight_unit = "kg"
        else:
            self.weight = weight

        self.activity_level = activity_level
        self.bmr_equation = bmr_equation
        self.body_fat_pct = body_fat_pct


    def calculate_bmr(self):
        if self.bmr_equation in BMRcalculator.BMR_MAPPER:
            bmr_calculation_method = BMRcalculator.BMR_MAPPER[self.bmr_equation]
            
            if self.bmr_equation in ["Harris-Benedict", "Harris Benedict (Revised)", "Mifflin-St Jeor"]:
                self.bmr = bmr_calculation_method(self.gender, self.age, self.weight, self.height)
            elif self.bmr_equation in ["Schofield", "Oxford"]:
                self.bmr = bmr_calculation_method(self.gender, self.age, self.weight)
            else:   # self.bmr_equation in ["Katch-McArdle", "Cunningham"]
                self.lean_body_mass = BMRcalculator.calculate_lean_body_mass(self.weight, self.body_fat_pct)
                self.bmr = bmr_calculation_method(self.lean_body_mass)

        else:
            raise ValueError("Invalid BMR calculation method.")
    
    def calculate_caloric_need(self):
        self.daily_caloric_need = BMRcalculator.calculate_caloric_need(self.activity_level, self.bmr)
        
    def calculate_bmi(self):
        self.bmi = BMIcalculator.calculate_metric_BMI(self.height, self.weight)
        
    def classify_bmi(self):
        self.bmi_classification = BMIcalculator.bmi_classification(self.bmi)