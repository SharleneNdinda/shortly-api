from allauth.socialaccount.models import SocialToken, SocialAccount
from allauth.socialaccount.signals import social_account_added, social_account_updated
from django.dispatch import receiver

@receiver(social_account_added)
@receiver(social_account_updated)
def save_google_token(sender, request, sociallogin, **kwargs):
    if sociallogin.account.provider == "google":
        # Get the token
        token = SocialToken.objects.get(account=sociallogin.account)
        # Save the token in the user's profile
        user = sociallogin.user
        user.google_token = token.token
        user.save()
