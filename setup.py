import sys
from setuptools import setup

try:
    from setuptools_rust import Binding, RustExtension
except ImportError:
    import subprocess

    errno = subprocess.call([sys.executable, "-m", "pip", "install", "setuptools-rust"])
    if errno:
        print("Please install setuptools-rust package")
        raise SystemExit(errno)
    else:
        from setuptools_rust import Binding, RustExtension

setup_requires = ["setuptools-rust>=0.9.2"]
install_requires = []

setup(
    name="gym_chess",
    version="0.2",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
    ],
    rust_extensions=[
        RustExtension("gym_chess.gym_chess", "Cargo.toml", binding=Binding.PyO3, debug=False)
    ],
    packages=["gym_chess"],
    zip_safe=False,
    install_requires=["gym>=0,<1", "numpy>=1,<2", "six>=1,<2"],
    extras_require={"dev": ["pytest", "black"]},
)
