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

        Scenario: search functionality
        Given launch the chrome browser
        When open the magento luma page
        Then click and type "bags"inside the search bar

          #inprogress
        Scenario Outline: search functionality with multiple search terms
          Given launch the chrome browser
          When open the magento luma page
          Then enter the multiple "<searchproduct>"

           Examples:
           |searchproduct|
           |watches      |
           |tops         |
           |bottoms      |
           |jackets      |

   #inprogress
  Scenario:handling header links by opening each of them in a separate tab
   Given launch the chrome browser
    When open the magento luma page
    Then click on each of the header links to open them in a new tab


  Scenario: Magento footer section links
    Given launch the chrome browser
    When open the magento luma page
    Then click on the About us link
    Then click on the Customer service link
    Then click on the Privacy and cookie policy link
    Then click on the Search Terms link
    Then click on the Advanced Search link
    Then click on the orders and Returns link
    Then click on the Contact us link


  Scenario: Hot sellers sections
    Given launch the chrome browser
    When open the magento luma page
    #Then click on the first product image
    Then click on each of the different sizes box individually
    #Then navigate to the previous page
    Then click on each of the colour swatches
    Then click add to cart button
    Then navigate to the counter quantity button to check the product has been added
    Then click on proceed to checkout

  Scenario: creating a new account
    Given launch the chrome browser
    When open the magento luma page
    Then click on Create an account link
    Then filling the personal information
    Then filling the signin information
    Then click on the create an account button


