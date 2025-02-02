"""Middleware to authenticate using Google tokens."""

import re

import requests
from allauth.socialaccount.models import SocialToken


class GoogleAuthMiddleware:
    """Google Authentication Middleware."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip protection for unauthenticated or specific endpoints
        excluded_patterns = [
            r"^/accounts/login/$",
            r"^/accounts/logout/$",
            r"^/accounts/signup/$",
            r"^/accounts/google/.*$",  # Match all Google login paths
        ]

        # Skip middleware for excluded patterns
        if any(re.match(pattern, request.path) for pattern in excluded_patterns):
            return self.get_response(request)

        # Retrieve and validate the Google token
        social_token = SocialToken.objects.get(
            account__user=request.user, account__provider="google"
        )
        url = (
            f"https://oauth2.googleapis.com/tokeninfo?access_token={social_token.token}"
        )
        response = requests.get(url)

        # Continue processing the request
        response = self.get_response(request)
        return response
