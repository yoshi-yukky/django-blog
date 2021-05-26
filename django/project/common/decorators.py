from django.views.generic.base import ContextMixin


def disable_side_bar(cls):
    assert issubclass(cls, ContextMixin), "ContextBaseMixinを継承していません。"

    get_context_data = cls.get_context_data
    def _replaced_function(*args, **kwargs):
        context = get_context_data(*args, **kwargs)
        context["disable_side_menu"] = True
        return context

    cls.get_context_data = _replaced_function
    return cls
