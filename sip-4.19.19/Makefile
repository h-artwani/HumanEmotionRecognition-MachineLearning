
all:
	@(cd sipgen; $(MAKE))
	@(cd siplib; $(MAKE))

install:
	@(cd sipgen; $(MAKE) install)
	@(cd siplib; $(MAKE) install)
	@test -d $(DESTDIR)/Library/Python/2.7/site-packages || mkdir -p $(DESTDIR)/Library/Python/2.7/site-packages
	cp -f sipconfig.py $(DESTDIR)/Library/Python/2.7/site-packages/sipconfig.py
	cp -f /Users/harshartwani/Downloads/Projects/EmotionMLNew/sip-4.19.19/sipdistutils.py $(DESTDIR)/Library/Python/2.7/site-packages/sipdistutils.py
	/usr/bin/python /Users/harshartwani/Downloads/Projects/EmotionMLNew/sip-4.19.19/mk_distinfo.py "$(DESTDIR)" /Library/Python/2.7/site-packages/sip-4.19.19.dist-info installed.txt

clean:
	@(cd sipgen; $(MAKE) clean)
	@(cd siplib; $(MAKE) clean)
