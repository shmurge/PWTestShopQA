class HeaderPageLocators:
    MAIN_LOGO = '[id="o_main_nav"] [title="My Website"]'
    LINK_CART = '[id="o_main_nav"] [href="/shop/cart"]'
    COUNTER_ON_CART = '//*[@id="o_main_nav"]/descendant::*[contains(@class, "my_cart_quantity")]'
    LINK_SIGN_IN = '[id="o_main_nav"] [href="/web/login"]'
    BUTTON_MAIN_SEARCH = '[id="o_main_nav"] [title="Search"]'
    USERNAME = '[class="small"]'
    MY_ACCOUNT_BUTTON = '[class="dropdown o_no_autohide_item"] [href="/my/home"]'
    LOGOUT_BUTTON = '[class="dropdown o_no_autohide_item"] [id="o_logout"]'
