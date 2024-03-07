import pandas as pd
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, InvalidSelectorException, ElementClickInterceptedException




chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

df = pd.read_csv("Colon Cancer February - Copy.csv",delimiter=';')

average_male_height_feet = 5
average_male_height_inches = 9



# convert bmi into feet and inches input, this basically takes the bmi and the average height to put in the weight(lbs)
def bmi_weight_input_male(bmi):
    weight_lbs = bmi * 1.75 * 1.75 * 2.2
    return round(weight_lbs)




veg_consumption = ['None', 'Less than 1 serving/week', '1-2 servings/week', '3-4 servings/week',
                     '5-6 servings/week', '7-10 servings/week','More than 10 servings/week' ]
veg_month_consumption = ['½ cup or less','Between ½ cup - 1½ cups','1½ cups - 3 cups',
                         '3 cups - 5 cups','More than 5 cups']
mod_phys_activity = [0,1,2,3,4,5,6,7,8,9,10,11,12]
mod_phys_activity_time = ['Up to 1 hour/week','Between 1 - 2 hours/week','2 - 3 hours/week',
                          '3 - 4 hours/week','More than 4 hours/week']
vig_phys_activity = [0,1,2,3,4,5,6,7,8,9,10,11,12]
vig_phys_activity_time = ['Up to 1 hour/week','Between 1 - 2 hours/week','2 - 3 hours/week',
                          '3 - 4 hours/week','More than 4 hours/week']

colonoscopy = ["Yes","No"]
polyp = ["Yes","No"]
meds_one = ["Yes","No"]
meds_two = ["Yes","No"]
family_history = ["Yes","No"]
family_numbers = ["1", "2 or more"]
cigarettes = ["Yes","No"]



#note this depends on the age entered we're gonna go with a number between 10 and age like this list(10,age)
# start_smoking = list(1,'age')
currently_smoking = ['Yes','No']

# #note this depends on the age entered we're gonna go with a number between start smoking and age like this list(start_smoking,age)
# quit_age = list(start_smoking,age)
cigarettes_per_day = ['0 cigarettes a day','1 to 10 cigarettes a day','11 to 20 cigarettes a day','More than 20 cigarettes a day']





#DEMOGRAPHICS
def demographics(race,sex,age,bmi):
    if race=='Latino':
        temp_latino = driver.find_element(By.XPATH,value='//*[@id="demo-section"]/div[1]/div[1]/div')
        temp_latino.click()
        time.sleep(1)
        pop_up = driver.find_element(By.XPATH, value='//*[@id="raceOkButton"]')
        pop_up.click()

    else:
        not_latino = driver.find_element(By.XPATH,value='//*[@id="demo-section"]/div[1]/div[2]/div')
        not_latino.click()
        time.sleep(1)

        if race=='White':
            temp_white = driver.find_element(By.XPATH,value='//*[@id="demo-section"]/div[2]/div[1]/div')
            temp_white.click()

    temp_age = driver.find_element(By.XPATH,value='//*[@id="age"]')
    temp_age.send_keys(str(age))
    # driver.execute_script("arguments[0].scrollIntoView();", temp_age)
    time.sleep(1)

    if sex=='Male':
        temp_sex = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, 'maleFocus'))
        )
        temp_sex.click()
        height_feet = driver.find_element(By.XPATH,value='//*[@id="height_ft"]')
        height_feet.send_keys(average_male_height_feet)
        height_inches = driver.find_element(By.XPATH,value='//*[@id="height_in"]')
        height_inches.send_keys(average_male_height_inches)
        temp_weight = driver.find_element(By.XPATH,value='//*[@id="weight"]')
        weight = bmi_weight_input_male(bmi)
        temp_weight.send_keys(weight)



