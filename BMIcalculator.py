
class BMIcalculator():
    """
    BMI (Body Mass Index) is a measurement of body fat based on height and 
    weight that applies to both men and women between the ages of 18 and 
    65 years.
    
    BMI can be used to indicate if you are overweight, obese, underweight 
    or normal. A healthy BMI score is between 20 and 25. A score below 20 
    indicates that you may be underweight; a value above 25 indicates that 
    you may be overweight.
    
    """

    @staticmethod
    def calculate_imperial_BMI(height, weight):
        return weight / (height ** 2) * 703
    
    @staticmethod
    def calculate_metric_BMI(height, weight):
        height_in_meters = height / 100
        return round(weight / (height_in_meters ** 2), 1)
            
    @staticmethod        
    def bmi_classification(bmi): 
        if bmi > 0 and bmi < 16.0: 
            return "Underweight (Severe thinness) [0-15.9]"
        elif bmi <= 16.9: 
            return "Underweight (Moderate thinness) [16.0-16.9]"
        elif bmi <= 18.4:
            return "Underweight (Mild thinness) [17.0-18.4]"
        elif bmi <=24.9:
            return "Normal range [18.5-24.9]"
        elif bmi <= 29.9:
            return "Overweight (Pre-obese) [25.0-29.9]"
        elif bmi <= 34.9:
            return "Obese (Class I) [30.0-34.9]"
        elif bmi <= 39.9:
            return "Obese (Class II) [35.0-39.9]"
        else:
            return "Obese (Class III) [40.0+]"