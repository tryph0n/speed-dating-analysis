import importlib

LIBRARIES = ["pandas", "numpy", "matplotlib", "seaborn", "scipy"]


def test_libraries_import():
    for name in LIBRARIES:
        importlib.import_module(name)
