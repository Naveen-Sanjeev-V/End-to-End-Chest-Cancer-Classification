import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME = "End-to-End-Chest-Cancer-Classification"
AUTHOR_NAME = "Naveen-Sanjeev-V"
SRC_REPO = "chest_cancer_classification"
AUTHOR_EMAIL = "naveensanjeev712@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)