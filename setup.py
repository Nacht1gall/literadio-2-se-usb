from setuptools import setup

setup(
    name='literadio2_se_usb',
    version='0.0.1',
    description='BETAFPV LiteRadio 2 SE Radio Transmitter USB.',
    long_description=
    """
    BETAFPV LiteRadio 2 SE Radio Transmitter USB.
    License: MIT
    """,
    author_email='johnherbertdillinger@ukr.net',
    license='MIT',
    platforms='any',
    url='https://github.com/Nacht1gall/literadio-2-se-usb',
    keywords=['betafpv', 'drone', 'controller'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'pyusb==1.2.1',
    ],
)
