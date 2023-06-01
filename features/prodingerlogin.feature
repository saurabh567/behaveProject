Feature: Prodinger login

  Scenario: Login in to Prodinger with valid parameters
    Given launch the chrome browser
    When open the prodinger page
    Then enter the username "kumar.saurabh@pixelmechanics.de" and password "prodinger@1234"
    Then click on login button
    #Then user must successfully login  to the homepage
    Then close the chrome browser
