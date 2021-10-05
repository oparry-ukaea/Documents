all:
	pdflatex rpc.tex
	bibtex rpc
	pdflatex rpc.tex
	pdflatex rpc.tex

clean: clean_aux
	rm -f *.pdf
	
clean_aux:
	rm -f *.aux *.blg *.bbl *.log *.out
