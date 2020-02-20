from time import sleep
from parsel import Selector
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    print("Compare the list of names in board_members.csv")
    print("to the board of directors working list on InterAction")

    board_current = str(input("Are the names on the Board Members correct? y/n: "))

    while board_current != "y":  # if board_members.csv is not current
        print("Please enter y or n, and if n, please update board member file")
        board_current = str(input("Are the names on the Board Members correct? y/n: "))

    else:

        # creates driver and navigates to LinkedIn
        driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver.get("http://www.linkedin.com")

        # clicks "Sign In"
        sign_in_button = driver.find_element_by_class_name("nav__button-secondary")
        sign_in_button.click()

        # inputs username
        username = driver.find_element_by_id("username")
        username_input = str(input("LinkedIn username:"))
        username.send_keys(username_input)
        sleep(0.5)

        # inputs password
        password = driver.find_element_by_id("password")
        password_input = str(input("LinkedIn password:"))
        password.send_keys(password_input)
        sleep(0.5)

        # submits username and password to sign in
        submit = driver.find_element_by_xpath("//*[@type='submit']")
        submit.click()
        sleep(0.5)

        csv_file = "board_members.csv"

        try: # NOTE 'with open' will automatically close the file

            # open the csv file for reading
            with open(csv_file, "r") as read_file:

                # create a reader object
                reader = csv.reader(read_file)
                lines = list(reader)

                # pull out number of records in file
                num_records = int(lines[0][3].strip())
                if num_records > 40:
                    over_40_records = True

                # for each record
                for i in range(1, 10):

                    # complete the linkedin url for each entry
                    li_suffix = str(lines[i][1])
                    li_url = "https://www.linkedin.com/in/" + li_suffix

                    #navigate driver to linkedin profile
                    driver.get(li_url)
                    sleep(5)

                    # scrape current position and employer
                    current_position = "position" #driver.find_element_by_
                    current_employer = "employer" #driver.find_element_by_

        except IOError:
            print("IOError")

        try: # NOTE 'with open' will automatically close the file

            # open csv file for writing
            with open(csv_file, "w") as write_file:

                # create a writer object
                writer = csv.writer(write_file)
                write.writerow(lines)

                # for each record
                for i in range(1, len(lines)):

                    if len(lines[i]) > 1:
                        if current_position == lines[i][2] \
                        and current_employer == lines[i][3]:
                            lines[i][4] == " "
                        else:
                            lines[i][4] == "updated!"
                    else:

                        # rewrite the information, adding position and employer
                        writer.writerow(lines[i][0], lines[i][1],
                                        current_position, current_employer)

        except IOError:
            print("IOError")


main()