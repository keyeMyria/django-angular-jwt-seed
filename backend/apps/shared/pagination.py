from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)
from rest_framework.response import Response


class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class CommonPageNumberPagination(PageNumberPagination):
    page_size = 30

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data
        })
