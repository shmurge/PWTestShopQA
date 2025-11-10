class ProductPageLocators:
    PRODUCT_TITLE = '[itemprop="name"]'
    PRODUCT_PRICE = '[class="oe_price"]'
    ADD_TO_CART_BUTTON = '[id="add_to_cart"]'
    ADD_ONE_BUTTON = '[id="o_wsale_cta_wrapper"] [title="Add one"]'
    REMOVE_ONE_BUTTON = '[id="o_wsale_cta_wrapper"] [title="Remove one"]'
    LOADER_IN_ADD_QUAN_BUTTON = '[class="fa fa-refresh fa-spin me-2"]'
    QUANTITY_INPUT = '[id="o_wsale_cta_wrapper"] [name="add_qty"]'

    RADIO_BUTTON_MATERIAL = '[type="radio"][data-attribute_name="Legs"]'
    RADIO_BUTTON_STEEL = '[type="radio"][data-value_name="Steel"]'
    RADIO_BUTTON_ALUMINIUM = '[type="radio"][data-value_name="Aluminium"]'
    RADIO_BUTTON_CUSTOM = '[type="radio"][data-value_name="Custom"]'
    INPUT_CUSTOM = '[data-attribute_value_name="Custom"]'

    RADIO_BUTTON_COLOR = '[type="radio"][data-attribute_name="Color"]'
    RADIO_BUTTON_BLACK = '[style="background:#000000"]'
    RADIO_BUTTON_WHITE = '[style="background:#FFFFFF"]'

    PRODUCT_DESCRIPTION = '//*[contains(@placeholder, "A short description")]'
    PRODUCT_PHOTO = '//*[contains(@class, "img img-fluid oe")]'

    CUSTOMIZE_DESK_PHOTO_ALUM_WHITE = '//*[contains(@src, "/web/image/product.product/14/")]'
    CUSTOMIZE_DESK_PHOTO_STEEL_BLACK = '//*[contains(@src, "/web/image/product.product/13/")]'
    CUSTOMIZE_DESK_PHOTO_STEEL_WHITE = '//*[contains(@src, "/web/image/product.product/12/")]'
    CUSTOMIZE_DESK_PHOTO_CUSTOM_WHITE = '//*[contains(@src, "/web/image/product.product/36/")]'
    CUSTOMIZE_DESK_PHOTO_CUSTOM_BLACK = '//*[contains(@src, "/web/image/product.product/37/")]'
