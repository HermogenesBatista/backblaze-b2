from setuptools import setup, find_packages
print 'pota que pariules'
print 'nois que voa bruxao'

setup(
    name='backblaze',
    version='0.1',
    packages=find_packages(),
    license=open("LICENSE").read(),
    long_description=open('README.md').read(),
    install_requires=["pycrypto==2.6.1"]
)
