from selenium import webdriver
import keyboard
import time
import os
from msedge.selenium_tools import Edge, EdgeOptions

ProjectName = input("Enter The Project Name:- \n")
path = input("Enter The Project Path:- \n")
commitMessage = str(input("Enter The Commit Message:- \n"))

print("***************Execution Started***********")

# ************* !IMPORTANT READ THIS CAREFULLY
# set the profile as the default edge account
# to get your profile path just type in your desidered browser - "Edge://version" and you will get a profile path, so copy that and paste it below
# initializing the edge options
# *************

edge_options = EdgeOptions()
edge_options.use_chromium = True

#!! Here you set the path of the your profile ending with User Data ****** not the profile folder ****
edge_options.add_argument(
    "user-data-dir=C:\\Users\\Swaya\\AppData\\Local\\Microsoft\\Edge\\User Data")  # !Paste The Profile Path here Ignore the Profile with double slasses

# !! type the name of The Profile folder here
edge_options.add_argument("profile-directory=Profile 4")

# In the previous commits you may see some unecessary logs by selenium
# so to disable it we have written below code
edge_options.add_argument("--disable-logging")

# This code will open Microsoft Edge and set your default account and open github.com
driver = Edge(options=edge_options, executable_path="msedgedriver.exe")


# ******** You can learn more about this here :-  https://stackoverflow.com/questions/67762186/user-profile-on-edge-using-selenium-python

# The maximize function will maximize the edge browser window
driver.maximize_window()

# Below code will open the github website
driver.get("https://github.com")

print("Github Opened Successfully")


def main():

    if "https://github.com" == driver.current_url:
        login()
    else:

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

        print(f"Repository Created Successfuly named {ProjectName}")

        # then the user will be navigated to the create repository page
        # here first our bot will copy the git link or Https link
        driver.find_element_by_xpath(
            "/html/body/div[4]/div/main/div[2]/div/git-clone-help/div[1]/div/div[4]/div/span/span/clipboard-copy").click()

        print("Successfuly Copied the git link")

        print("Opening CMD")

        # this os.system() function will opoen cmd on the given path
        os.system(f"start cmd /K cd {path}")
        time.sleep(1.2)

        print("CMD Opened Successfuly")

        # after the opening of the terminal the bot will initialize that folder with git
        keyboard.write("git init")
        keyboard.press_and_release("enter")

        print("Git Initialised Successfuly")

        keyboard.write("git add .")
        keyboard.press_and_release("enter")

        print("Arranged Untracked Files")
        print("Changed To Be Commited")

        keyboard.write(f'''git commit -m "{commitMessage}" ''')
        keyboard.press_and_release("enter")

        print("Changed Commited Successfuly")
        print("Connecting To your Remote repository...")

        keyboard.write("git remote add origin ")
        keyboard.press_and_release("control + v")
        keyboard.press_and_release("enter")

        print("Project Connected Successfuly to your remote repository")
        print("Pushing your project files to github...")

        keyboard.write("git push -u origin master")
        keyboard.press_and_release("enter")

        print("congrats project Uploaded Successfuly to github")


def login():

    # click on the sign In Button and enter my credentials
    driver.find_element_by_xpath(
        "/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a").click()

    # !!!!!!! For Username !!!!!!!!
    # ** the below code clicks on the username input and fill my username
    # ! You Put your github username here in send_keys function
    driver.find_element_by_xpath(
        "/html/body/div[3]/main/div/div[4]/form/input[2]").send_keys("your_username_here")

    # !!!!!!! For Password !!!!!!!!
    # ** below code clicks on the password input and fill my password
    driver.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[1]").send_keys(
        "your_password_here")  # ! You Put your github password here in send_keys function

    # !! then the below code will click on the login button
    driver.find_element_by_xpath(
        "/html/body/div[3]/main/div/div[4]/form/div/input[12]").click()

    # ******* If YOU HAVE TWO-FACTOR-AUTHENTICATION IN GITHUB THE BELOW CODE IS FOR THAT

    # # our bot will press the button named - "Enter a two-factor-verification code"
    driver.find_element_by_xpath(
        "/html/body/div[3]/main/div/div[7]/ul/li[1]/a").click()

    # !! then our bot will type my or your recovery code
    # ************** PLS PUT YOUR RECOVERY CODE BELOW in send_keys() function #

    # !! PUT_YOUR_RECOVERY_CODE_HERE
    driver.find_element_by_xpath(
        "/html/body/div[3]/main/div/div/form/div[3]/input").send_keys("your_github_recovery_code_here")

    # !! and then our bot should click on the verify button
    driver.find_element_by_xpath(
        "/html/body/div[3]/main/div/div/form/div[3]/button").click()

    # **---------- NOW OUR BOT WILL LOGIN TO YOUR ACCOUNT -----------------**
    print("Account Login Successfull")
    main()


main()