#Diet & Physical Activity
def diet():
    servings= driver.find_element(By.XPATH,value='//*[@id="veg_servings"]')
    driver.execute_script("arguments[0].scrollIntoView();", servings)
    temp_servings = random.choice(veg_consumption)
    if temp_servings=='None':
        servings.send_keys(temp_servings)
        df.iloc[i, df.columns.get_loc('Diet Servings')]=temp_servings

    elif temp_servings!='None':
        servings.send_keys(temp_servings)
        df.iloc[i, df.columns.get_loc('Diet Servings')]= temp_servings
        number_servings = driver.find_element(By.XPATH,value='//*[@id="veg_amount"]')
        temp_number_servings = random.choice(veg_month_consumption)
        number_servings.send_keys(temp_number_servings)
        df.iloc[i, df.columns.get_loc('Number of Servings')] = temp_number_servings
    #----
    moderate_activity = driver.find_element(By.XPATH, value='//*[@id="moderate_months"]')
    temp_moderate_activity = random.choice(mod_phys_activity)
    if temp_moderate_activity == 0:
        moderate_activity.send_keys(temp_moderate_activity)
        df.iloc[i, df.columns.get_loc('Mod Activity')]=temp_moderate_activity
    elif temp_moderate_activity!=0:
        moderate_activity.send_keys(temp_moderate_activity)
        df.iloc[i, df.columns.get_loc('Mod Activity')] = temp_moderate_activity
        hours_moderate_activity = driver.find_element(By.XPATH,value='//*[@id="moderate_hours"]')
        temp_hours_moderate_activity = random.choice(mod_phys_activity_time)
        hours_moderate_activity.send_keys(temp_hours_moderate_activity)
        df.iloc[i, df.columns.get_loc('Mod_Hours')] = temp_hours_moderate_activity


    vigorous_activity = driver.find_element(By.XPATH, value='//*[@id="vigorous_months"]')
    driver.execute_script("arguments[0].scrollIntoView();", vigorous_activity)
    temp_vig_activity = random.choice(vig_phys_activity)
    if temp_vig_activity == 0:
        vigorous_activity.send_keys(temp_vig_activity)
        df.iloc[i, df.columns.get_loc('Vig Activity')] = temp_vig_activity
    elif temp_vig_activity != 0:
        vigorous_activity.send_keys(temp_vig_activity)
        vigorous_hours = driver.find_element(By.XPATH,value='//*[@id="vigorous_hours"]')
        temp_vig_hours = random.choice(vig_phys_activity_time)
        vigorous_hours.send_keys(temp_vig_hours)
        df.iloc[i, df.columns.get_loc('Vig Hours')] = temp_vig_hours


#MEDICAL HISTORY

def medical_history():
    temp_colonoscopy = random.choice(colonoscopy)
    if temp_colonoscopy == 'Yes':
        yes_colon = driver.find_element(By.XPATH,value='//*[@id="medical-section"]/div[1]/div[1]/div')
        yes_colon.click()
        df.iloc[i, df.columns.get_loc('Colonoscopy')] = 'Yes'
        driver.execute_script("arguments[0].scrollIntoView();", yes_colon)
        temp_polyp = random.choice(polyp)
        if temp_polyp=='Yes':
            polyp_question = driver.find_element(By.XPATH,value='//*[@id="medical-section"]/div[2]/div[1]/div')
            polyp_question.click()
            df.iloc[i, df.columns.get_loc('Polyp')] = 'Yes'
        elif temp_polyp == 'No':
            polyp_question = driver.find_element(By.XPATH, value='//*[@id="medical-section"]/div[2]/div[2]/div')
            polyp_question.click()
            df.iloc[i, df.columns.get_loc('Polyp')] = 'No'
        # else:
        #     polyp_question = driver.find_element(By.XPATH, value='//*[@id="medical-section"]/div[2]/div[3]/div')
        #     polyp_question.click()
        #     df.iloc[i, df.columns.get_loc('Polyp')] = 'Unknown'
    elif temp_colonoscopy == 'No':
        no_colon = driver.find_element(By.XPATH,value='//*[@id="medical-section"]/div[1]/div[2]/div')
        no_colon.click()
        df.iloc[i, df.columns.get_loc('Colonoscopy')] = 'No'
    # else:
    #     not_know_colon = driver.find_element(By.XPATH,value='//*[@id="medical-section"]/div[1]/div[3]/div')
    #     not_know_colon.click()
    #     df.iloc[i, df.columns.get_loc('Colonoscopy')] = 'Unknown'
    temp_meds = random.choice(meds_one)
    if temp_meds == 'Yes':
        medication = driver.find_element(By.XPATH,value='//*[@id="medical-section"]/div[3]/div[1]/div')

        medication.click()
        df.iloc[i, df.columns.get_loc('Meds_one')] = 'Yes'
    else:
        medication = driver.find_element(By.XPATH, value='//*[@id="medical-section"]/div[3]/div[2]/div')

        medication.click()
        df.iloc[i, df.columns.get_loc('Meds_one')] = 'No'
    # else:
    #     medication = driver.find_element(By.XPATH, value='//*[@id="medical-section"]/div[3]/div[3]/div')
    #
    #     medication.click()
    #     df.iloc[i, df.columns.get_loc('Meds_one')] = 'Unknown'

    temp_meds_two = random.choice(meds_two)
    if temp_meds_two == 'Yes':
        medication_two = driver.find_element(By.XPATH, value='//*[@id="medical-section"]/div[4]/div[1]/div/span')
        medication_two.click()
        df.iloc[i, df.columns.get_loc('Meds_Two')] = 'Yes'
    else:
        medication_two = driver.find_element(By.XPATH, value='//*[@id="medical-section"]/div[4]/div[2]/div/span')
        medication_two.click()
        df.iloc[i, df.columns.get_loc('Meds_Two')] = 'No'
    # else:
    #     medication_two = driver.find_element(By.XPATH, value='//*[@id="medical-section"]/div[4]/div[3]/div/span')
    #     medication_two.click()
    #     df.iloc[i, df.columns.get_loc('Meds_Two')] = 'Unknown'


