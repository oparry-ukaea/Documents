# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import glob
import os
import re
import shutil
import sys
import warnings
from pdfminer.high_level import extract_text

sys.path.insert(0, os.path.abspath("."))
from titles_from_bibtex import get_path_to_title_from_bibtex

project = "Excalibur-Neptune Documents"
copyright = "2023, UKAEA"
author = "UKAEA"
release = "0.0.1"


def strip_regex(regex_str, title):
    pattern = re.compile(regex_str, re.IGNORECASE)
    title = pattern.sub("", title)
    return title


def discard_non_title_lines(lines):
    line_after_title = 10000000
    for i, line in enumerate(lines):
        if len(line.split(",")) > 3:  # list of authors
            line_after_title = min(i, line_after_title)
        if (line.find("University") > -1) or (line.find("College") > -1):
            line_after_title = min(i, line_after_title)
        try:
            int(line)
            del lines[i]
        except:
            pass
    lines = lines[0:line_after_title]
    lines = [x for x in lines if x.strip() != ""]
    return lines


def get_raw_title_from_text(pdftxt):
    counter = 0
    location = 0
    for i in re.finditer("\n", pdftxt):
        counter += 1
        location = i.start()
        if counter == 10:
            break
    title = pdftxt[0:location]
    title = strip_regex(r"T/[A-Z]*[0-9]*/[0-9]", title)  # e.g. T/AW012/34
    title = strip_regex(r"[0-9]*-TN-\d\d", title)  # e.g. 2012345-TN-01
    title = strip_regex(r"D\d\.\d:", title)  # e.g. D1.2:
    title = strip_regex(r"D\d\.\d", title)  # e.g. D1.2
    title = strip_regex(r"Task [0-9]", title)  # e.g. Task 1
    title = strip_regex(r"Task [0-9]*\.[0-9]", title)  # e.g. Task 1.2
    title = strip_regex(r"[A-Za-z]+\s\d", title)  # e.g. Task 1.2
    title = strip_regex(r"TN-[0-9]*-[0-9]*:", title)  # e.g. TN-01-23
    title = strip_regex(r"TN-[0-9]", title)  # e.g. TN-01
    title = strip_regex(r"-\d: ", title)  # e.g. "-3: "
    title = strip_regex(r"\s:", title)  # e.g. " :"
    title = strip_regex(r"[0-9]*\s\d", title)  # e.g. "12345 2  "
    title = strip_regex(r"Excalibur", title)
    title = strip_regex(r"Neptune", title)
    title = strip_regex(r"report.\d", title)
    title = strip_regex(r"M.\d.\d.\d", title)
    title = strip_regex(r"M.\d.\d", title)
    title = strip_regex(r"M.\d", title)
    title = title.replace("Report", "")
    title = title.replace("Code structure and coordination", "")
    title = title.replace("Support and Coordination", "")

    lines = title.split("\n")
    lines = discard_non_title_lines(lines)
    if len(lines) > 1:
        title = lines[0] + lines[1]
    else:
        title = lines[0]

    return title.strip()


pdfpaths_to_nice_titles_dict = get_path_to_title_from_bibtex("../../tex/bib/exc.bib")


def descriptive_title_from_pdf(pdfpath, pdftxt):
    try:
        if (
            pdfpath in pdfpaths_to_nice_titles_dict
            and pdfpaths_to_nice_titles_dict[pdfpath] is not None
        ):
            title = pdfpaths_to_nice_titles_dict[pdfpath]
        else:
            title = get_raw_title_from_text("".join(pdftxt))
    except Exception as e:
        warnings.warn(
            "Could not extract report title from {}\nError:\n{}".format(pdfpath, e)
        )
        title = ""

    if len(title) <= 4:
        head, pdf = os.path.split(pdfpath)
        title = pdf[0:-4]
    return title


def clean_title(title):
    title += " "
    # get rid of common general words
    for i in [
        "a",
        "the",
        "of",
        "and",
        "for",
        "report",
        "study",
        "review",
        "describes",
        "milestone",
        "with",
        "in",
        "excalibur",
        "neptune",
        "on",
        "programme",
        "to",
        "overview",
        "findings",
        "devices",
        "models",
        "associated",
        "issues",
        "relevant",
        "which",
        "techniques",
        "software",
        "assessment",
        "literature",
    ]:
        title = re.sub(r"\b%s\b" % i, "", title, re.I)
    title = title.title()  # make first letter of all words uppercase
    title = re.sub(r"\W+", "", title)  # strip out any non alphanumeric values
    title = title.replace(" ", "")  #  remove all spaces
    title = title[0 : min(80, len(title))]  # limit length otherwise OS complains
    return title.strip()


