from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def authentication_error(self, request, provider_id, error=None, exception=None, extra_context=None):
        """Bypass the login confirmation page"""
        return self.respond_authentication_error(request, provider_id, error, exception, extra_context)
