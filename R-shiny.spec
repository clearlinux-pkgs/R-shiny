#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: 0c573b6
#
Name     : R-shiny
Version  : 1.9.1
Release  : 96
URL      : https://cran.r-project.org/src/contrib/shiny_1.9.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/shiny_1.9.1.tar.gz
Summary  : Web Application Framework for R
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-3.0 MIT
Requires: R-shiny-license = %{version}-%{release}
Requires: R-R6
Requires: R-bslib
Requires: R-cachem
Requires: R-commonmark
Requires: R-crayon
Requires: R-fastmap
Requires: R-fontawesome
Requires: R-glue
Requires: R-htmltools
Requires: R-httpuv
Requires: R-jsonlite
Requires: R-later
Requires: R-lifecycle
Requires: R-mime
Requires: R-promises
Requires: R-rlang
Requires: R-sourcetools
Requires: R-withr
Requires: R-xtable
BuildRequires : R-R6
BuildRequires : R-bslib
BuildRequires : R-cachem
BuildRequires : R-commonmark
BuildRequires : R-crayon
BuildRequires : R-fastmap
BuildRequires : R-fontawesome
BuildRequires : R-future
BuildRequires : R-glue
BuildRequires : R-htmltools
BuildRequires : R-httpuv
BuildRequires : R-jsonlite
BuildRequires : R-later
BuildRequires : R-lifecycle
BuildRequires : R-mime
BuildRequires : R-promises
BuildRequires : R-rlang
BuildRequires : R-sourcetools
BuildRequires : R-withr
BuildRequires : R-xtable
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
applications with R. Automatic "reactive" binding between inputs and
    outputs and extensive prebuilt widgets make it possible to build
    beautiful, responsive, and powerful applications with minimal effort.

%package license
Summary: license components for the R-shiny package.
Group: Default

%description license
license components for the R-shiny package.


%prep
%setup -q -n shiny
pushd ..
cp -a shiny buildavx2
popd
pushd ..
cp -a shiny buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1722529358

