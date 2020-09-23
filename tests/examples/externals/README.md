Stencils might make use of external symbols which are neither fields/variables nor
built-in dusk symbols. There should be a proper way to introduce them to dusk
so dusk knows whether a symbol usage is valid and what the symbol encodes.
Dusk then needs to _communicate_ the whole stencil program to dawn.

dusk can _communicate_ with dawn in various ways:

* built-in SIR elements/trees
* magic values/constants (e.g., magic integers or strings)
* command line flags (seems questionable)
* environment variables (seems like a bad idea)

(the last two options have the disadvantage that the .sir file can't be
compiled by a user unless they know the dawn flags/environment variables,
the .sir file wouldn't be _self contained_)

For some external symbols it's easiest to use magic values/constants during
prototyping. Later, proper ways to encode them in SIR can be added.
