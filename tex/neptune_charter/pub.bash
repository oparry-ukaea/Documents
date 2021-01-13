sed -e '/<==omit$/s/^/%/' <rp.tex > rpomit.tex
pdflatex rpomit;bibtex rpomit; pdflatex rpomit
pdflatex cover.tex
pdfunite cover.pdf rpomit.pdf rppub.pdf
#rm -f rpomit.tex
