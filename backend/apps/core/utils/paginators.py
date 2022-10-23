from rest_framework.pagination import PageNumberPagination

PAGE_SIGE_PARAM = "page_size"

class Pagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = PAGE_SIGE_PARAM
    max_page_size = 50

