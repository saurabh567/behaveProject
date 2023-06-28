Feature: Magento login

  Scenario: Login in to Magento with valid parameters
    Given launch the chrome browser
    When open the magento luma page
    Then click on signin button
    Then enter the username "kumar.saurabh@pixelmechanics.de" and password "magento@1234"
    Then click on signin button of customer account page
    Then close the chrome browser


    Scenario Outline: Login in to Magento with Multiple parameters
    Given launch the chrome browser
    When open the magento luma page
    Then click on signin button
    Then enter the username "<username>" and password "<password>"
    Then close the chrome browser

      Examples:
      |username                           | password    |
      |kumar.saurabh@pixelmechanics.de    |magento@1234 |
      |testkumar.saurabh@pixelmechanics.de| magento@1234|



      Scenario: showcartbutton functionality
        Given launch the chrome browser
        When open the magento luma page
        Then click on the action showcart button
        Then get the title of the page
        Then click here link to continue shopping
