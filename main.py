from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_contact_form_submission():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.talktosomto.xyz/contact")

        wait = WebDriverWait(driver, 8)

        name_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "name"))
        )
        email_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        work_type_element = wait.until(
            EC.visibility_of_element_located((By.NAME, "workType"))
        )
        timeline_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "timeline"))
        )
        budget_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "budget"))
        )
        message_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "details"))
        )

        name_input.send_keys("Somto")
        email_input.send_keys("my@email.com")
        Select(work_type_element).select_by_visible_text("Collaboration")
        timeline_input.send_keys("Full-time employment")
        budget_input.send_keys("N150,000/month")
        message_input.send_keys("Hello world!")

        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//button[@type='submit' and contains(., 'Send message')]")
            )
        )

        assert submit_button.is_enabled()

        submit_button.click()

        success_message = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(., 'Message received')]")
            )
        )

        assert success_message.is_displayed()

    finally:
        driver.quit()
