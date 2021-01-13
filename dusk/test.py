from typing import Callable

from dusk.integration import StencilObject
from dusk.transpile import validate as validate_sir, stencil_object_to_sir


# FIXME: properly design & implement testing infrastructure


def stencil_test(validate: bool = True) -> Callable:

    assert isinstance(validate, bool)

    def decorator(stencil: Callable) -> Callable:
        assert stencil.__name__.startswith("test_")

        def test_stencil() -> None:
            sir = stencil_object_to_sir(StencilObject(stencil))
            if validate:
                validate_sir(sir)

        return test_stencil

    return decorator
