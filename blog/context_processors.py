from .models import Application, Module


def add_active_apps_and_modules(request):
    applications = Application.objects.filter(active=True)
    modules = Module.objects.filter(active=True)
    return {
        'applications': applications,
        'modules': modules,
    }
