%define		_rc	rc7
Summary:	Unix port of eMule client
Summary(pl):	Uniksowy port klienta eMule
Name:		aMule
Version:	2.0.0
Release:	0.%{_rc}.1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/amule/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	b62106da3c38be29314a542aa3d20e95
# Source0-size:	2491155
Patch0:		%{name}-configure_in.patch
URL:		http://www.amule.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7.3
BuildRequires:	bison
#BuildRequires:	cryptopp-devel >= 5.1
BuildRequires:	curl-devel >= 7.9.7
BuildRequires:	expat-devel
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	wxGTK2-devel >= 2.4.0
BuildRequires:	wxBase-devel >= 2.4.0
Requires:	wget
Obsoletes:	xmule
Obsoletes:	lmule
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aMule is a Linux port of eMule client.

%description -l pl
aMule to linuksowy port klienta eMule.

%prep
%setup -q -n %{name}-%{version}%{_rc}
%patch0 -p1

%build
rm -r autom4te.cache
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-wx-config=/usr/bin/wxgtk2-2.4-config \
	--enable-optimise

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang amule

%clean
rm -rf $RPM_BUILD_ROOT

%files -f amule.lang
%defattr(644,root,root,755)
%doc docs/AUTHORS docs/README docs/Changelog docs/ED2K-Links.HOWTO docs/TODO docs/amulesig.txt
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
