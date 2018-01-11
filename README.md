# fuzzyattr

fuzzyattr matches the closest attribute name in python so you can make unlimited free typos.

## usage

Decorate any class.

```python
from fuzzyattr import fuzzyattr

@fuzzyattr
class Human:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        return f'{self.name} ate {food}'
```

Now you can make typos.

```python
someone = Human('Someone')
someone.ate('poop')
```

`ate` doesn't exist. fuzzyattr matches `eat`. It logs a warning when this happens.

## how is this useful?

Fix non-PEP8 code written by other morons. Make python standard library more pythonic.

```python
@fuzzyattr
class BetterTestCase(unittest.TestCase):
    pass
    
class PythonicTest(BetterTestCase):
    def test_thing(self):
        self.assert_equal(True, False)
        # much better than assertEqual
```

## install

```bash
pip install fuzzyattr
```