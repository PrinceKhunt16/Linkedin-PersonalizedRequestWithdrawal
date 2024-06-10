from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configure the WebDriver (assuming Chrome)
driver = webdriver.Chrome()  # Update the path if needed

# Open LinkedIn
driver.get('https://www.linkedin.com/login')

# Log in to LinkedIn
username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')
username.send_keys("")  # Replace with your email
password.send_keys("")  # Replace with your password
driver.find_element(By.XPATH, '//*[@type="submit"]').click()

# Wait for the page to load
time.sleep(5)

# Navigate to 'Manage invitations'
driver.get('https://www.linkedin.com/mynetwork/invitation-manager/sent/')

# Wait for the page to load
time.sleep(5)

# Function to withdraw a single invitation
def withdraw_invitation(name):
    try:
        withdraw_buttons = driver.find_elements(By.XPATH, f'//button[contains(@aria-label, "Withdraw invitation sent to {name}")]')
        if withdraw_buttons:
            withdraw_buttons[0].click()
            time.sleep(3)  # Wait for the withdrawal to complete
            # Handle the confirmation popup (click on the 'Withdraw' button)
            withdraw_confirm_button = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary')
            withdraw_confirm_button.click()
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    
# Loop to withdraw all invitations
names = []

# Loop to withdraw all invitations
for name in names:
    while True:
        if not withdraw_invitation(name):
            break

# Close the browser
driver.quit()
