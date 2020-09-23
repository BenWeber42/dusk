from dusk.script import *

# integration works naturally through python's import mechanism
from definitions import *


@stencil
def horizontal_subdomains(edge1: Field[Edge, K]):

    # examples of dusk syntax for horizontal subdomains

    # short + slice syntax
    with levels_upward, domain[nudging : halo - 1]:
        edge1 = 1
        # ...

    # short + list syntax
    with levels_upward, [nudging, halo - 1]:
        edge1 = 1
        # ...

    # long + slice syntax
    with levels_upward, domain[regions.nudging : regions.halo - 1]:
        edge1 = 1
        # ...

    # long + list syntax
    with levels_upward, [regions.nudging, regions.halo - 1]:
        edge1 = 1
        # ...

    # `in` operator + short + slice syntax
    with levels_upward in domain[nudging : halo - 1]:
        edge1 = 1
        # ...

    # The `in` operator is problematic with lists (_weird python_)
    with levels_downward[:k_flat] in [lb, nudging]:
        edge1 = 1
        # ...

    # `in` also isn't symmetric in python (_weird python_)
    with domain[:nudging] in levels_downward[5:]:
        edge1 = 1
        # ...

    # reusing `levels_downward` & `levels_upward` + nested comma index
    with levels_upward[k_flat:-5][nudging - 1, halo]:
        edge1 = 1
        # ...

    # reusing `levels_downward` & `levels_upward` + comma slice
    with levels_upward[k_flat:-5, nudging - 1 : halo]:
        edge1 = 1
        # ...

    # maybe we should also rethink `levels_upward` and `levels_downward`

    with domain[7:-7][interior:halo]:
        edge1 = 1
        # ...

    with domain.vertical[7:-7].horizontal[interior:halo]:
        edge1 = 1
        # ...

    with domain.upward[7:-7].accross[interior:halo]:
        edge1 = 1
        # ...

    with domain.accross[interior - 1 : halo].downward[7:-7]:
        edge1 = 1
        # ...

