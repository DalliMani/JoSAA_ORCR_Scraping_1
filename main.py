#Experimented and made by D.Manideep as a reminiscence of my own JoSAA couselling
#Not made by mfing AI.
#Will work in 2025.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pandas as pd
from io import StringIO

def main():
    #Opening the browser
    driver = webdriver.Firefox(options=Options())
    #Setting the URL
    url = "https://josaa.admissions.nic.in/applicant/seatmatrix/openingclosingrankarchieve.aspx"
    driver.get(url)

    #Waiting until the user selects the options and options are loaded
    print('Go to Firefox and load the table and scroll down to the end of the table!')
    print('Check the scrollbar of the the browser to see if the table has been loaded completely. For safety, wait 10-20 seconds depending on net speed.')
    input('<Click-Enter>\n')

    #Getting the table
    table = driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]')
    table_html = StringIO(table.get_attribute('outerHTML'))
    frame_list =pd.read_html(table_html) #This was just observed from nature of pd.read_html
    mainframe = frame_list[0]

    #Closing the HTML because we don't need it
    table_html.close()

    #Coverting the OR and CR columns to integer because the fricking excel sort doesn't work properly with text
    mainframe['Opening Rank'] = pd.to_numeric(mainframe['Opening Rank'], downcast='integer', errors='coerce')
    mainframe['Closing Rank'] = pd.to_numeric(mainframe['Closing Rank'], downcast='integer', errors='coerce')

    #Keeping the filesaving convention to fixed for now (lazy)
    filename = 'JoSAA_Data_0'
    should_save_as = {
        'Excel': True,
        'CSV': False,
        'Dataframe as pickle': True
    }

    if should_save_as['Excel']:
        mainframe.to_excel(f'./{filename}.xlsx')
        print('Printed Frame as Excel!')
    if should_save_as['Dataframe as pickle']:
        mainframe.to_pickle(f'./{filename}.dat')
        print('Printed Frame as Pickle!')
    if should_save_as['CSV']:
        mainframe.to_csv(f'./{filename}.csv')
        print('Printed Frame as CSV!')

if __name__=="__main__":
    main()