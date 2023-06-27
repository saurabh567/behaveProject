Feature: Prodinger login

  Scenario: Login in to Prodinger with valid parameters
    Given launch the chrome browser
    When open the prodinger page
    Then enter the username "kumar.saurabh@pixelmechanics.de" and password "prodinger@1234"
    Then click on login button
    #Then user must successfully login  to the homepage
    Then close the chrome browser


    Scenario Outline: Login in to Prodinger with Multiple parameters
    Given launch the chrome browser
    When open the prodinger page
    Then enter the username "<username>" and password "<password>"
    Then click on login button
    #Then user must successfully login  to the homepage
    Then close the chrome browser

      Examples:
      |username                       | password    |
      |kumar.saurabh@pixelmechanics.de|prodinger@1234|
      |shivani.singh@pixelmechanics.de| Shivani@2022 |
