sed -e '/<==omit$/s/^/%/' <rp1.tex > rp1omit.tex
pdflatex rp1omit;bibtex rp1omit; pdflatex rp1omit; pdflatex rp1omit
pdflatex cover.tex
pdfunite cover.pdf rp1omit.pdf rp1pub.pdf
rm -f rp1omit.tex rp1omit.aux rp1omit.bbl rp1omit.blg rp1omit.log rp1omit.out rp1omit.pdf
mv rp1pub.pdf CD-EXCALIBUR-FMS0021-1.27-M1.2.1.pdf
