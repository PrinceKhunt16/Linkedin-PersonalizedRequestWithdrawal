from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Start a new Chrome browser session
driver = webdriver.Chrome()

# Navigate to the LinkedIn login page
driver.get("https://www.linkedin.com/login")

# Log in to LinkedIn
username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')
username.send_keys('')  # Replace with your email
password.send_keys("")  # Replace with your password
driver.find_element(By.XPATH, '//*[@type="submit"]').click()

# Wait for the login process to complete
time.sleep(5)  # Adjust the sleep duration as needed

# Navigate to the "Sent invitations" page
driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")

# Wait for the page to load
time.sleep(5)  # Adjust the sleep duration as needed

# Extract the page source
page_source = driver.page_source

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, "html.parser")

# Find the ul element with class "artdeco-list mn-invitation-list"
ul_element = soup.find("ul", class_="artdeco-list mn-invitation-list")

# Find all li elements with class "invitation-card artdeco-list__item" within the ul element
li_elements = ul_element.find_all("li", class_="invitation-card artdeco-list__item")

# Extract the text from all a tags with class "app-aware-link" within each li element
names = []
for li in li_elements:
    a_tags = li.find_all("a", class_="app-aware-link")
    for a_tag in a_tags:
        names.append(a_tag.get_text(strip=True))

# Print the extracted names
filtered_names = []

for i in range(len(names)):
    if (i % 3 == 0):
        filtered_names.append(names[i+1])
        
print(filtered_names)

# Close the browser session
driver.quit()