%install
export SOURCE_DATE_EPOCH=1722529358
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-shiny
cp %{_builddir}/shiny/LICENSE %{buildroot}/usr/share/package-licenses/R-shiny/762741cd0200d40737e4ec06835160ac88a0b862 || :
cp %{_builddir}/shiny/inst/www/shared/busy-indicators/spinners/LICENSE %{buildroot}/usr/share/package-licenses/R-shiny/4ecc89edada4b04044ac3afce5a26bfb3b2818e8 || :
cp %{_builddir}/shiny/inst/www/shared/highlight/LICENSE %{buildroot}/usr/share/package-licenses/R-shiny/cd25196630fe891662ad77810f0f6dee5bc85ddc || :
cp %{_builddir}/shiny/inst/www/shared/jqueryui/LICENSE.txt %{buildroot}/usr/share/package-licenses/R-shiny/15df6665dfd90f5cd8fdfde4c0c43051fbb76dae || :
cp %{_builddir}/shiny/inst/www/shared/showdown/license.txt %{buildroot}/usr/share/package-licenses/R-shiny/da02c977aba236f45145329e97f95f4bdc3387b8 || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/shiny/app_template/R/example-module.R
/usr/lib64/R/library/shiny/app_template/R/example.R
/usr/lib64/R/library/shiny/app_template/app.R
/usr/lib64/R/library/shiny/app_template/tests/testthat.R
/usr/lib64/R/library/shiny/app_template/tests/testthat/setup-shinytest2.R
/usr/lib64/R/library/shiny/app_template/tests/testthat/test-examplemodule.R
/usr/lib64/R/library/shiny/app_template/tests/testthat/test-server.R
/usr/lib64/R/library/shiny/app_template/tests/testthat/test-shinytest2.R
/usr/lib64/R/library/shiny/app_template/tests/testthat/test-sort.R
/usr/lib64/R/library/shiny/diagrams/outputProgressStateMachine.drawio
/usr/lib64/R/library/shiny/diagrams/outputProgressStateMachine.svg
/usr/lib64/R/library/shiny/examples-shiny/01_hello/DESCRIPTION
/usr/lib64/R/library/shiny/examples-shiny/01_hello/Readme.md
/usr/lib64/R/library/shiny/examples-shiny/01_hello/app.R
/usr/lib64/R/library/shiny/examples-shiny/02_text/DESCRIPTION
/usr/lib64/R/library/shiny/examples-shiny/02_text/Readme.md
/usr/lib64/R/library/shiny/examples-shiny/02_text/app.R
/usr/lib64/R/library/shiny/examples-shiny/03_reactivity/DESCRIPTION
/usr/lib64/R/library/shiny/examples-shiny/03_reactivity/Readme.md
/usr/lib64/R/library/shiny/examples-shiny/03_reactivity/app.R
/usr/lib64/R/library/shiny/examples-shiny/04_mpg/DESCRIPTION
/usr/lib64/R/library/shiny/examples-shiny/04_mpg/Readme.md
/usr/lib64/R/library/shiny/examples-shiny/04_mpg/app.R
/usr/lib64/R/library/shiny/examples-shiny/05_sliders/DESCRIPTION
/usr/lib64/R/library/shiny/examples-shiny/05_sliders/Readme.md
/usr/lib64/R/library/shiny/examples-shiny/05_sliders/app.R
/usr/lib64/R/library/shiny/examples-shiny/06_tabsets/DESCRIPTION
/usr/lib64/R/library/shiny/examples-shiny/06_tabsets/Readme.md
/usr/lib64/R/library/shiny/examples-shiny/06_tabsets/app.R
/usr/lib64/R/library/shiny/examples-shiny/07_widgets/DESCRIPTION
/usr/lib64/R/library/shiny/examples-shiny/07_widgets/Readme.md
/usr/lib64/R/library/shiny/examples-shiny/07_widgets/app.R
/usr/lib64/R/library/shiny/examples-shiny/08_html/DESCRIPTION
/usr/lib64/R/library/shiny/examples-shiny/08_html/Readme.md
/usr/lib64/R/library/shiny/examples-shiny/08_html/app.R
/usr/lib64/R/library/shiny/examples-shiny/08_html/www/index.html
/usr/lib64/R/library/shiny/examples-shiny/09_upload/DESCRIPTION
/usr/lib64/R/library/shiny/examples-shiny/09_upload/Readme.md
/usr/lib64/R/library/shiny/examples-shiny/09_upload/app.R
/usr/lib64/R/library/shiny/examples-shiny/10_download/DESCRIPTION
/usr/lib64/R/library/shiny/examples-shiny/10_download/Readme.md
/usr/lib64/R/library/shiny/examples-shiny/10_download/app.R
/usr/lib64/R/library/shiny/examples-shiny/11_timer/DESCRIPTION
/usr/lib64/R/library/shiny/examples-shiny/11_timer/Readme.md
/usr/lib64/R/library/shiny/examples-shiny/11_timer/app.R
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
/usr/lib64/R/library/shiny/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/shiny/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/shiny/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/shiny/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/shiny/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/shiny/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/shiny/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/shiny/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/shiny/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/shiny/help/figures/logo.png
/usr/lib64/R/library/shiny/help/paths.rds
/usr/lib64/R/library/shiny/help/shiny.rdb
/usr/lib64/R/library/shiny/help/shiny.rdx
/usr/lib64/R/library/shiny/html/00Index.html
/usr/lib64/R/library/shiny/html/R.css
/usr/lib64/R/library/shiny/template/default.html
/usr/lib64/R/library/shiny/template/error.html
/usr/lib64/R/library/shiny/tests/test-encoding/01-symbols/app.R
/usr/lib64/R/library/shiny/tests/test-encoding/02-backslash/server.R
/usr/lib64/R/library/shiny/tests/test-encoding/02-backslash/ui.R
/usr/lib64/R/library/shiny/tests/test-encoding/test-all.R
/usr/lib64/R/library/shiny/tests/test-helpers/app1-standard/R/helperCap.R
/usr/lib64/R/library/shiny/tests/test-helpers/app1-standard/R/helperLower.r
/usr/lib64/R/library/shiny/tests/test-helpers/app1-standard/global.R
/usr/lib64/R/library/shiny/tests/test-helpers/app1-standard/server.R
/usr/lib64/R/library/shiny/tests/test-helpers/app1-standard/tests/runner1.R
/usr/lib64/R/library/shiny/tests/test-helpers/app1-standard/tests/runner2.R
/usr/lib64/R/library/shiny/tests/test-helpers/app1-standard/ui.R
/usr/lib64/R/library/shiny/tests/test-helpers/app2-nested/R/helper.R
/usr/lib64/R/library/shiny/tests/test-helpers/app2-nested/R/nested/helper.R
/usr/lib64/R/library/shiny/tests/test-helpers/app2-nested/app.R
/usr/lib64/R/library/shiny/tests/test-helpers/app2-nested/global.R
/usr/lib64/R/library/shiny/tests/test-helpers/app3-badglobal/R/helper.R
/usr/lib64/R/library/shiny/tests/test-helpers/app3-badglobal/global.R
/usr/lib64/R/library/shiny/tests/test-helpers/app4-both/app.R
/usr/lib64/R/library/shiny/tests/test-helpers/app4-both/r/lower.R
/usr/lib64/R/library/shiny/tests/test-helpers/app5-bad-supporting/R/helper.R
/usr/lib64/R/library/shiny/tests/test-helpers/app5-bad-supporting/global.R
/usr/lib64/R/library/shiny/tests/test-helpers/app6-disabled/R/_DISABLE_autoload.r
/usr/lib64/R/library/shiny/tests/test-helpers/app6-disabled/R/helperCap.R
/usr/lib64/R/library/shiny/tests/test-helpers/app6-disabled/R/helperLower.r
/usr/lib64/R/library/shiny/tests/test-helpers/app6-disabled/global.R
/usr/lib64/R/library/shiny/tests/test-helpers/app6-disabled/server.R
/usr/lib64/R/library/shiny/tests/test-helpers/app6-disabled/ui.R
/usr/lib64/R/library/shiny/tests/test-helpers/app6-empty-tests/tests/file.txt
/usr/lib64/R/library/shiny/tests/test-helpers/app7-port/app.R
/usr/lib64/R/library/shiny/tests/test-helpers/app7-port/option-broken.R
/usr/lib64/R/library/shiny/tests/test-helpers/app7-port/option.R
/usr/lib64/R/library/shiny/tests/test-helpers/app7-port/wrapped.R
/usr/lib64/R/library/shiny/tests/test-helpers/app7-port/wrapped2.R
/usr/lib64/R/library/shiny/tests/test-modules/06_tabsets/app.R
/usr/lib64/R/library/shiny/tests/test-modules/107_scatterplot/R/linked-scatterplot-module.R
/usr/lib64/R/library/shiny/tests/test-modules/107_scatterplot/R/scatterplot.R
/usr/lib64/R/library/shiny/tests/test-modules/107_scatterplot/app.R
/usr/lib64/R/library/shiny/tests/test-modules/107_scatterplot/tests/testthat.R
/usr/lib64/R/library/shiny/tests/test-modules/107_scatterplot/tests/testthat/test-linked-scatterplot-module.R
/usr/lib64/R/library/shiny/tests/test-modules/107_scatterplot/tests/testthat/test-plot.R
/usr/lib64/R/library/shiny/tests/test-modules/107_scatterplot/tests/testthat/test-server.R
/usr/lib64/R/library/shiny/tests/test-modules/12_counter/R/my-module.R
/usr/lib64/R/library/shiny/tests/test-modules/12_counter/R/utils.R
/usr/lib64/R/library/shiny/tests/test-modules/12_counter/app.R
/usr/lib64/R/library/shiny/tests/test-modules/12_counter/tests/testthat.R
/usr/lib64/R/library/shiny/tests/test-modules/12_counter/tests/testthat/test-mymodule.R
/usr/lib64/R/library/shiny/tests/test-modules/12_counter/tests/testthat/test-server.R
/usr/lib64/R/library/shiny/tests/test-modules/12_counter/tests/testthat/test-utils.R
/usr/lib64/R/library/shiny/tests/test-modules/server_r/server.R
/usr/lib64/R/library/shiny/tests/test-modules/server_r/ui.R
/usr/lib64/R/library/shiny/tests/testthat.R
/usr/lib64/R/library/shiny/tests/testthat/_snaps/busy-indication.md
/usr/lib64/R/library/shiny/tests/testthat/_snaps/tabPanel.md
/usr/lib64/R/library/shiny/tests/testthat/helper.R
/usr/lib64/R/library/shiny/tests/testthat/print-reactiveValues.txt
/usr/lib64/R/library/shiny/tests/testthat/test-actionButton.R
/usr/lib64/R/library/shiny/tests/testthat/test-app.R
/usr/lib64/R/library/shiny/tests/testthat/test-bind-cache.R
/usr/lib64/R/library/shiny/tests/testthat/test-bind-event.R
/usr/lib64/R/library/shiny/tests/testthat/test-bookmarking.R
/usr/lib64/R/library/shiny/tests/testthat/test-bootstrap.r
/usr/lib64/R/library/shiny/tests/testthat/test-built-files.R
/usr/lib64/R/library/shiny/tests/testthat/test-busy-indication.R
/usr/lib64/R/library/shiny/tests/testthat/test-devmode.R
/usr/lib64/R/library/shiny/tests/testthat/test-diagnostics.R
/usr/lib64/R/library/shiny/tests/testthat/test-gc.r
/usr/lib64/R/library/shiny/tests/testthat/test-get-extension.R
/usr/lib64/R/library/shiny/tests/testthat/test-hybrid-chain.R
/usr/lib64/R/library/shiny/tests/testthat/test-inline-markdown.R
/usr/lib64/R/library/shiny/tests/testthat/test-input-handler.R
/usr/lib64/R/library/shiny/tests/testthat/test-input-select.R
/usr/lib64/R/library/shiny/tests/testthat/test-input-slider.R
/usr/lib64/R/library/shiny/tests/testthat/test-mock-session.R
/usr/lib64/R/library/shiny/tests/testthat/test-modules.R
/usr/lib64/R/library/shiny/tests/testthat/test-options.R
/usr/lib64/R/library/shiny/tests/testthat/test-pkgdown.R
/usr/lib64/R/library/shiny/tests/testthat/test-plot-coordmap.R
/usr/lib64/R/library/shiny/tests/testthat/test-plot-png.R
/usr/lib64/R/library/shiny/tests/testthat/test-reactives.R
/usr/lib64/R/library/shiny/tests/testthat/test-reactivity.r
/usr/lib64/R/library/shiny/tests/testthat/test-reactlog.R
/usr/lib64/R/library/shiny/tests/testthat/test-render-functions.R
/usr/lib64/R/library/shiny/tests/testthat/test-shinywrappers.R
/usr/lib64/R/library/shiny/tests/testthat/test-stacks-deep.R
/usr/lib64/R/library/shiny/tests/testthat/test-stacks-pruning.R
/usr/lib64/R/library/shiny/tests/testthat/test-stacks.R
/usr/lib64/R/library/shiny/tests/testthat/test-stop-app.R
/usr/lib64/R/library/shiny/tests/testthat/test-tabPanel.R
/usr/lib64/R/library/shiny/tests/testthat/test-test-runTests.R
/usr/lib64/R/library/shiny/tests/testthat/test-test-server-app.R
/usr/lib64/R/library/shiny/tests/testthat/test-test-server-nesting.R
/usr/lib64/R/library/shiny/tests/testthat/test-test-server-scope.R
/usr/lib64/R/library/shiny/tests/testthat/test-test-server.R
/usr/lib64/R/library/shiny/tests/testthat/test-test-shinyAppTemplate.R
/usr/lib64/R/library/shiny/tests/testthat/test-text.R
/usr/lib64/R/library/shiny/tests/testthat/test-timer.R
/usr/lib64/R/library/shiny/tests/testthat/test-update-input.R
/usr/lib64/R/library/shiny/tests/testthat/test-url.R
/usr/lib64/R/library/shiny/tests/testthat/test-utils.R
/usr/lib64/R/library/shiny/www-dir/index.html
/usr/lib64/R/library/shiny/www/shared/bootstrap/accessibility/css/bootstrap-accessibility.min.css
/usr/lib64/R/library/shiny/www/shared/bootstrap/accessibility/js/bootstrap-accessibility.min.js
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
/usr/lib64/R/library/shiny/www/shared/busy-indicators/busy-indicators.css
/usr/lib64/R/library/shiny/www/shared/busy-indicators/spinners/LICENSE
/usr/lib64/R/library/shiny/www/shared/busy-indicators/spinners/bars.svg
/usr/lib64/R/library/shiny/www/shared/busy-indicators/spinners/bars2.svg
/usr/lib64/R/library/shiny/www/shared/busy-indicators/spinners/bars3.svg
/usr/lib64/R/library/shiny/www/shared/busy-indicators/spinners/dots.svg
/usr/lib64/R/library/shiny/www/shared/busy-indicators/spinners/dots2.svg
/usr/lib64/R/library/shiny/www/shared/busy-indicators/spinners/dots3.svg
/usr/lib64/R/library/shiny/www/shared/busy-indicators/spinners/pulse.svg
/usr/lib64/R/library/shiny/www/shared/busy-indicators/spinners/pulse2.svg
/usr/lib64/R/library/shiny/www/shared/busy-indicators/spinners/pulse3.svg
/usr/lib64/R/library/shiny/www/shared/busy-indicators/spinners/ring.svg
/usr/lib64/R/library/shiny/www/shared/busy-indicators/spinners/ring2.svg
/usr/lib64/R/library/shiny/www/shared/busy-indicators/spinners/ring3.svg
/usr/lib64/R/library/shiny/www/shared/datatables/css/dataTables.bootstrap.css
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
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker-en-CA.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ar-tn.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ar.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.az.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.bg.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.bm.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.bn.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.br.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.bs.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ca.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.cs.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.cy.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.da.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.de.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.el.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.en-AU.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.en-CA.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.en-GB.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.en-IE.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.en-NZ.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.en-ZA.min.js
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
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.hi.min.js
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
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.km.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ko.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.kr.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.lt.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.lv.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.me.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.mk.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.mn.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ms.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.nl-BE.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.nl.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.no.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.oc.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.pl.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.pt-BR.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.pt.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ro.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.rs-latin.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.rs.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ru.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.si.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sk.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sl.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sq.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sr-latin.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sr.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sv.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.sw.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.ta.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.tg.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.th.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.tk.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.tr.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.uk.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.uz-cyrl.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.uz-latn.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.vi.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.zh-CN.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/js/locales/bootstrap-datepicker.zh-TW.min.js
/usr/lib64/R/library/shiny/www/shared/datepicker/scss/build3.scss
/usr/lib64/R/library/shiny/www/shared/datepicker/scss/datepicker3.scss
/usr/lib64/R/library/shiny/www/shared/highlight/LICENSE
/usr/lib64/R/library/shiny/www/shared/highlight/classref.txt
/usr/lib64/R/library/shiny/www/shared/highlight/highlight.pack.js
/usr/lib64/R/library/shiny/www/shared/highlight/rstudio.css
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/css/ion.rangeSlider.css
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/js/ion.rangeSlider.js
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/js/ion.rangeSlider.min.js
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/scss/_base.scss
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/scss/_mixins.scss
/usr/lib64/R/library/shiny/www/shared/ionrangeslider/scss/shiny.scss
/usr/lib64/R/library/shiny/www/shared/jquery-AUTHORS.txt
/usr/lib64/R/library/shiny/www/shared/jquery.js
/usr/lib64/R/library/shiny/www/shared/jquery.min.js
/usr/lib64/R/library/shiny/www/shared/jquery.min.js.map
/usr/lib64/R/library/shiny/www/shared/jqueryui/AUTHORS.txt
/usr/lib64/R/library/shiny/www/shared/jqueryui/LICENSE.txt
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
/usr/lib64/R/library/shiny/www/shared/legacy/jquery-AUTHORS.txt
/usr/lib64/R/library/shiny/www/shared/legacy/jquery.js
/usr/lib64/R/library/shiny/www/shared/legacy/jquery.min.js
/usr/lib64/R/library/shiny/www/shared/legacy/jquery.min.map
/usr/lib64/R/library/shiny/www/shared/selectize/accessibility/js/selectize-plugin-a11y.js
/usr/lib64/R/library/shiny/www/shared/selectize/accessibility/js/selectize-plugin-a11y.min.js
/usr/lib64/R/library/shiny/www/shared/selectize/css/selectize.bootstrap3.css
/usr/lib64/R/library/shiny/www/shared/selectize/js/selectize.js
/usr/lib64/R/library/shiny/www/shared/selectize/js/selectize.min.js
/usr/lib64/R/library/shiny/www/shared/selectize/scss/plugins/auto_position.scss
/usr/lib64/R/library/shiny/www/shared/selectize/scss/plugins/clear_button.scss
/usr/lib64/R/library/shiny/www/shared/selectize/scss/plugins/drag_drop.scss
/usr/lib64/R/library/shiny/www/shared/selectize/scss/plugins/dropdown_header.scss
/usr/lib64/R/library/shiny/www/shared/selectize/scss/plugins/optgroup_columns.scss
/usr/lib64/R/library/shiny/www/shared/selectize/scss/plugins/remove_button.scss
/usr/lib64/R/library/shiny/www/shared/selectize/scss/selectize.bootstrap3.scss
/usr/lib64/R/library/shiny/www/shared/selectize/scss/selectize.bootstrap4.scss
/usr/lib64/R/library/shiny/www/shared/selectize/scss/selectize.bootstrap5.scss
/usr/lib64/R/library/shiny/www/shared/selectize/scss/selectize.default.scss
/usr/lib64/R/library/shiny/www/shared/selectize/scss/selectize.scss
/usr/lib64/R/library/shiny/www/shared/shiny-autoreload.js
/usr/lib64/R/library/shiny/www/shared/shiny-autoreload.js.map
/usr/lib64/R/library/shiny/www/shared/shiny-showcase.css
/usr/lib64/R/library/shiny/www/shared/shiny-showcase.js
/usr/lib64/R/library/shiny/www/shared/shiny-showcase.js.map
/usr/lib64/R/library/shiny/www/shared/shiny-testmode.js
/usr/lib64/R/library/shiny/www/shared/shiny-testmode.js.map
/usr/lib64/R/library/shiny/www/shared/shiny.js
/usr/lib64/R/library/shiny/www/shared/shiny.js.map
/usr/lib64/R/library/shiny/www/shared/shiny.min.css
/usr/lib64/R/library/shiny/www/shared/shiny.min.js
/usr/lib64/R/library/shiny/www/shared/shiny.min.js.map
/usr/lib64/R/library/shiny/www/shared/shiny_scss/shiny.bootstrap3.scss
/usr/lib64/R/library/shiny/www/shared/shiny_scss/shiny.bootstrap4.scss
/usr/lib64/R/library/shiny/www/shared/shiny_scss/shiny.bootstrap5.scss
/usr/lib64/R/library/shiny/www/shared/shiny_scss/shiny.scss
/usr/lib64/R/library/shiny/www/shared/showdown/compressed/showdown.js
/usr/lib64/R/library/shiny/www/shared/showdown/license.txt
/usr/lib64/R/library/shiny/www/shared/showdown/src/showdown.js
/usr/lib64/R/library/shiny/www/shared/strftime/strftime-min.js

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-shiny/15df6665dfd90f5cd8fdfde4c0c43051fbb76dae
/usr/share/package-licenses/R-shiny/4ecc89edada4b04044ac3afce5a26bfb3b2818e8
/usr/share/package-licenses/R-shiny/762741cd0200d40737e4ec06835160ac88a0b862
/usr/share/package-licenses/R-shiny/cd25196630fe891662ad77810f0f6dee5bc85ddc
/usr/share/package-licenses/R-shiny/da02c977aba236f45145329e97f95f4bdc3387b8