#FAMILY HISTORY

def family_genetics():
    temp_family = random.choice(family_history)
    if temp_family == 'Yes':
        temp_family_genetics = driver.find_element(By.XPATH,value='//*[@id="family-section"]/div[1]/div[1]/div/span')
        temp_family_genetics.click()
        df.iloc[i, df.columns.get_loc('Family History')] = 'Yes'
        temp_family_numbers = random.choice(family_numbers)
        time.sleep(1)
        if temp_family_numbers=="1":
            select_family = driver.find_element(By.XPATH,value='//*[@id="family-section"]/div[3]/div[1]/div/span')
            select_family.click()

            df.iloc[i, df.columns.get_loc('Family Numbers')] = '1'
        else:
            select_family = driver.find_element(By.XPATH,value='//*[@id="family-section"]/div[3]/div[2]/div/span')
            select_family.click()
            df.iloc[i, df.columns.get_loc('Family Numbers')] = '2 or more'

        # else:
        #     select_family = driver.find_element(By.XPATH, value='//*[@id="family-section"]/div[3]/div[3]/div/span')
        #     select_family.click()
        #     df.iloc[i, df.columns.get_loc('Family Numbers')] = 'Unknown'
    else:
        temp_family_genetics = driver.find_element(By.XPATH, value='//*[@id="family-section"]/div[1]/div[2]/div/span')

        temp_family_genetics.click()
        df.iloc[i, df.columns.get_loc('Family History')] = 'No'
    # else:
    #     temp_family_genetics = driver.find_element(By.XPATH, value='//*[@id="family-section"]/div[1]/div[3]/div/span')
    #
    #     temp_family_genetics.click()
    #     df.iloc[i, df.columns.get_loc('Family History')] = 'Unknown'

#CIGARETE USAGE

