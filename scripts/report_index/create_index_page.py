"""
Installation
------------

For python prerequisites:

    pip install -r requirements.txt

tex to html conversion is tested with pandoc.


Introduction
------------

This script generates the LaTeX source for an index page of NEPTUNE reports.
External reports are found by matching the pattern "*/TN*.pdf" internal reports
are found by matching the pattern "ukaea_reports/*.*". The output tex sections
are constructed on a per Purchase Order (PO) number using titles in the config
file. 

External report bibtex keys are constructed as <directory>-<filename>, e.g. the
report in directory "2047357/TN-04.pdf" should match the bibtex entry with id
"2047357-TN-04". 

Internal report bibtex entries are found using the report/FMS number. For
example <title>-<number>.ext has report number <number>. E.g.
"CD-EXCALIBUR-FMS0055-M1.8.1.pdf" has report number "M1.8.1". Bibtex entries
for internal reports use the bibtex "NUMBER" field. E.g. a bibtex entry with
the number field "{CD/EXCALIBUR-FMS/0041-M3.2.2}" provides the bibtex entry for
report "M3.2.2".

This script should be ran with the "reports" directory as the working
directory. The script is launched with a single argument which is the path to
the config file:

    python3 create_index_page.py index_config.yaml

which creates (using the default config) "report_index.tex". The LaTeX source
can be converted to html using:

    pandoc report_index.tex -o report_index.html
"""


import sys
import os
import bibtexparser
import glob
import yaml


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
                bibkey = extract_ukaea_bibkey(bibtex_number)
                if bibkey is None:
                    print(
                        f'WARNING: Failed to compute bibtex key for number "{bibtex_number}'
                    )
                else:
                    new_map[bibkey] = item
    return new_map


def extract_ukaea_bibkey(s):
    """
    Extracts FMS number and report number from filenames / bibtex NUMBER fields for internal UKAEA reports.
    Might be simpler to do this with regex...
    """

    name_components = s.split("-")
    report_number = name_components[-1]
    FMS_number = None
    for comp in name_components:
        if comp.startswith("FMS"):
            FMS_number = comp.replace("/", "")
            break
    if FMS_number is None:
        return None
    else:
        return (FMS_number, report_number)


def find_reports():
    """
    Return list of all report PDFs to be indexed.
    """
    external_reports = glob.glob("*/TN*.pdf")
    ukaea_reports = glob.glob("ukaea_reports/*.*")

    return external_reports + ukaea_reports


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
        bid = extract_ukaea_bibkey(os.path.splitext(basename)[0])
    else:

        bid = po + "-" + ".".join(basename.split(".")[:-1])

    return bid


def find_bibtex_entry(config, bibtex, bibtex_fms, report):
    """
    Find the bibtex entry for the report.
    """

    basename = os.path.basename(report)

    # If a specific bibtex entry was specified in the config for this file then
    # use the key in the config to get the bibtex entry
    if basename in config["bibtex_ids"].keys():
        bibtex_key = config["bibtex_ids"][basename]
    else:
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
            # config file key case
            bibtex_entry = bibtex.entries_dict[bibtex_key]
        else:
            print(
                f'Warning: Could not find bibtex entry for {report} under key "{bibtex_key}"'
            )
            bibtex_entry = None

    return bibtex_entry


def get_name_from_po(config, po):
    """
    Map the PO to an institution/group
    """
    if po in config["po_name"].keys():
        name = config["po_name"][po]
    else:
        print(f"Warning: No name found for {po}.")
        name = po

    return name


def escape_underscores(string):
    """
    Escape underscores for LaTeX output.
    """
    return string.replace("_", r"\_")


class Report:
    """
    Simple class to hold the information and formatting for each report.
    """

    def __init__(self, filename, bibtex_entry):
        self.filename = filename
        self.bibtex_entry = bibtex_entry

    def po(self):
        return parse_po(self.filename)

    def __str__(self):
        return self.filename

    def title(self):
        if self.bibtex_entry is None:
            return self.po() + "-" + self.basename()
        else:
            return self.bibtex_entry["title"]

    def basename(self):
        return os.path.basename(self.filename)


def get_bibtex_dicts(config):
    """
    Get the two bibtex dicts required to map between bibtex key and bibtex
    entry.
    """
    bibtex = os.path.abspath(os.path.expanduser(config["bibtex"]))

    with open(bibtex) as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)

    # create the map from report numbers, e.g. M2.1.1a to bibtex entries
    bib_database_fms_keys = create_fms_bibtex(bib_database)

    return bib_database, bib_database_fms_keys


def get_config():
    """
    Get the config as a dict.
    """
    # first and only argument is a path to the config file
    config_file = os.path.abspath(os.path.expanduser(sys.argv[1]))

    with open(config_file, "r") as fh:
        yaml_dict = yaml.safe_load(fh)
    config = yaml_dict["index_config"]

    return config


if __name__ == "__main__":

    # first and only command line arg should be the yaml config
    config = get_config()

    # construct the bibtex dicts
    bib_database, bib_database_fms_keys = get_bibtex_dicts(config)

    # find reports matching */TN*.pdf and ukaea_reports/*.*
    reports = find_reports()

    # find reports and construct map from PO to reports
    PO_report = {}
    for fx in reports:

        # find the bibtex entry for this file
        bibtex_entry = find_bibtex_entry(
            config, bib_database, bib_database_fms_keys, fx
        )

        # create a new report object
        new_report = Report(fx, bibtex_entry)

        po = new_report.po()
        if not po in PO_report.keys():
            PO_report[po] = []

        PO_report[po].append(new_report)

    # sort the reports from each PO by filename
    for po in PO_report.keys():
        PO_report[po].sort(key=lambda x: x.filename)

    # start constructing the latex source for the page
    page = """
\\begin{document}
    """

    # create the section and table for each PO
    for fx in PO_report.keys():
        name = get_name_from_po(config, fx)
        po_reports = PO_report[fx]

        rtable = r"""
        \begin{center}
        \begin{tabular}{l}
        """
        for rx in po_reports:
            url = config["base_url"] + rx.filename
            title = escape_underscores(rx.title())
            rtable += f" \href{{ {url} }}{{ {title} }} \\\\ \n"

        rtable += r"""\end{tabular}
\end{center}"""

        b = f"\n \section{{ {name} }} \n{rtable}"

        page += b

    page += "\n\\end{document}"

    with open(config["output_file"], "w") as fh:
        fh.write(page)
