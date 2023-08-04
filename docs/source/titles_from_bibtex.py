"""
Installation
------------

For python prerequisites:

    pip install -r requirements.txt

tex to html conversion is tested with pandoc.


Introduction
------------

This script generates a dict of pdf paths to titles. The pdfs are located
in the pdf directory and their title is extracted from a bibtex file from
they are referenced.
 
External report bibtex keys are constructed as <directory>-<filename>, e.g. the
report in directory "2047357/TN-04.pdf" should match the bibtex entry with id
"2047357-TN-04". 

Internal report bibtex entries are found using the report/FMS number. For
example <title>-<number>.ext has report number <number>. E.g.
"CD-EXCALIBUR-FMS0055-M1.8.1.pdf" has report number "M1.8.1". Bibtex entries
for internal reports use the bibtex "NUMBER" field. E.g. a bibtex entry with
the number field "{CD/EXCALIBUR-FMS/0041-M3.2.2}" provides the bibtex entry for
report "M3.2.2".

This script should be run as part of ci.
"""


import os
import bibtexparser
import glob


def create_fms_bibtex(bib_database):
    """
    Creates a map from UKAEA FMS report numbers to bibtex entries. This is
    required as mapping from file name to bibtex id for the UKAEA reports is
    non-obvious.
    """

    new_map = {}
    for item in bib_database.entries:
        # the UKAEA bibtex entries need a NUMBER field
        if "number" in item.keys():
            bibtex_number = item["number"]

            # If there is no FMS number throw away
            if bibtex_number.find("EXCALIBUR-FMS") > 0:
                bibtex_number = bibtex_number.replace("{", "")
                bibtex_number = bibtex_number.replace("}", "")

                # assume the format of the NUMBER field is FMS-foo-A.1.2.3
                split_bibtex_number = bibtex_number.split("-")
                report_number = split_bibtex_number[-1]
                new_map[report_number] = item

    return new_map


def parse_po(report):
    """
    Return the PO for a report. Returns 123456_1 for an external grantee and
    ukaea_reports for UKAEA reports.
    """
    po = os.path.split(os.path.dirname(report))[-1]
    return po


def get_bibtex_key(report):
    """
    Construct bibtex id from filename. For external reports this key looks like
    "2047357-TN-04". For internal reports this key is the report number e.g.
    "M2.2.1" or "D3.1". Specific keys for specific files are specified in the
    config file.
    """

    po = parse_po(report)
    basename = os.path.basename(report)

    if po == "ukaea_reports":
        no_extension = os.path.splitext(basename)[0]
        report_number = no_extension.split("-")[-1]
        bid = report_number

    else:
        bid = po + "-" + ".".join(basename.split(".")[:-1])

    return bid


def find_bibtex_entry(bibtex, bibtex_fms, report):
    """
    Find the bibtex entry for the report.
    """
    bibtex_key = get_bibtex_key(report)

    if parse_po(report) != "ukaea_reports":
        # use the original bibtex database keyed by bibtex ids for external reports
        if bibtex_key in bibtex.entries_dict.keys():
            bibtex_entry = bibtex.entries_dict[bibtex_key]
        else:
            print(
                f'Warning: Could not find bibtex entry for {report} under key "{bibtex_key}"'
            )
            bibtex_entry = None
    else:
        # use the bibtex dict keyed by report numbers for internal reports
        if bibtex_key in bibtex_fms.keys():
            # report number as keys
            bibtex_entry = bibtex_fms[bibtex_key]
        elif bibtex_key in bibtex.entries_dict.keys():
            bibtex_entry = bibtex.entries_dict[bibtex_key]
        else:
            print(
                f'Warning: Could not find bibtex entry for {report} under key "{bibtex_key}"'
            )
            bibtex_entry = None

    return bibtex_entry


def get_bibtex_dicts(bibtex_path):
    """
    Get the two bibtex dicts required to map between bibtex key and bibtex
    entry.
    """
    bibtex = os.path.abspath(os.path.expanduser(bibtex_path))

    with open(bibtex) as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)

    # create the map from report numbers, e.g. M2.1.1a to bibtex entries
    bib_database_fms_keys = create_fms_bibtex(bib_database)

    return bib_database, bib_database_fms_keys


def get_path_to_title_from_bibtex(bibtex_path):
    # construct the bibtex dicts
    bib_database, bib_database_fms_keys = get_bibtex_dicts(bibtex_path)

    # find reports in the pdf dir
    reports = glob.glob("../../pdfs/**/*.pdf")

    # find reports and construct map from PO to reports
    path_to_title_dict = {}
    for fx in reports:
        # find the bibtex entry for this file
        bibtex_entry = find_bibtex_entry(bib_database, bib_database_fms_keys, fx)
        if (bibtex_entry is not None) and ("title" in bibtex_entry):
            path_to_title_dict[fx] = bibtex_entry["title"]

    return path_to_title_dict
