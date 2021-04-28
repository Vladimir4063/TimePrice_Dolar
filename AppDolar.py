from selenium import webdriver
import time
from datetime import date
from io import open


hoy = date.today() #Registro de fecha.

PATH = "C:\Program Files (x86)\msedgedriver.exe"

driver = webdriver.Edge(PATH) #Guardamos la ubicacion del archivo.

driver.get('https://www.google.com/search?q=precio+dolar+hoy+argentina&sxsrf=ALeKk01LU79nhSUfi-rTvrFjze7E92djfQ%3A1619610459771&ei=W0uJYLjfLpXU1sQPhvqwyAY&oq=precio+dolar+hoy+ar&gs_lcp=Cgdnd3Mtd2l6EAMYADIKCAAQsQMQRhCCAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BwgjEMkDECc6CggAEIcCELEDEBQ6BwgjEOoCECc6BAgjECc6CggAELEDEIMBEEM6BAgAEEM6CAgAELEDEIMBOg4IABCxAxCDARDHARCjAjoJCCMQJxBGEIICOgcIABDJAxBDOgUIABCSAzoHCAAQsQMQQzoKCAAQsQMQyQMQQzoFCAAQsQM6CAgAELEDEMkDOgcIABCHAhAUOgQIABADUIweWNBGYPROaAFwAngDgAGzAYgB3yGSAQUzMi4xM5gBAKABAaoBB2d3cy13aXqwAQrAAQE&sclient=gws-wiz')

time.sleep(3) #Esperamos 3 segundos para que cargue bien la pagina.

precio_dolar = driver.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')

# Damos formato texto al resultado
registro = ("Precio dolar hoy: ", hoy, "$", precio_dolar.text)

#abrimos el archivo
archivo_texto = open("archivo.txt", "w")

#Escribimos en el
archivo_texto.write(str(registro))

#cerramos el navegador
archivo_texto.close()
driver.quit()
