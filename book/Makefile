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


