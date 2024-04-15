
class BMRcalculator():
    """
    BMR Calculator will calculate your Basal Metabolic Rate (BMR); the 
    number of calories you'd burn if you stayed in bed all day.
    
    BMR_calculator class serves as a utility class that encapsulates the logic 
    for calculating the Basal Metabolic Rate (BMR). 
    It doesn't have any attributes of its own, but it provides a method 
    calculate_bmr that accepts parameters representing the 
    attributes of a human (weight, height, age, and gender).


    To determine your total daily calorie needs, multiply your BMR by the 
    appropriate activity factor, as follows:
        If you are sedentary (little or no exercise): Calorie-Calculation = BMR x 1.2
        If you are lightly active (light exercise/sports 1-3 days/week) : Calorie-Calculation = BMR x 1.375
        If you are moderatetely active (moderate exercise/sports 3-5 days/week) : Calorie-Calculation = BMR x 1.55
        If you are very active (hard exercise/sports 6-7 days a week) : Calorie-Calculation = BMR x 1.725
        If you are extra active (very hard exercise/sports & physical job or 2x training) : Calorie-Calculation = BMR x 1.9
    
    """   

    @staticmethod
    def calculate_lean_body_mass(weight, body_fat):
        return (1 - body_fat / 100) * weight


    @staticmethod
    def calculate_bmr_Harris_Benedict(gender, age, height, weight):
        if gender == "male": 
            return 66.4730 + (13.7516 * weight) + (5.0033 * height) - (6.7550 * age)
        else: 
            return 655.0955 + (9.5634 * weight) + (1.8496 * height) - (4.6756 * age)
         
    
    @staticmethod
    def calculate_bmr_Harris_Benedict_rev(gender, age, height, weight):
        if gender == "male": 
            return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else: 
            return 447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age)
        

    @staticmethod
    def calculate_bmr_Mifflin_St_Jeor(gender, age, height, weight):
        if gender == "male": 
            return (9.99 * weight) + (6.25 * height) - (4.92 * age) + 5
        else:
            return (9.99 * weight) + (6.25 * height) - (4.92 * age) - 161
        

    @staticmethod
    def calculate_bmr_Schofield(gender, age, weight):
        if gender == "male": 
            if 0 <= age < 3:
                return 59.512 * weight - 30.4
            if 3 <= age < 10:
                return 22.706 * weight + 504.3
            if 10 <= age < 18:
                return 17.686 * weight + 658.2
            if 18 <= age < 30:
                return 15.057 * weight + 692.2
            if 30 <= age < 69:
                return 11.472 * weight + 873.1
            else:
                return 11.711 * weight + 587.7   
        else:
            if 0 <= age < 3:
                return 58.317 * weight - 31.1
            if 3 <= age < 10:
                return 20.315 * weight + 485.9
            if 10 <= age < 18:
                return 13.384 * weight + 692.6
            if 18 <= age < 30:
                return 14.818 * weight + 486.6
            if 30 <= age < 69:
                return 8.126 * weight + 845.6
            else:
                return 9.082 * weight + 658.5
        

    @staticmethod
    def calculate_bmr_Oxford(gender, age, weight):
        if gender == "male":
            if 0 <= age < 3:
                return 61.0 * weight - 33.7
            if 3 <= age < 10:
                return 23.3 * weight + 514
            if 10 <= age < 18:
                return 18.4 * weight + 581
            if 18 <= age < 30:
                return 16.0 * weight + 545
            if 30 <= age < 69:
                return 14.2 * weight + 593
            else:
                return 13.5 * weight + 514
        else:
            if 0 <= age < 3:
                return 58.9 * weight - 23.1
            if 3 <= age < 10:
                return 20.1 * weight + 507
            if 10 <= age < 18:
                return 11.1 * weight + 761
            if 18 <= age < 30:
                return 13.1 * weight + 558
            if 30 <= age < 69:
                return 9.74 * weight + 694
            else:
                return 10.1 * weight + 569
        
    
    @staticmethod
    def calculate_bmr_Katch_McArdle(lean_body_mass):
        return 370 + (21.6 * lean_body_mass)
        
    
    @staticmethod
    def calculate_bmr_Cunningham(lean_body_mass):
        """ The Cunningham equation is more accurate for very athletic people"""
        return 500 + (22 * lean_body_mass)
    
    
    @staticmethod
    def calculate_caloric_need(activity_level, bmr):
        if activity_level == "sedentary": 
            return bmr * 1.2
        elif activity_level == "lightly active": 
            return bmr * 1.375
        elif activity_level == "moderatetely active": 
            return bmr * 1.55
        elif activity_level == "very active":
            return bmr * 1.725
        elif activity_level == "extra active": 
            return bmr * 1.9
        else:
            raise ValueError("Invalid activity level.")


    BMR_MAPPER = {"Harris-Benedict" : calculate_bmr_Harris_Benedict,
                  "Harris Benedict (Revised)" : calculate_bmr_Harris_Benedict_rev, 
                  "Mifflin-St Jeor" : calculate_bmr_Mifflin_St_Jeor,
                  "Schofield" : calculate_bmr_Schofield, 
                  "Oxford" : calculate_bmr_Oxford,
                  "Katch-McArdle" : calculate_bmr_Katch_McArdle,
                  "Cunningham" : calculate_bmr_Cunningham}

