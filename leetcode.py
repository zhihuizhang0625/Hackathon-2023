from selenium.webdriver.common.by import By
import time 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


PATH = "/Users/czhang3/Desktop/chromedriver_mac64/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get('https://leetcode.com/')

time.sleep(3)
sign_in = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div[2]/div/a[5]")

# time.sleep(2)

sign_in.click()

time.sleep(5)

username = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/form/span[1]/input")
    
# time.sleep(2)

username.send_keys('clarajelly_')

# time.sleep(1)

password = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/form/span[2]/input")


password.send_keys('Clara_0625')

# time.sleep(1)

sign_in_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/button/div")

sign_in_button.click()

time.sleep(5)

problems = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[3]/a")

problems.click()

time.sleep(5)




# Attempted section

solved_button= driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[1]/div[6]/div[1]/div/div[1]/div[3]/div/button")

solved_button.click()
time.sleep(3)

Attempted_problems = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[1]/div[6]/div[1]/div/div[1]/div[3]/div[2]/div[3]/div/div/span")

Attempted_problems.click()

time.sleep(3)

page = 1
page_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[1]/div[6]/div[3]/nav")
page_total = 0
children = page_button.find_elements_by_xpath("./child::*")
for x in children:
    page_total+=1
print(page_total)

tableRows_Prefix="/html/body/div[1]/div/div[2]/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div["
problem_title_End = "]/div[2]/div/div/div/div/a"
difficulty_End = "]/div[5]/span"
problem_button_End = "]/div[2]/div/div/div"

pagePrefix = "/html/body/div[1]/div/div[2]/div[1]/div[1]/div[6]/div[3]/nav/button["
buttonLimit = page_total - 1
pageEnd = "]"
pageXPath = pagePrefix + str(buttonLimit) + pageEnd
lastPage_button = driver.find_element(by=By.XPATH, value=pageXPath)
lastPage = int(lastPage_button.text)
nextPage_XPath = pagePrefix + str(page_total) + pageEnd
# print(lastPage)

