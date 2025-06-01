from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pandas as pd

def main():
    driver = webdriver.Firefox(options=Options())
    url = "https://josaa.admissions.nic.in/applicant/seatmatrix/openingclosingrankarchieve.aspx"
    driver.get(url)
    input('Press a key and enter when details are filled!')
    tbody = driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_GridView1"]/tbody')

    trs = tbody.find_elements(By.XPATH, './/tr')
    print('Got the TRs!')
    data = []

    for tr in trs:
        row = [item.text for item in tr.find_elements(By.XPATH, ".//td")]
        data.append(row)
    del data[0]
    table_heading = [item.text for item in trs[0].find_elements(By.XPATH, './/th')]
    print('Got the data!')
    frame = pd.DataFrame(data, columns=table_heading)
    frame.to_excel('./JoSAA_Data_0.xlsx')
    print('Printed Frame as Excel!')
    save_to_pickle = True
    if save_to_pickle:
        frame.to_pickle('./JoSAA_Dat_0.dat')
        print('Printed Frame as Pickle!')
    frame.to_csv('./JoSAA_Data_0.csv')
    print('Printed Frame as CSV!')

    print(len(data))

def main2():
    header = ['Fruit', 'Animal', 'Pet']
    data = [['Apple', 'Bat', 'Cat'], ['Death', 'Elephant', 'Feather']]
    frame = pd.DataFrame(data, columns=header)
    print(frame)

if __name__=="__main__":
    main()