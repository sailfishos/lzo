Name:       lzo
Summary:    Data compression library with very fast (de)compression
Version:    2.10
Release:    1
License:    GPLv2+
URL:        http://www.oberhumer.com/opensource/lzo/
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(zlib)


%description
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory. In addition there are slower
compression levels achieving a quite competitive compression ratio
while still decompressing at this very high speed.


%package devel
Summary:    Development files for the lzo library
Requires:   %{name} = %{version}-%{release}
Requires:   zlib-devel

%description devel
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
This package contains development files needed for lzo.


%prep
%autosetup -p1 -n %{name}-%{version}

%build

%configure --disable-static \
    --disable-dependency-tracking \
    --enable-shared

%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/liblzo2.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/LZOAPI.TXT doc/LZO.FAQ doc/LZO.TXT AUTHORS THANKS NEWS
%{_includedir}/lzo
%{_libdir}/pkgconfig/lzo2.pc
%{_libdir}/lib*lzo*.so
%{_datadir}/doc/lzo/*

