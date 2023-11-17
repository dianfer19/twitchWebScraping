from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd

# Inicializamos el dataframe para excel
df_jobs = pd.DataFrame(columns=['job_title', 'company', 'fecha', 'metadata'])

# Iniciando
xpath_link_jobs = "/html/body/nav/ul/li[5]/a"
city = "Guayaquil, Guayas, Ecuador"
# url = "https://www.linkedin.com/"
# Url directa para que no me pida inicio de sesión
url = "https://www.linkedin.com/jobs/search?keywords=&location=Guayaquil%2C%20Guayas%2C%20Ecuador&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
# options = Options
driver = webdriver.Firefox()
driver.get(url)
print("iniciando .........")
sleep(3)
# session = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/button")
# session.click()
# sleep(3)
# link_jobs = driver.find_element(By.XPATH, xpath_link_jobs)
# print(f"Nombre:{link_jobs.accessible_name}")
# if str(link_jobs.accessible_name) == "Jobs":
#     link_jobs.send_keys(Keys.ENTER)
#     print("Click Jobs .........")
# else:
#     xpath_link_jobs = xpath_link_jobs.replace("5", "4")
#     link_jobs = driver.find_element(By.XPATH, xpath_link_jobs)
#     print(f"Nombre:{link_jobs.accessible_name}")
#     link_jobs.send_keys(Keys.ENTER)
# sleep(3)
# # Busqueda
id_search_location = "job-search-bar-location"
class_ul_result = "jobs-search__results-list"
# input_search_location = driver.find_element(By.ID, id_search_location)
# input_search_location.clear()
# sleep(3)
# input_search_location.send_keys(city)
# input_search_location.send_keys(Keys.ENTER)
# sleep(3)
ul_jobs = driver.find_element(By.CLASS_NAME, class_ul_result)
li_results = ul_jobs.find_elements(By.TAG_NAME, 'li')
# Recorremos el resultado
h3_title = "base-search-card__title"
h4_sub_title = "base-search-card__subtitle"
div_metadata = "base-search-card__metadata"
datetime_meta_data = "job-search-card__listdate"
for item in li_results:
    title_job = item.find_element(By.CLASS_NAME, h3_title)
    company_job = item.find_element(By.CLASS_NAME, h4_sub_title)
    metadata_job = item.find_element(By.CLASS_NAME, div_metadata)
    date_publish = metadata_job.find_element(By.CLASS_NAME, datetime_meta_data)
    new_line = pd.Series([title_job.text, company_job.text, date_publish.get_attribute('datetime'), metadata_job.text],
                         index=df_jobs.columns)
    print(f"job {title_job.text} company {company_job.text}")
    print(f"Metadata {metadata_job.text} fecha {date_publish.get_attribute('datetime')}")
    df_jobs.loc[len(df_jobs)] = new_line

file_excel_name = f"{city}.xlsx"
df_jobs.to_excel(file_excel_name)
