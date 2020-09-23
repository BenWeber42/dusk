from dusk.script import *

# A `definitions.py` could be one way to naturally introduce symbols that can
# be imported and used in dusk stencils.

regions = Regions(
    # Here we specify which magic integers to use. This enables us to quickly
    # prototype new features. Once SIR has built-in support for this, it can
    # be changed.
    lb=1,
    nudging=2,
    interior=3,
    halo=4,
)

# string encoding
another_regions = HorizontalRegions(
    lb="lb", nudging="nudging", interior="interior", halo="halo"
)
# compact string encoding
regions_again = HorizontalDomains("lb", "nudging", "interior", "halo")

# with python's value unpacking, we can introduce quick shortcuts as well
lb, nudging, interior, halo = regions = Domains("lb", "nudging", "interior", "halo")

# can also skip `regions`
lb, nudging, interior, halo = Domains("lb", "nudging", "interior", "halo")

# Now these external symbols are well integrated in Python. Dusk can import them
# and find out what to do based on the type of the objects.
# E.g., encode `Regions` through the corresponding magic integers/strings.

# Other kinds of external symbols can be easily supported as well.
k_flat = VerticalLevel("k_flat")

# Classes like `HorizontalRegions` or `VerticalLevel` can be defined in `dusk.script`

# Other more advanced features can also be supported with a `definitions.py`.
# E.g., introducing aliases:
VertexDiamond = Edge > Cell > Vertex
EdgeDiamond = Edge > Cell > Edge

# or simple model constants
g = 9.81

# A `definitions.py` would be similar to a C++ header file that can be reused
# by multiple stencils.
