Feature: Flipkart logo
  Scenario: Logo presence on the flipkart page
    Given launch chrome browser
    When open the flipkart page
    Then verify the flipkart logo present on the page
    #Then close the browser

Scenario: Presence on the flipkart page
    Given launch chrome browser
    When open the flipkart page
    Then click on the popupclose button
    Then click on the seller button