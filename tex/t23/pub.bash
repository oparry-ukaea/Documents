sed -e '/<==omit$/s/^/%/' <rp$1.tex > rp$1omit.tex
pdflatex rp$1omit;bibtex rp$1omit; pdflatex rp$1omit
pdflatex cover$1.tex
pdfunite cover$1.pdf rp$1omit.pdf rp$1pub.pdf
rm -f rp$1omit.tex
