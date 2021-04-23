#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pcaPP
Version  : 1.9.74
Release  : 28
URL      : https://cran.r-project.org/src/contrib/pcaPP_1.9-74.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pcaPP_1.9-74.tar.gz
Summary  : Robust PCA by Projection Pursuit
Group    : Development/Tools
License  : GPL-3.0
Requires: R-pcaPP-lib = %{version}-%{release}
Requires: R-mvtnorm
BuildRequires : R-mvtnorm
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-pcaPP package.
Group: Libraries

%description lib
lib components for the R-pcaPP package.


%prep
%setup -q -c -n pcaPP
cd %{_builddir}/pcaPP

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619188617

%install
export SOURCE_DATE_EPOCH=1619188617
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pcaPP
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pcaPP
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pcaPP
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pcaPP || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pcaPP/DESCRIPTION
/usr/lib64/R/library/pcaPP/INDEX
/usr/lib64/R/library/pcaPP/Meta/Rd.rds
/usr/lib64/R/library/pcaPP/Meta/features.rds
/usr/lib64/R/library/pcaPP/Meta/hsearch.rds
/usr/lib64/R/library/pcaPP/Meta/links.rds
/usr/lib64/R/library/pcaPP/Meta/nsInfo.rds
/usr/lib64/R/library/pcaPP/Meta/package.rds
/usr/lib64/R/library/pcaPP/Meta/vignette.rds
/usr/lib64/R/library/pcaPP/NAMESPACE
/usr/lib64/R/library/pcaPP/R/pcaPP
/usr/lib64/R/library/pcaPP/R/pcaPP.rdb
/usr/lib64/R/library/pcaPP/R/pcaPP.rdx
/usr/lib64/R/library/pcaPP/doc/index.html
/usr/lib64/R/library/pcaPP/doc/matlab.R
/usr/lib64/R/library/pcaPP/doc/matlab.pdf
/usr/lib64/R/library/pcaPP/doc/matlab.rnw
/usr/lib64/R/library/pcaPP/help/AnIndex
/usr/lib64/R/library/pcaPP/help/aliases.rds
/usr/lib64/R/library/pcaPP/help/paths.rds
/usr/lib64/R/library/pcaPP/help/pcaPP.rdb
/usr/lib64/R/library/pcaPP/help/pcaPP.rdx
/usr/lib64/R/library/pcaPP/html/00Index.html
/usr/lib64/R/library/pcaPP/html/R.css
/usr/lib64/R/library/pcaPP/tests/tpcapp.R
/usr/lib64/R/library/pcaPP/tests/tpcapp.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/pcaPP/libs/pcaPP.so
/usr/lib64/R/library/pcaPP/libs/pcaPP.so.avx2
/usr/lib64/R/library/pcaPP/libs/pcaPP.so.avx512
