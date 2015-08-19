pdf: courseml.tex
	pdflatex courseml.tex
	bibtex courseml
	makeindex courseml
	pdflatex courseml.tex
	pdflatex courseml.tex
	pdflatex courseml.tex
	./book2toc.pl > toc.html
#	scp toc.html context:~/public_html/ciml/private/contents-autogen.html
	rm -rf foo
	mkdir foo
	pdfsam-console -f courseml.pdf -o foo/ -s BLEVEL -bl 1 split

clean:
	rm -f *.aux
	rm -rf foo
	rm -rf courseml.bbl
	rm -rf courseml.blg
	rm -rf courseml.idx
	rm -rf courseml.ilg
	rm -rf courseml.ind
	rm -rf courseml.log
	rm -rf courseml.out
	rm -rf courseml.pdf
	rm -rf courseml.toc
