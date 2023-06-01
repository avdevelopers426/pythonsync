from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
from flask import Flask,request

app = Flask(__name__)

@app.route("/result",methods=["POST"])

def result():
	data = request.json
	print(data['a_length'])
	
	
	chrome_options = Options()
	chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without opening the browser window)

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
	input_field1.send_keys(data['a_length'])

	input_field2 = form.find_element(By.NAME, "stocks[0].width")
	input_field2.send_keys(data['a_width'])

	input_field3 = form.find_element(By.NAME, "stocks[0].count")
	input_field3.send_keys(data['a_qty'])

	input_field4 = form.find_element(By.NAME, "settings.kerf")
	input_field4.send_keys(data['cut_width'])
	
	#elements = driver.find_elements(By.CLASS_NAME, ".card-body.py-1")
	#elements2=elements[2].find_elements(By.CLASS_NAME, ".switcher")
	grain = driver.find_element(By.ID, "settings.grain")
	grain.find_element(By.XPATH, "..").click()
	#elements2.click()

	r_panel_values = data.get('r_panel', [])

	x=0
	js_code = """
		addRequirementsRow2d(1, 'Delete', 'Horizontal', 'Vertical', true);
		"""

		# Call the JavaScript function
	
	#planReqTablebutton = driver.find_element(By.CSS_SELECTOR, ".d-xs-block .btn.mb-2:first-child")
	#planReqTablebutton.click()
	print(len(r_panel_values))
	for panel in r_panel_values:
		input_field1 = form.find_element(By.NAME, "requirements["+str(x)+"].length")
		input_field1.send_keys(panel.get('r_length'))

		input_field2 = form.find_element(By.NAME, "requirements["+str(x)+"].width")
		input_field2.send_keys(panel.get('r_width'))

		input_field3 = form.find_element(By.NAME, "requirements["+str(x)+"].count")
		input_field3.send_keys(panel.get('r_qty'))

		input_field4 = Select(form.find_element(By.NAME, "requirements["+str(x)+"].grainDirection"))
		input_field4.select_by_value(panel.get('grainDirection'))
		if len(r_panel_values)!=x+1:
			driver.execute_script(js_code)
		x=x+1;

	#time.sleep(50)
	try:
		form.submit()
	except StaleElementReferenceException:
		return "error";
	# Find the input fields within the form and fill in the desired values
	
	

	
	#driver.implicitly_wait(500) 

	#result = driver.page_source

	# Submit the form
	#form.submit()

	# Wait for the page to load after form submission
	#driver.implicitly_wait(10)  # Wait for 5 seconds (adjust as needed)
	#driver.page_source
	#time.sleep(50)
	try:
		target_div = driver.find_element(By.CSS_SELECTOR, ".tab-pane.active > .card-body > table")
	except NoSuchElementException:
		return "error";

	div_html = target_div.get_attribute("outerHTML")
	#print(div_html)
	if div_html:
		return div_html;

	"""if len(target_div) == 0:
		return "error";

	div_html = target_div.get_attribute("outerHTML")
	#print(div_html)
	if div_html:
		return div_html;
	else:
		return "error";"""


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