numbered_to_descriptive_dirs = {}
numbered_to_descriptive_dirs["2047352_1"] = "UQ_UCL"
numbered_to_descriptive_dirs["2057701"] = "UQ_UCL-2"
numbered_to_descriptive_dirs["2047352_2"] = "Surrogates_UCL"
numbered_to_descriptive_dirs["2047353"] = "Precondition_STFC"
numbered_to_descriptive_dirs["2068625"] = "Precondition_STFC-2"
numbered_to_descriptive_dirs["2047355"] = "PIC_Warwick"
numbered_to_descriptive_dirs["2047356"] = "Fluids_York_etal"
numbered_to_descriptive_dirs["2047357"] = "MomentKinetics_Oxford"
numbered_to_descriptive_dirs["2070839"] = "MomentKinetics_Oxford-2"
numbered_to_descriptive_dirs["2047358"] = "Software_York_etal"
numbered_to_descriptive_dirs["2048465"] = "Meshing_Exeter"
numbered_to_descriptive_dirs["2053622"] = "Nektar++"
numbered_to_descriptive_dirs["2057699"] = "Platforms"
numbered_to_descriptive_dirs["2060042"] = "Nektar++"
numbered_to_descriptive_dirs["2060049"] = "Coupling_STFC"
numbered_to_descriptive_dirs["ukaea_reports"] = "UKAEA"
numbered_to_descriptive_dirs["equations"] = "Equations"
numbered_to_descriptive_dirs["2067270"] = "Hardware_York_etal"


list_of_directories_to_ignore = [
#    "2057701",
]  # the content in these directory shouldn't be displayed
rst_names = []


def copy_and_rename_file(pdfpath, pdftxt):
    head, pdf = os.path.split(pdfpath)

    fname = pdf.split(".")[0]
    # work out if we want to ignore this file
    if fname[0:2] == "AD":  # ignore these
        return None
    for skip in list_of_directories_to_ignore:  # a directory without good content
        if skip in head:
            return None
    # get the directory
    dirstub = pdfpath
    dirstub = dirstub[dirstub.find("pdfs") + 5 : :]
    dirstub = dirstub.replace("/", "_")
    # create a new file name, replacing numbers with words
    new_file_name = None
    for key in numbered_to_descriptive_dirs:
        if key in str(dirstub):
            new_file_name = dirstub.replace(key, numbered_to_descriptive_dirs[key])
            break
    if new_file_name is None:
        return None
    # add descriptive title-like suffix
    readable_suffix = "_" + clean_title(descriptive_title_from_pdf(pdfpath, pdftxt))
    new_file_name = new_file_name[:-4] + readable_suffix + ".pdf"
    # copy the file over to where sphinx expects it
    destpath = "../source/_static/" + new_file_name
    os.makedirs(os.path.dirname(destpath), exist_ok=True)
    shutil.copy(pdfpath, destpath)
    # record that the pdf has been renamed and therfore an .rst file
    # by that same name must be created to embed the pdf in
    stub = new_file_name[:-4]
    rst_names.append(stub + ".rst")

    return stub


def comma_separated_text_from_pdf(pdftxt):
    pdfstr = "".join(pdftxt)
    keywords = re.sub("\s+", ",", pdfstr.strip())
    return keywords


# iterate through all pdfs and create an rst that embeds the pdf for one we want to keep
for pdfpath in glob.glob("../../pdfs/**/*.pdf"):
    pdftxt = extract_text(pdfpath)
    stub = copy_and_rename_file(pdfpath, pdftxt)
    if stub is None:
        continue
    rstpath = "./" + stub + ".rst"
    os.makedirs(os.path.dirname(rstpath), exist_ok=True)
    f = open(rstpath, "w")
    f.write(stub + "\n")  # the title of the .rst document containing the pdf
    title_equals = "=" * len(stub)
    f.write(title_equals + "\n\n")
    # add a meta sectio with description and keywords so that Sphinx will
    # index the embedded pdfs
    f.write(".. meta::\n")
    f.write("   :description: technical note\n\n")
    keywords = comma_separated_text_from_pdf(pdftxt)
    # extract the text from the pdf, separated by commas, so that Sphinx will index the pdfs
    f.write("   :keywords: {0}\n\n".format(keywords))
    embed_string = (
        ":pdfembed:`src:_static/{0}, height:1600, width:1100, align:middle`\n\n"
    )
    assert os.path.isfile("_static/" + stub + ".pdf")
    f.write(embed_string.format(stub + ".pdf"))
    f.close()

rst_names.sort()

# create the file that we want to embed the pdfs in and start a toctree
f = open("embeddedpdfs.rst", "w")
f.write("Technical Reports\n")
f.write("=================\n\n")
f.write(".. toctree::\n")
# add a toctree entry for each category in numbered_to_descriptive_dirs
for dirname in sorted(set(numbered_to_descriptive_dirs.values())):
    f.write("    {0}\n".format(dirname))
f.close()
# now create an .rst file for each of the toctree entries in numbered_to_descriptive_dirs

for key in numbered_to_descriptive_dirs:
    dirname = numbered_to_descriptive_dirs[key]
    f = open("./" + dirname + ".rst", "w")
    title = dirname
    title = title.replace("_", " ")
    f.write(title + "\n")  # the title of the .rst document containing the pdf
    title_equals = "=" * len(dirname)
    f.write(title_equals + "\n\n")
    f.write(".. toctree::\n")
    for rst in rst_names:
        if dirname != rst[0 : len(dirname)]:
            continue
        f.write("    {0}\n".format(rst))
    f.close()

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxcontrib.pdfembed",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_css_files = ["custom.css"]
html_static_path = ["_static"]

html_theme_options = {
    "page_width": 1000,
}
