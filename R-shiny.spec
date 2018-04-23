#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-shiny
Version  : 1.0.5
Release  : 24
URL      : https://cran.r-project.org/src/contrib/shiny_1.0.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/shiny_1.0.5.tar.gz
Summary  : Web Application Framework for R
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0 MIT
Requires: R-Cairo
Requires: R-ggplot2
Requires: R-htmltools
Requires: R-httpuv
Requires: R-jsonlite
Requires: R-sourcetools
Requires: R-xtable
BuildRequires : R-Cairo
BuildRequires : R-ggplot2
BuildRequires : R-htmltools
BuildRequires : R-httpuv
BuildRequires : R-jsonlite
BuildRequires : R-sourcetools
BuildRequires : R-xtable
BuildRequires : clr-R-helpers

%description
applications with R. Automatic "reactive" binding between inputs and
    outputs and extensive prebuilt widgets make it possible to build
    beautiful, responsive, and powerful applications with minimal effort.

%prep
%setup -q -c -n shiny

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517379873

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1517379873
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shiny
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library shiny
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library shiny|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/shiny/DESCRIPTION
/usr/lib64/R/library/shiny/INDEX
/usr/lib64/R/library/shiny/LICENSE
/usr/lib64/R/library/shiny/Meta/Rd.rds
/usr/lib64/R/library/shiny/Meta/features.rds
/usr/lib64/R/library/shiny/Meta/hsearch.rds
/usr/lib64/R/library/shiny/Meta/links.rds
/usr/lib64/R/library/shiny/Meta/nsInfo.rds
/usr/lib64/R/library/shiny/Meta/package.rds
/usr/lib64/R/library/shiny/NAMESPACE
/usr/lib64/R/library/shiny/NEWS.md
/usr/lib64/R/library/shiny/R/shiny
/usr/lib64/R/library/shiny/R/shiny.rdb
/usr/lib64/R/library/shiny/R/shiny.rdx
/usr/lib64/R/library/shiny/examples/01_hello/DESCRIPTION
/usr/lib64/R/library/shiny/examples/01_hello/Readme.md
/usr/lib64/R/library/shiny/examples/01_hello/app.R
/usr/lib64/R/library/shiny/examples/02_text/DESCRIPTION
/usr/lib64/R/library/shiny/examples/02_text/Readme.md
/usr/lib64/R/library/shiny/examples/02_text/app.R
/usr/lib64/R/library/shiny/examples/03_reactivity/DESCRIPTION
/usr/lib64/R/library/shiny/examples/03_reactivity/Readme.md
/usr/lib64/R/library/shiny/examples/03_reactivity/app.R
/usr/lib64/R/library/shiny/examples/04_mpg/DESCRIPTION
/usr/lib64/R/library/shiny/examples/04_mpg/Readme.md
/usr/lib64/R/library/shiny/examples/04_mpg/app.R
/usr/lib64/R/library/shiny/examples/05_sliders/DESCRIPTION
/usr/lib64/R/library/shiny/examples/05_sliders/Readme.md
/usr/lib64/R/library/shiny/examples/05_sliders/app.R
/usr/lib64/R/library/shiny/examples/06_tabsets/DESCRIPTION
/usr/lib64/R/library/shiny/examples/06_tabsets/Readme.md
/usr/lib64/R/library/shiny/examples/06_tabsets/app.R
/usr/lib64/R/library/shiny/examples/07_widgets/DESCRIPTION
/usr/lib64/R/library/shiny/examples/07_widgets/Readme.md
/usr/lib64/R/library/shiny/examples/07_widgets/app.R
/usr/lib64/R/library/shiny/examples/08_html/DESCRIPTION
/usr/lib64/R/library/shiny/examples/08_html/Readme.md
/usr/lib64/R/library/shiny/examples/08_html/app.R
/usr/lib64/R/library/shiny/examples/08_html/www/index.html
/usr/lib64/R/library/shiny/examples/09_upload/DESCRIPTION
/usr/lib64/R/library/shiny/examples/09_upload/Readme.md
/usr/lib64/R/library/shiny/examples/09_upload/app.R
/usr/lib64/R/library/shiny/examples/10_download/DESCRIPTION
/usr/lib64/R/library/shiny/examples/10_download/Readme.md
/usr/lib64/R/library/shiny/examples/10_download/app.R
/usr/lib64/R/library/shiny/examples/11_timer/DESCRIPTION
/usr/lib64/R/library/shiny/examples/11_timer/Readme.md
/usr/lib64/R/library/shiny/examples/11_timer/app.R
/usr/lib64/R/library/shiny/help/AnIndex
/usr/lib64/R/library/shiny/help/aliases.rds
/usr/lib64/R/library/shiny/help/paths.rds
/usr/lib64/R/library/shiny/help/shiny.rdb
/usr/lib64/R/library/shiny/help/shiny.rdx
/usr/lib64/R/library/shiny/html/00Index.html
/usr/lib64/R/library/shiny/html/R.css
/usr/lib64/R/library/shiny/staticdocs/index.r
/usr/lib64/R/library/shiny/template/default.html
/usr/lib64/R/library/shiny/www-dir/index.html
/usr/lib64/R/library/shiny/www/reactive-graph.html
/usr/lib64/R/library/shiny/www/shared/bootstrap/css/bootstrap-theme.css
/usr/lib64/R/library/shiny/www/shared/bootstrap/css/bootstrap-theme.css.map
/usr/lib64/R/library/shiny/www/shared/bootstrap/css/bootstrap-theme.min.css
/usr/lib64/R/library/shiny/www/shared/bootstrap/css/bootstrap-theme.min.css.map
/usr/lib64/R/library/shiny/www/shared/bootstrap/css/bootstrap.css
/usr/lib64/R/library/shiny/www/shared/bootstrap/css/bootstrap.css.map
/usr/lib64/R/library/shiny/www/shared/bootstrap/css/bootstrap.min.css
/usr/lib64/R/library/shiny/www/shared/bootstrap/css/bootstrap.min.css.map
/usr/lib64/R/library/shiny/www/shared/bootstrap/fonts/glyphicons-halflings-regular.eot
/usr/lib64/R/library/shiny/www/shared/bootstrap/fonts/glyphicons-halflings-regular.svg
/usr/lib64/R/library/shiny/www/shared/bootstrap/fonts/glyphicons-halflings-regular.ttf
/usr/lib64/R/library/shiny/www/shared/bootstrap/fonts/glyphicons-halflings-regular.woff
/usr/lib64/R/library/shiny/www/shared/bootstrap/fonts/glyphicons-halflings-regular.woff2
/usr/lib64/R/library/shiny/www/shared/bootstrap/js/bootstrap.js
/usr/lib64/R/library/shiny/www/shared/bootstrap/js/bootstrap.min.js
/usr/lib64/R/library/shiny/www/shared/bootstrap/js/npm.js
/usr/lib64/R/library/shiny/www/shared/bootstrap/shim/html5shiv.min.js
/usr/lib64/R/library/shiny/www/shared/bootstrap/shim/respond.min.js
/usr/lib64/R/library/shiny/www/shared/datatables/css/dataTables.bootstrap.css
/usr/lib64/R/library/shiny/www/shared/datatables/css/dataTables.extra.css
/usr/lib64/R/library/shiny/www/shared/datatables/images/sort_asc.png
/usr/lib64/R/library/shiny/www/shared/datatables/images/sort_asc_disabled.png
/usr/lib64/R/library/shiny/www/shared/datatables/images/sort_both.png
/usr/lib64/R/library/shiny/www/shared/datatables/images/sort_desc.png
/usr/lib64/R/library/shiny/www/shared/datatables/images/sort_desc_disabled.png
/usr/lib64/R/library/shiny/www/shared/datatables/js/dataTables.bootstrap.js
/usr/lib64/R/library/shiny/www/shared/datatables/js/jquery.dataTables.min.js
/usr/lib64/R/library/shiny/www/shared/datatables/upgrade1.10.txt
/usr/lib64/R/library/shiny/www/shared/datepicker/css/bootstrap-datepicker3.css
/usr/lib64/R/library/shiny/www/shared/datepicker/css/bootstrap-datepicker3.min.css
/usr/lib64/R/library/shiny/www/shared/datepicker/js/bootstrap-datepicker.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/bootstrap-datepicker.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ar.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.az.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.bg.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.bs.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ca.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.cs.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.cy.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.da.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.de.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.el.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.en-AU.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.en-GB.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.eo.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.es.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.et.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.eu.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.fa.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.fi.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.fo.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.fr-CH.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.fr.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.gl.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.he.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.hr.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.hu.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.hy.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.id.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.is.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.it-CH.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.it.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ja.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ka.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.kh.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.kk.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ko.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.kr.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.lt.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.lv.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.me.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.mk.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.mn.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ms.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.nb.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.nl-BE.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.nl.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.no.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.pl.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.pt-BR.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.pt.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ro.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.rs-latin.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.rs.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ru.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sk.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sl.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sq.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sr-latin.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sr.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sv.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sw.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.th.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.tr.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.uk.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.vi.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.zh-CN.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.zh-TW.min.js
/usr/lib64/R/library/shiny/www/shared/font-awesome/css/font-awesome.css
/usr/lib64/R/library/shiny/www/shared/font-awesome/css/font-awesome.min.css
/usr/lib64/R/library/shiny/www/shared/font-awesome/fonts/FontAwesome.otf
/usr/lib64/R/library/shiny/www/shared/font-awesome/fonts/fontawesome-webfont.eot
/usr/lib64/R/library/shiny/www/shared/font-awesome/fonts/fontawesome-webfont.svg
/usr/lib64/R/library/shiny/www/shared/font-awesome/fonts/fontawesome-webfont.ttf
/usr/lib64/R/library/shiny/www/shared/font-awesome/fonts/fontawesome-webfont.woff
/usr/lib64/R/library/shiny/www/shared/font-awesome/fonts/fontawesome-webfont.woff2
/usr/lib64/R/library/shiny/www/shared/highlight/LICENSE
/usr/lib64/R/library/shiny/www/shared/highlight/classref.txt
/usr/lib64/R/library/shiny/www/shared/highlight/highlight.pack.js
/usr/lib64/R/library/shiny/www/shared/highlight/rstudio.css
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/css/ion.rangeSlider.css
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/css/ion.rangeSlider.skinFlat.css
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/css/ion.rangeSlider.skinHTML5.css
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/css/ion.rangeSlider.skinModern.css
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/css/ion.rangeSlider.skinNice.css
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/css/ion.rangeSlider.skinShiny.css
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/css/ion.rangeSlider.skinSimple.css
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/css/normalize.css
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/img/sprite-skin-flat.png
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/img/sprite-skin-modern.png
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/img/sprite-skin-nice.png
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/img/sprite-skin-simple.png
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/js/ion.rangeSlider.js
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/js/ion.rangeSlider.min.js
/usr/lib64/R/library/shiny/www/shared/jquery-AUTHORS.txt
/usr/lib64/R/library/shiny/www/shared/jquery.js
/usr/lib64/R/library/shiny/www/shared/jquery.min.js
/usr/lib64/R/library/shiny/www/shared/jquery.min.map
/usr/lib64/R/library/shiny/www/shared/jqueryui/AUTHORS.txt
/usr/lib64/R/library/shiny/www/shared/jqueryui/LICENSE.txt
/usr/lib64/R/library/shiny/www/shared/jqueryui/README
/usr/lib64/R/library/shiny/www/shared/jqueryui/images/ui-icons_444444_256x240.png
/usr/lib64/R/library/shiny/www/shared/jqueryui/images/ui-icons_555555_256x240.png
/usr/lib64/R/library/shiny/www/shared/jqueryui/images/ui-icons_777620_256x240.png
/usr/lib64/R/library/shiny/www/shared/jqueryui/images/ui-icons_777777_256x240.png
/usr/lib64/R/library/shiny/www/shared/jqueryui/images/ui-icons_cc0000_256x240.png
/usr/lib64/R/library/shiny/www/shared/jqueryui/images/ui-icons_ffffff_256x240.png
/usr/lib64/R/library/shiny/www/shared/jqueryui/index.html
/usr/lib64/R/library/shiny/www/shared/jqueryui/jquery-ui.css
/usr/lib64/R/library/shiny/www/shared/jqueryui/jquery-ui.js
/usr/lib64/R/library/shiny/www/shared/jqueryui/jquery-ui.min.css
/usr/lib64/R/library/shiny/www/shared/jqueryui/jquery-ui.min.js
/usr/lib64/R/library/shiny/www/shared/jqueryui/jquery-ui.structure.css
/usr/lib64/R/library/shiny/www/shared/jqueryui/jquery-ui.structure.min.css
/usr/lib64/R/library/shiny/www/shared/jqueryui/jquery-ui.theme.css
/usr/lib64/R/library/shiny/www/shared/jqueryui/jquery-ui.theme.min.css
/usr/lib64/R/library/shiny/www/shared/json2-min.js
/usr/lib64/R/library/shiny/www/shared/selectize/css/selectize.bootstrap3.css
/usr/lib64/R/library/shiny/www/shared/selectize/js/es5-shim.min.js
/usr/lib64/R/library/shiny/www/shared/selectize/js/selectize.min.js
/usr/lib64/R/library/shiny/www/shared/shiny-showcase.css
/usr/lib64/R/library/shiny/www/shared/shiny-showcase.js
/usr/lib64/R/library/shiny/www/shared/shiny-testmode.js
/usr/lib64/R/library/shiny/www/shared/shiny.css
/usr/lib64/R/library/shiny/www/shared/shiny.js
/usr/lib64/R/library/shiny/www/shared/shiny.js.map
/usr/lib64/R/library/shiny/www/shared/shiny.min.js
/usr/lib64/R/library/shiny/www/shared/shiny.min.js.map
/usr/lib64/R/library/shiny/www/shared/showdown/compressed/showdown.js
/usr/lib64/R/library/shiny/www/shared/showdown/license.txt
/usr/lib64/R/library/shiny/www/shared/showdown/src/showdown.js
/usr/lib64/R/library/shiny/www/shared/strftime/strftime-min.js
