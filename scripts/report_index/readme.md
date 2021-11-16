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

External report bibtex keys are constructed as "<directory>-<filename>", e.g. the
report in directory "2047357/TN-04.pdf" should match the bibtex entry with id
"2047357-TN-04". 

Internal report bibtex entries are found using the report/FMS number. For
example "<title>-<number>.ext" has report number "<number>". E.g.
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
