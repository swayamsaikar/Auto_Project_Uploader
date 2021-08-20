
from selenium.webdriver import Edge
import keyboard
import time
import os

ProjectName = input("Enter The Project Name:- \n")
path = input("Enter The Project Path:- \n")
commitMessage = str(input("Enter The Commit Message:- \n"))


# This code will open Microsoft Edge and open github.com
driver = Edge("msedgedriver.exe")

# The maximize function will maximize the edge browser window
driver.maximize_window()

# Below code will open the github website
driver.get("https://github.com")

# after opening of github or bot will do the following things :-

# click on the sign In Button and enter my credentials
driver.find_element_by_xpath(
    "/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a").click()

# !!!!!!! For Username !!!!!!!!
# ** the below code clicks on the username input and fill my username
# ! You Put your github username here in send_keys function
driver.find_element_by_xpath(
    "/html/body/div[3]/main/div/div[4]/form/input[2]").send_keys("your_username")

# !!!!!!! For Password !!!!!!!!
# ** below code clicks on the password input and fill my password
driver.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[1]").send_keys(
    "your_password")  # ! You Put your github password here in send_keys function


# !! then the below code will click on the login button
driver.find_element_by_xpath(
    "/html/body/div[3]/main/div/div[4]/form/div/input[12]").click()


# now our bot will click on the new repo menu
driver.find_element_by_xpath(
    "/html/body/div[1]/header/div[6]/details/summary").click()

# now our bot will click on the new repository button inside the menu
driver.find_element_by_xpath(
    "/html/body/div[1]/header/div[6]/details/details-menu/a[1]").click()

# now our bot will click on the "repository name" input box and fill the value as the ProjectName that we have taken the input from the user above in the PorjectName variable
driver.find_element_by_xpath(
    "/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input").send_keys(ProjectName)

time.sleep(0.6)
# then our bot will click on the create Repository button
driver.find_element_by_xpath(
    "/html/body/div[4]/main/div/form/div[4]/button").click()


# then the user will be navigated to the create repository page
# here first our bot will copy the git link or Https link
driver.find_element_by_xpath(
    "/html/body/div[4]/div/main/div[2]/div/git-clone-help/div[1]/div/div[4]/div/span/span/clipboard-copy").click()

# this os.system() function will opoen cmd on the given path
os.system(f"start cmd /K cd {path}")
time.sleep(1.5)

# after the opening of the terminal the bot will initialize that folder with git
keyboard.write("git init")
keyboard.press_and_release("enter")

keyboard.write("git add .")
keyboard.press_and_release("enter")

keyboard.write(f'''git commit -m "{commitMessage}" ''')
keyboard.press_and_release("enter")

keyboard.write("git remote add origin ")
keyboard.press_and_release("control + v")
keyboard.press_and_release("enter")

keyboard.write("git push -u origin master")
keyboard.press_and_release("enter")
