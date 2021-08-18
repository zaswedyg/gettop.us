# Created by yurka at 8/9/2021
Feature: Products

  Scenario: User can open and close Quick View by clicking on closing X
    Given Open Shop page
    When Open Quick View
    Then Verify user can close by clicking on X

  Scenario: User can click Quick View and add product to cart
    Given Open Shop page
    When Open Quick View
    Then Verify user can add product to cart

  Scenario: User can click through multiple product pages by clicking 1, 2 for page number
    Given Open Shop page
    Then Verify user can click through multiple product pages by clicking 1, 2 for page number

  Scenario: User can click trough multiple product pages by clicking > and <
    Given Open Shop page
    Then Verify user can click trough multiple product pages by clicking > and <

  Scenario: "No products were found matching your selection." message shown if no products match selected filters
    Given Open Shop page
    When Selecting non-match filter
    Then Verify "No products were found matching your selection." message appears

  Scenario: If user resets applied filters from No match, the products are shown
    Given Open Shop page
    When Selecting non-match filter
    Then Clear filter and verify products are displayed