from django.conf import settings
from django.shortcuts import render

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if maintenance mode is enabled in settings
        is_maintenance = getattr(settings, 'MAINTENANCE_MODE', False)

        if is_maintenance:
            # Allow access to exempt URLs (default includes admin panel)
            exempt_urls = getattr(settings, 'MAINTENANCE_MODE_EXEMPT_URLS', ['/admin/'])

            # Check if the current path matches any exempt URL
            path = request.path_info
            if any(path.startswith(url) for url in exempt_urls):
                return self.get_response(request)

            # Allow access to staff members (if AuthenticationMiddleware is loaded before this)
            if hasattr(request, 'user') and request.user.is_authenticated and request.user.is_staff:
                return self.get_response(request)

            # Render the maintenance page with 503 Service Unavailable status
            return render(request, 'core/maintenance.html', status=503)

        return self.get_response(request)