def cigarette_usage(age):
    temp_lifetime_cigarettes = random.choice(cigarettes)
    if temp_lifetime_cigarettes == 'Yes':
        lifetime_cigarettes = driver.find_element(By.XPATH,value='//*[@id="cigarette-section"]/div[1]/div[1]/div')
        lifetime_cigarettes.click()
        df.iloc[i, df.columns.get_loc('Cigarettes')] = 'Yes'
        start_smoking = list(range(1,age))
        start_smoking.append("Never smoked cigarettes regularly")
        start_smoking_temp = random.choice(start_smoking)
        select_start_smoking = driver.find_element(By.XPATH,value='//*[@id="firstYearSmoke"]')
        driver.execute_script("arguments[0].scrollIntoView();", select_start_smoking)
        if start_smoking_temp == 'Never smoked cigarettes regularly':
            select_start_smoking.send_keys(start_smoking_temp)
            df.iloc[i, df.columns.get_loc('Smoking_Age')] = 'N/A'

        else:
            select_start_smoking.send_keys(start_smoking_temp)
            df.iloc[i, df.columns.get_loc('Smoking_Age')] = start_smoking_temp
            is_currently_smoking = random.choice(currently_smoking)
            if is_currently_smoking=='Yes':
                currently_smoke_selection = driver.find_element(By.XPATH,value='//*[@id="cigarette-section"]/div[3]/div[1]/div/span')
                currently_smoke_selection.click()
                df.iloc[i, df.columns.get_loc('Currently Smoking')] = 'Yes'
            else:
                currently_smoke_selection = driver.find_element(By.XPATH, value='//*[@id="cigarette-section"]/div[3]/div[2]/div/span')
                currently_smoke_selection.click()
                df.iloc[i, df.columns.get_loc('Currently Smoking')] = 'No'
                quitting_age_sample = random.choice(list(range(start_smoking_temp,age)))
                quitting_age_selection = driver.find_element(By.XPATH,value='//*[@id="smoke_quit"]')
                time.sleep(1)
                # select_quit_age = Select(quitting_age_selection)
                # select_quit_age.select_by_visible_text(str(quitting_age_sample))
                quitting_age_selection.send_keys(str(quitting_age_sample))
                df.iloc[i, df.columns.get_loc('Quit_Age')] = quitting_age_sample
            number_of_cigarettes_per_day = random.choice(cigarettes_per_day)
            cigarettes_per_day_selector = driver.find_element(By.XPATH,value='//*[@id="cigarettes_num"]')
            cigarettes_per_day_selector.send_keys(number_of_cigarettes_per_day)
            df.iloc[i, df.columns.get_loc('No of Cigarettes')] = number_of_cigarettes_per_day
    elif temp_lifetime_cigarettes=='No':
        lifetime_cigarettes = driver.find_element(By.XPATH, value='//*[@id="cigarette-section"]/div[1]/div[2]/div')
        lifetime_cigarettes.click()
        df.iloc[i, df.columns.get_loc('Cigarettes')] = 'No'
    # else:
    #     lifetime_cigarettes = driver.find_element(By.XPATH, value='//*[@id="cigarette-section"]/div[1]/div[3]/div')
    #     lifetime_cigarettes.click()
    #     df.iloc[i, df.columns.get_loc('Cigarettes')] = 'Unknown'


#RESULT

def get_result():
    result = driver.find_element(By.XPATH, value='//*[@id="calculate"]')
    result.click()
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 300)")

    patient_risk = driver.find_element(By.XPATH, value='//*[@id="Risk5"]')
    print(patient_risk.text)
    df.iloc[i, df.columns.get_loc('Result')]= patient_risk.text


for j in [1750,1840,1900]:

    for i in range(j,2000,1):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://ccrisktool.cancer.gov/calculator.html")
        row = df.iloc[i]
        race = row['Ethnicity']
        age = row['Age']
        sex = row['Gender']
        bmi = row['BMI']

        try:
            demographics(race,sex,age,bmi)
            diet()
            medical_history()
            family_genetics()
            cigarette_usage(age)
            get_result()
        except (ElementNotInteractableException,InvalidSelectorException, ElementClickInterceptedException) as e:
            print(e)

            df.to_csv(f"Sample size of even {i}.csv")
            driver.quit()
            break

        if i % 10 == 0:
            driver.refresh()
            time.sleep(1)
        driver.quit()



# df.to_csv(f"Sample size of even 1900.csv")














#
#
#
#
#
#
# question = driver.find_element(By.XPATH, value='//*[@id="demo-section"]/div[1]/div[1]/div/span')
# question.click()
# time.sleep(3)
# pop_up = driver.find_element(By.XPATH,value='//*[@id="raceOkButton"]')
# pop_up.click()
#
# race = driver.find_element(By.XPATH,value='//*[@id="demo-section"]/div[2]/div[2]/div')
# print(race.text)
# time.sleep(3)
#
# veggies = driver.find_element(By.XPATH, value='//*[@id="veg_servings"]')
# driver.execute_script("arguments[0].scrollIntoView();", veggies)
# veggies.send_keys('Less than 1 serving/week')
#
# time.sleep(2)
#
# portions = driver.find_element(By.XPATH,value='//*[@id="veg_amount"]')
#
# portions.send_keys('½ cup or less')
# time.sleep(2)
# # To select by visible text (if "75" is the text shown in the dropdown)
#
# # dropdown.select_by_visible_text("3-4 servings/week")
#


























#########################################################################3
