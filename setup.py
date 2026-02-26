from setuptools import setup
import glob

setup(
    name="OligoMiner",
    version="1.0",
    scripts=glob.glob("./*.py"),
)
