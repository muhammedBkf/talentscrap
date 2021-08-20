from time import sleep
import re


class Student:
    def __init__(self,driver):
        self.driver=driver
        self.promo,self.id=self.get_matricule()
        self.familyName,self.name=self.get_name()
        self.email=self.get_email()
        self.image=self.get_image()


    def get_matricule(self):
        matriculePath="/descendant::h5"
        matricule=self.driver.find_element_by_xpath(matriculePath).text
        matricule=matricule.split("/")
        promo=matricule[0][-2:]
        id=matricule[1]
        return promo,id 
    
    def get_name(self):
        #----------------------------
        familyNamePath="/descendant::td"
        familyName=self.driver.find_element_by_xpath(familyNamePath).text[6:].split("\n")
        #----------------------------
        NamePath="/descendant::td[position()=2]"
        name=self.driver.find_element_by_xpath(NamePath).text[9:].split("\n")
        return familyName[0].replace("'"," "),name[0].replace("'"," ")

    def get_email(self):
        emailPath="/descendant::tr[position()=2]/td"
        email=self.driver.find_element_by_xpath(emailPath).text[7:]
        #there is some students from promo19 that have a tutor
        if(not(re.search("@", email))):
            emailPath="/descendant::tr[position()=3]/td"
            email=self.driver.find_element_by_xpath(emailPath).text[7:]
        return email
    
    def get_image(self):
        imagePath="/descendant::img[position()=4]"
        image=self.driver.find_element_by_xpath(imagePath)
        imageFilePath="images/{}_{}.png".format(self.promo,self.id)
        with open(imageFilePath, 'wb') as file:
            file.write(image.screenshot_as_png)
        return imageFilePath

    
    def print_student(self):
        print("Matricule : {}/{}\nFamily Name : {}\nName : {}\nEmail : {}\nImage Path : {}".format(self.promo,self.id,self.familyName,self.name,self.email,self.image))
