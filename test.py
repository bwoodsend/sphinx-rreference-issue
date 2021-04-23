class Foo:
    def foo(self):
        """A docstring."""
        pass


class Bar(Foo):
    def uses_foo(self):
        """This method calls :meth:`foo`.""" # <- This cross reference won't work!
        self.foo()
