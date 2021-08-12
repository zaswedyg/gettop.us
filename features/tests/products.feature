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