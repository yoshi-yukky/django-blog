from django.views import generic
from common.decorators import disable_side_bar


@disable_side_bar
class ProfileView(generic.TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["side_menu"] = True
        return context
