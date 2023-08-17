# health-analytics
Assignment as a primer for 504/507

I created all the variables that was needed for this assignment which  as follows:
number variable 
string variable
list variable 
nested dictionary 

The main function of the code that i created was to find the BMI status for the patient that I created name as John
I created an argument which takes in a weight and height values of the patient which 100 (W) and 175 (H)
Since the height was in centimeters, I created a function called height_m that changes the height from cms to m  which helped with BMI calculation

Then I created a function called BMi which takes in the weight in 'kgs' and divides it by the height in 'm' squared 

Then I created else / elif / else function to determine the BMI status  
if bmi < 18.5:
        status = 'Underweight'
    elif 18.5 <= bmi < 24.9:
        status = 'Normal Weight'
    elif 25 <= bmi <29.9:
        status = 'Overweight'
    else:
status = 'Obese'

    return bmi, status

    Then used the PRINT function to show the results in the output.

    
        status = 'Obese'
