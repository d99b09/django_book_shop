from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class SGPagination(LimitOffsetPagination):

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_pages': int(self.count / self.limit),
            'count': self.count,
            'results': data
        })
