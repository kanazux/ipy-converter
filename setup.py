from setuptools import setup


setup(name="ipy_converter",
      packages=["ipy_converter"],
      scripts=['scripts/ipy-show'],
      version='0.1',
      description='A simple ip converter and stats.',
      long_description=("Convert an ip and maks in slash notation to binary. "
                        "Calcule the number max of hosts, number max of subnet"
                        " the network ip and broadast."),
      author='Silvio Ap Silva a.k.a Kanazuchi',
      author_email='contato@kanazuchi.com',
      url='http://github.com/kanazux/ipy-converter',
      zip_safe=False)