while page in range(1, lastPage+1):     
    tableRows = driver.find_elements(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div")
    i = 1
    svgPrefix = '#__next > div > div.mx-auto.mt-\[50px\].w-full.grow.p-4.md\:mt-0.md\:max-w-\[888px\].md\:p-6.lg\:max-w-screen-xl > div.grid.grid-cols-4.gap-4.md\:grid-cols-3.lg\:grid-cols-4.lg\:gap-6 > div.col-span-4.z-base.md\:col-span-2.lg\:col-span-3 > div:nth-child(7) > div.-mx-4.md\:mx-0 > div > div > div:nth-child(2) > div:nth-child('
    svgEnd = ') > div:nth-child(1) > svg'
    time.sleep(3)
    for e in tableRows:
        if(page ==1 and i ==1):
            i+=1
            continue
        problem_title_xpath = tableRows_Prefix+str(i)+problem_title_End
        problem_title = driver.find_element(by=By.XPATH, value=problem_title_xpath)
        print(problem_title.text)
        problem_link = problem_title.get_attribute('href')
        print(problem_link)
        # time.sleep(2)
        difficulty_xpath = tableRows_Prefix+str(i)+difficulty_End
        # print(difficulty_xpath)
        difficulty = driver.find_element(by=By.XPATH, value=difficulty_xpath)
        print(difficulty.text)
    
        # time.sleep(2)
        cssSelector = svgPrefix + str(i) + svgEnd
        try:
            status_svg = driver.find_element(By.CSS_SELECTOR, cssSelector)
            status = status_svg.get_attribute('class')
            if 'green' in status:
                status = 'Solved'
            if 'yellow' in status:
                status = 'Attempted'
        except NoSuchElementException:
            status = 'To do'
        print(status)
        problem_button_xpath = tableRows_Prefix+str(i)+problem_button_End
        problem_button = driver.find_element(by=By.XPATH, value=problem_button_xpath)
        problem_button.click()
        time.sleep(5)
        submissions_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div/a[4]/div")
        submissions_button.click()
        time.sleep(5)
        submission_prefix = "/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div[2]/div["
        submission_endpath="]/div[1]/div[1]/div/div/span"
        dates_endpath = "]/div[1]/div[1]/span"
        submissionRows = driver.find_elements(by=By.XPATH, value="/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div[2]/div")
        submission_count = 0
        for s in submissionRows:
            # submission = s.find_element(by=By.XPATH, value=".//div[1]/div[1]/div/div/span")
            # print(submission.text)
            try:
                submission_count += 1
                submission_path = submission_prefix + str(submission_count)+ submission_endpath
                submission = s.find_element(by=By.XPATH, value=submission_path)
                print(submission.text)
                dates_path = submission_prefix + str(submission_count)+ dates_endpath
                dates = driver.find_element(by=By.XPATH, value=dates_path)
                print(dates.text)
            except NoSuchElementException:
                break
            except StaleElementReferenceException:
                break
        submission_count-=1
        print(submission_count)
        # back_svg = driver.find_element(By.CSS_SELECTOR,"#__next > div > div > div > nav > div > div > div.absolute.left-\[50\%\].hidden.-translate-x-2\/4.items-center.space-x-4.lc-md\:flex > div.flex.cursor-pointer.items-center.space-x-2 > svg")
        # back_svg.click()
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        i+=1
        time.sleep(3)
    if (page == lastPage):
        break
    page_button = driver.find_element(by=By.XPATH, value=nextPage_XPath)

    page_button.click()
    time.sleep(3)
    page+=1





# Solved section

solved_button= driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[1]/div[6]/div[1]/div/div[1]/div[3]/div/button")

solved_button.click()
time.sleep(3)

solved_problems = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[1]/div[6]/div[1]/div/div[1]/div[3]/div[2]/div[2]/div/div/span")

solved_problems.click()

time.sleep(3)

page = 1
page_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[1]/div[6]/div[3]/nav")
page_total = 0
children = page_button.find_elements_by_xpath("./child::*")
for x in children:
    page_total+=1
print(page_total)

tableRows_Prefix="/html/body/div[1]/div/div[2]/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div["
problem_title_End = "]/div[2]/div/div/div/div/a"
difficulty_End = "]/div[5]/span"
problem_button_End = "]/div[2]/div/div/div"

pagePrefix = "/html/body/div[1]/div/div[2]/div[1]/div[1]/div[6]/div[3]/nav/button["
buttonLimit = page_total - 1
pageEnd = "]"
pageXPath = pagePrefix + str(buttonLimit) + pageEnd
lastPage_button = driver.find_element(by=By.XPATH, value=pageXPath)
lastPage = int(lastPage_button.text)
nextPage_XPath = pagePrefix + str(page_total) + pageEnd
# print(lastPage)

while page in range(1, lastPage+1):     
    tableRows = driver.find_elements(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[1]/div[6]/div[2]/div/div/div[2]/div")
    i = 1
    svgPrefix = '#__next > div > div.mx-auto.mt-\[50px\].w-full.grow.p-4.md\:mt-0.md\:max-w-\[888px\].md\:p-6.lg\:max-w-screen-xl > div.grid.grid-cols-4.gap-4.md\:grid-cols-3.lg\:grid-cols-4.lg\:gap-6 > div.col-span-4.z-base.md\:col-span-2.lg\:col-span-3 > div:nth-child(7) > div.-mx-4.md\:mx-0 > div > div > div:nth-child(2) > div:nth-child('
    svgEnd = ') > div:nth-child(1) > svg'
    time.sleep(3)
    for e in tableRows:
        if(page ==1 and i ==1):
            i+=1
            continue
        problem_title_xpath = tableRows_Prefix+str(i)+problem_title_End
        problem_title = driver.find_element(by=By.XPATH, value=problem_title_xpath)
        print(problem_title.text)
        problem_link = problem_title.get_attribute('href')
        print(problem_link)
        # time.sleep(2)
        difficulty_xpath = tableRows_Prefix+str(i)+difficulty_End
        # print(difficulty_xpath)
        difficulty = driver.find_element(by=By.XPATH, value=difficulty_xpath)
        print(difficulty.text)
    
        # time.sleep(2)
        cssSelector = svgPrefix + str(i) + svgEnd
        try:
            status_svg = driver.find_element(By.CSS_SELECTOR, cssSelector)
            status = status_svg.get_attribute('class')
            if 'green' in status:
                status = 'Solved'
            if 'yellow' in status:
                status = 'Attempted'
        except NoSuchElementException:
            status = 'To do'
        print(status)
        problem_button_xpath = tableRows_Prefix+str(i)+problem_button_End
        problem_button = driver.find_element(by=By.XPATH, value=problem_button_xpath)
        problem_button.click()
        time.sleep(5)
        submissions_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div/a[4]/div")
        submissions_button.click()
        time.sleep(5)
        submission_prefix = "/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div[2]/div["
        submission_endpath="]/div[1]/div[1]/div/div/span"
        dates_endpath = "]/div[1]/div[1]/span"
        submissionRows = driver.find_elements(by=By.XPATH, value="/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div[2]/div")
        submission_count = 0
        for s in submissionRows:
            # submission = s.find_element(by=By.XPATH, value=".//div[1]/div[1]/div/div/span")
            # print(submission.text)
            try:
                submission_count += 1
                submission_path = submission_prefix + str(submission_count)+ submission_endpath
                submission = s.find_element(by=By.XPATH, value=submission_path)
                print(submission.text)
                dates_path = submission_prefix + str(submission_count)+ dates_endpath
                dates = driver.find_element(by=By.XPATH, value=dates_path)
                print(dates.text)
            except NoSuchElementException:
                break
            except StaleElementReferenceException:
                break
        submission_count-=1
        print(submission_count)
        # back_svg = driver.find_element(By.CSS_SELECTOR,"#__next > div > div > div > nav > div > div > div.absolute.left-\[50\%\].hidden.-translate-x-2\/4.items-center.space-x-4.lc-md\:flex > div.flex.cursor-pointer.items-center.space-x-2 > svg")
        # back_svg.click()
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
 
        i+=1
        time.sleep(3)
    if (page == lastPage):
        break
    page_button = driver.find_element(by=By.XPATH, value=nextPage_XPath)

    page_button.click()
    time.sleep(3)
    page+=1



