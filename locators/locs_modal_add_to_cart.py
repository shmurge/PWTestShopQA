class ModalAddToCartLocators:
    PRODUCT_TITLE = '//*[contains(@class, "js_product in_cart")]/descendant::strong'
    PRODUCT_PRICE = '//*[contains(@class, "js_product in_cart")]/descendant::*[@class="oe_price product_id"]'
    TOTAL_PRICE = '[class="js_price_total fw-bold"]'

    ADD_TO_CART_MODAL = '[class="modal-content"]'
    ADD_ONE_BUTTON = '[class="text-center td-qty"] [title="Add one"]'
    REMOVE_ONE_BUTTON = '[class="text-center td-qty"] [title="Remove one"]'
    QUANTITY_INPUT = '[class="text-center td-qty"] [name="add_qty"]'
    CLOSE_ADD_TO_CART_MODAL_BUTTON = '[class="modal-content"] [aria-label="Close"]'

    CONTINUE_SHOPPING_BUTTON = '//*[@class="btn btn-secondary"]'
    PROCEED_TO_CHECKOUT_BUTTON = '//*[contains(@class, "btn btn-primary o_sa")]'

    PRODUCT_PHOTOS_IN_MODAL = '[alt="Product Image"]'
