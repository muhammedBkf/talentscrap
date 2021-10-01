from os import sched_getscheduler, wait
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from classes.Student import Student
from classes.Database import Database

PAGENUMBER=5
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)


def get_students_number():
    xpath="/descendant::tbody[position()=1]"
    found = driver.find_element_by_xpath(xpath)
    return found.text.count("Détail")

mydb=Database("Student.db")
mydb.create()
for page in range(1,PAGENUMBER+1):
    driver.get("https://talents.esi.dz/scolar/public_etudiant_list?page={}".format(page))
    studentsNumber=get_students_number()
    for student in range(1,studentsNumber+1):
        driver.get("https://talents.esi.dz/scolar/public_etudiant_list?page={}".format(page))
        #the path for the student's element  
        detailButtonPath="/descendant::tbody[position()=1]/tr[position()={}]/td[position()=8]/a".format(student)
        detailButton = driver.find_element_by_xpath(detailButtonPath)
        studentLink=detailButton.get_attribute("href")
        driver.get(studentLink)
        std=Student(driver)
        mydb.insert_student(std)
    print("page {} completed .".format(page))


""" Login to talents
login_username=driver.find_element_by_id("id_username")
login_username.send_keys("your email goes here")

login_username=driver.find_element_by_id("id_password")
login_username.send_keys("your password goes here")

login_button=driver.find_element_by_class_name("btn-primary")
login_button.click()
"""
