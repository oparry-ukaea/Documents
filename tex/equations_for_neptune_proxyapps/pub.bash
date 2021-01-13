sed -e '/<==omit$/s/^/%/' <skel.tex > rp1omit.tex
pdflatex rp1omit;bibtex rp1omit; pdflatex rp1omit
pdflatex cover.tex
pdfunite cover.pdf rp1omit.pdf rp1pub.pdf
rm -f rp1omit.tex
