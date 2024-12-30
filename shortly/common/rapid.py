from typing import Any

from django.conf import settings
from requests import Timeout, TooManyRedirects, request
from requests.models import Response
from urllib3.exceptions import MaxRetryError


class APIConnectionErrorException(Exception):
    """Exception raised for API connection errors."""

    pass


class RapidAPI:
    """Class to communicate with RapidAPI endpoint."""

    def __init__(self) -> None:
        """RapidAPI Constructor."""
        self.headers: dict[str, str] = {
            "x-rapidapi-key": settings.X_RAPID_API_KEY,
            "x-rapidapi-secret": settings.X_RAPID_API_SECRET,
            "Content-Type": "application/json",
        }

        self.base_url = settings.RAPID_API_HOST

    def api_call(
        self,
        url: str,
        method: str = "POST",
        payload: dict[str, Any] | None = None,  # type: ignore
    ) -> Response:
        """General API call that other methods will use.

        Args:
            url: The API `URL` to hit.
            method: `HTTP` request method. Either `POST` or `GET`.
            headers: `HTTP` headers.
            payload: Holds the payload to send to the API.

        Returns:
            An API response if successful.

        Raises:
            APIConnectionErrorException: If there's an error connecting to Cube.
        """
        request_kwargs: dict[str, Any] = {"headers": self.headers}
        request_kwargs["json"] = payload

        try:
            response = request(method, url, **request_kwargs)
        except (
            ConnectionError,
            TooManyRedirects,
            Timeout,
            MaxRetryError,
        ) as e:
            error_msg = str(e)
            raise APIConnectionErrorException(error_msg)
        return response
