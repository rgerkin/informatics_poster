try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='neuronunit',
    version='0.1.8.6',
    author='Rick Gerkin',
    author_email='rgerkin@asu.edu',
        packages=[
            'neuronunit',
            'neuronunit.capabilities',
            'neuronunit.neuroconstruct',
            'neuronunit.neuron',
            'neuronunit.models',
            'neuronunit.tests'],
    url='http://github.com/scidash/neuronunit',
    license='MIT',
    description='A SciUnit library for data-driven testing of single-neuron physiology models.',
    long_description="",
    install_requires=['scipy>=0.17',
                      'matplotlib>=1.5',
                      'neo==0.4',
                      'elephant',
                      'sciunit==0.1.5.6',
                      'allensdk==0.12.4.1',
                      'pyneuroml>=0.2.3',
                      'scoop'],
    dependency_links = ['https://github.com/scidash/sciunit/tarball/dev#egg=sciunit-0.1.5.6',
                        'https://github.com/rgerkin/AllenSDK/tarball/python3.5#egg=allensdk-0.12.4.1',
                        'https://github.com/rgerkin/pyNeuroML/tarball/master#egg=pyneuroml-0.2.3']
)
