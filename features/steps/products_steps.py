from behave import given, when, then



@given('Open Shop page')
def open_shop_page(context):
    context.app.shop.open_shop_page()

@when('Open Quick View')
def open_quick_view(context):
    context.app.shop.open_quick_view()

@when('Selecting non-match filter')
def select_extreme_filter(context):
    context.app.shop.select_extreme_filter()
    context.app.shop.press_filter_button()

@then('Verify user can close by clicking on X')
def verify_user_can_close_by_clicking_x(context):
    context.app.shop.close_quick_view_by_x()

@then('Verify user can add product to cart')
def verify_user_can_add_product_to_cart(context):
    context.app.shop.verify_user_can_add_product_to_cart()

@then('Verify user can click through multiple product pages by clicking 1, 2 for page number')
def verify_user_can_click_through_multiple_page_numbers(context):
    context.app.shop.verify_user_can_click_through_multiple_page_numbers()

@then('Verify user can click trough multiple product pages by clicking > and <')
def verify_user_can_click_through_multiple_pages_by_clicking_next_and_back(context):
    context.app.shop.verify_user_can_click_through_multiple_pages_by_clicking_next()
    context.app.shop.verify_user_can_click_through_multiple_pages_by_clicking_back()

@then('Verify "No products were found matching your selection." message appears')
def verify_no_product_found_message_appears(context):
    context.app.shop.verify_no_product_found_message_appears()

@then('Clear filter and verify products are displayed')
def clear_filter_and_verify_products_are_displayed(context):
    context.app.shop.clear_filter_and_verify_products_are_displayed()