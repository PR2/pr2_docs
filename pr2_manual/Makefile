#LATEX = latex
LATEX = pdflatex
BIBTEX = bibtex
DVIPS = dvips
PS2PDF = ps2pdf

BASE_NAME = main
CHEAT_NAME = ROScheatsheet

OTHER_FILES = 1_introduction.tex 2_safety.tex 3_pr2_hardware.tex 4_pr2_computers.tex 5_pr2_setup.tex 6_running_pr2.tex 7_pr2_development.tex 8_pr2_maintenance.tex 
PDF_FILES = $(subst dia,pdf,$(shell ls images/*.dia))

all: $(PDF_FILES) $(BASE_NAME).pdf $(CHEAT_NAME).pdf

$(BASE_NAME).pdf: $(BASE_NAME).tex $(OTHER_FILES) $(PNG_FILES)
	$(LATEX) $< && $(LATEX) $< && $(LATEX) $<

$(BASE_NAME).dvi: $(BASE_NAME).tex 
	$(LATEX) $< && $(LATEX) $< && $(LATEX) $<

$(BASE_NAME).ps: $(BASE_NAME).dvi
	$(DVIPS) -P pdf -f -t a4 $(BASE_NAME).dvi > $@

$(CHEAT_NAME).pdf: $(CHEAT_NAME).tex $(PNG_FILES)
	$(LATEX) $< && $(LATEX) $< && $(LATEX) $<

$(CHEAT_NAME).dvi: $(CHEAT_NAME).tex 
	$(LATEX) $< && $(LATEX) $< && $(LATEX) $<

$(CHEAT_NAME).ps: $(CHEAT_NAME).dvi
	$(DVIPS) -P pdf -f -t a4 $(CHEAT_NAME).dvi > $@

display: $(BASE_NAME).pdf
	evince $(BASE_NAME).pdf &

%.eps: %.dia
	cd `dirname $<` && dia `basename $<` -t eps

%.pdf: %.eps
	epstopdf $<

clean:
	rm -f $(BASE_NAME).ps $(BASE_NAME).dvi $(BASE_NAME).log \
	      $(BASE_NAME).aux $(BASE_NAME).blg $(BASE_NAME).toc \
              missfont.log $(BASE_NAME).bbl $(BASE_NAME).pdf\
        $(CHEAT_NAME).ps $(CHEAT_NAME).dvi $(CHEAT_NAME).log \
	      $(CHEAT_NAME).aux $(CHEAT_NAME).blg $(CHEAT_NAME).toc \
              missfont.log $(CHEAT_NAME).bbl $(CHEAT_NAME).pdf 


#manual.pdf: main.tex
#	pdflatex main.tex

#clean:
#	- rm *.pdf *.aux *.toc *.log
