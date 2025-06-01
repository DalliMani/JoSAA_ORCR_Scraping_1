#Experimented and made by D.Manideep as a reminiscence of my own JoSAA couselling
#Not made by mfing AI.
#Will work in 2025.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pandas as pd

def main():
    #Opening the browser
    driver = webdriver.Firefox(options=Options())
    #Setting the URL
    url = "https://josaa.admissions.nic.in/applicant/seatmatrix/openingclosingrankarchieve.aspx"
    driver.get(url)
    #Waiting until the user selects the options and options are loaded
    input('Press a key and enter when details are filled AND the table is loaded!\nCheck the scrollbar of the the browser to see if the table has been loaded completely. For safety, wait 5-10 seconds depending on net speed.\n<Click-Enter>\n')
    table = driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]')
    table_html = table.get_attribute('outerHTML')
    frame_list =pd.read_html(table_html) #This was just observed from nature of pd.read_html
    mainframe = frame_list[0]

    #Coverting the OR and CR columns to integer because the fricking excel sort doesn't work properly with text
    mainframe['Opening Rank'] = pd.to_numeric(mainframe['Opening Rank'], downcast='integer', errors='coerce')
    mainframe['Closing Rank'] = pd.to_numeric(mainframe['Closing Rank'], downcast='integer', errors='coerce')

    #Keeping the filesaving convention to fixed for now (lazy)
    mainframe.to_excel('./JoSAA_Data_0.xlsx')
    print('Printed Frame as Excel!')

    save_to_pickle = True
    if save_to_pickle:
        mainframe.to_pickle('./JoSAA_Dat_0.dat')
        print('Printed Frame as Pickle!')

    mainframe.to_csv('./JoSAA_Data_0.csv')
    print('Printed Frame as CSV!')

if __name__=="__main__":
    main()