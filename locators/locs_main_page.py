class MainPageLocators:
    SEARCH_INPUT = '[id="products_grid"] [name="search"]'

    MESSAGE_ON_PAGE_NO_SEARCHING_RESULTS = '//*[contains(@class, "text-center text-muted")]'
    SEARCHING_RESULT_CNT = '//*[contains(@class, "products_header")]/descendant::*[@class="oe_search_found"]'

    PRODUCT_TITLE = '[itemprop="name"]'
    PRODUCT_PRICE = '[class="product_price"]'
