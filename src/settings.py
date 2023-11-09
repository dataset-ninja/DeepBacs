from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "DeepBacs E. Coli"
PROJECT_NAME_FULL: str = (
    "DeepBacs: Escherichia Coli Antibiotic Phenotyping Object Detection Dataset and YOLOv2 Model"
)
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Research.Biomedical()]
CATEGORY: Category = Category.Medical(extra=Category.Biology())

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2021-10-05"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://zenodo.org/record/5551057#.YlFcXn9Bzmg"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 830027
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/DeepBacs"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "Antibiotic_profiling_examples.png": "https://zenodo.org/record/5551057/files/Antibiotic_profiling_examples.png?download=1",
    "DeepBacs_Data_Object_Detection_E.coli_Antibiotic_Phenotyping.zip": "https://zenodo.org/record/5551057/files/DeepBacs_Data_Object_Detection_E.coli_Antibiotic_Phenotyping.zip?download=1",
    "DeepBacs_Model_Object_Detection_E.coli_Antibiotic_Phenotyping.zip": "https://zenodo.org/record/5551057/files/DeepBacs_Model_Object_Detection_E.coli_Antibiotic_Phenotyping.zip?download=1",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "Rifampicin": [255, 0, 0],
    "Oblique": [0, 255, 0],
    "Nalidixate": [0, 0, 255],
    "Mecillinam": [255, 255, 0],
    "CAM": [255, 0, 255],
    "Vesicle": [0, 255, 255],
    "Control": [255, 165, 0],
    "MP265": [220, 190, 255],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://www.biorxiv.org/content/10.1101/2021.11.03.467152v1"
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {"GitHub":"https://github.com/HenriquesLab/DeepBacs/wiki"}

CITATION_URL: Optional[str] = "https://zenodo.org/record/5551057#.YlFcXn9Bzmg"
AUTHORS: Optional[List[str]] = [
    "Christoph Spahn",
    "Romain F. Laine",
    "Pedro Matos Pereira",
    "Estibaliz Gómez-de-Mariscal",
    "Lucas von Chamier",
    "Mia Conduit",
    "Mariana Gomes de Pinho",
    "Guillaume Jacquemet",
    "Séamus Holden",
    "Mike Heilemann",
    "Ricardo Henriques",
]
AUTHORS_CONTACTS: Optional[List[str]] = ["christoph.spahn@mpi-marburg.mpg.de"]

ORGANIZATION_NAME: Optional[
    Union[str, List[str]]
] = "Institute of Physical and Theoretical Chemistry, Goethe-University Frankfurt, Germany"
ORGANIZATION_URL: Optional[
    Union[str, List[str]]
] = "https://www.ptc.uni-frankfurt.de/home/index.php"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None


##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
