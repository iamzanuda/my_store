from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    """
    Custom pagination class for Product viewsets.

    This class customizes the pagination behavior for the product listings.
    It sets a default page size and allows clients to override it by
    providing a 'page_size' query parameter. The maximum page size is also
    restricted to prevent excessively large responses.

    Attributes:
        page_size (int): The default number of items per page.
        page_size_query_param (str): The query parameter that allows clients
            to set a custom page size.
        max_page_size (int): The maximum number of items allowed per page.
    """

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50
