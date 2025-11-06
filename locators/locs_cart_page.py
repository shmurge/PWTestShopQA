class CartPageLocators:
    ORDER_OVERVIEW = '[class="mb-4"]'
    EMPTY_CART_MESSAGE = '[class="js_cart_lines alert alert-info"]'
    PRODUCT_TITLE = '//*[contains(@class, "d-inline align-top")]'
    PRODUCT_PRICE = '[data-oe-expression="product_price"]'
    QUANTITY_INPUT = '[class="css_quantity input-group mb-2"] [type="text"]'

    SUBTOTAL_PRICE = '[id="order_total_untaxed"] [class="monetary_field"]'
    TAXES = '[id="order_total_taxes"] [class="monetary_field"]'
    TOTAL_PRICE = '[class="monetary_field text-end p-0"]'

    DELETE_PRODUCT_BUTTON = '[title="Remove from cart"]'
