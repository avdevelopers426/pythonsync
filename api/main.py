from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from flask import Flask, request

app = Flask(__name__)

@app.route("/result",methods=["POST","GET"])

def result():

	form_data = request.get_json()
	
	chrome_options = Options()
	#chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without opening the browser window)

	# Create a new instance of the Chrome driver
	driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

	# Define the URL of the web page
	url = "https://www.opticutter.com/cut-list-optimizer"

	# Navigate to the web page
	driver.get(url)


	# Find the form element using appropriate selectors (e.g., ID, class, etc.)
	form = driver.find_element(By.ID, "planForm")

	# Find the input fields within the form and fill in the desired values
	input_field1 = form.find_element(By.NAME, "stocks[0].length")
	input_field1.send_keys("1250")

	input_field2 = form.find_element(By.NAME, "stocks[0].width")
	input_field2.send_keys("2500")

	input_field3 = form.find_element(By.NAME, "stocks[0].count")
	input_field3.send_keys("2")


	# Find the input fields within the form and fill in the desired values
	input_field1 = form.find_element(By.NAME, "requirements[0].length")
	input_field1.send_keys("297")

	input_field2 = form.find_element(By.NAME, "requirements[0].width")
	input_field2.send_keys("420")

	input_field3 = form.find_element(By.NAME, "requirements[0].count")
	input_field3.send_keys("40")


	#driver.implicitly_wait(500) 

	#result = driver.page_source

	# Submit the form
	form.submit()

	# Wait for the page to load after form submission
	#driver.implicitly_wait(10)  # Wait for 5 seconds (adjust as needed)
	#driver.page_source
	target_div = driver.find_element(By.CSS_SELECTOR, ".tab-pane.active > .card-body > table")
	div_html = target_div.get_attribute("outerHTML")
	print(div_html)
	if div_html:
		return div_html;
	else:
		return "error";


#APP = result()

#if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=5000, debug=True)
    #app.run(debug=True,host='pythonsync.onrender.com')


# Set the path to the chromedriver executable
#webdriver_service = Service('C:/Users/MS/Downloads/pyirf-main/chromedriver_win32/chromedriver.exe')

# Configure Chrome options

#time.sleep(50)
# Store the result in a variable
#result = driver.page_source

# Print or process the result as desired
#print(result)

# Close the browser
#driver.quit()
