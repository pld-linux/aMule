Summary:	Unix port of eMule client
Summary(pl):	Uniksowy port klienta eMule
Name:		aMule
Version:	1.0.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/amule/%{name}-%{version}.tar.bz2
# Source0-md5:	92c197614ff08ee554e23efe8865e474
URL:		http://amule.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7.3
BuildRequires:	bison
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	expat-devel
BuildRequires:	wxGTK2-devel >= 2.4.0
BuildRequires:	gtk2+-devel >= 2.2.0
BuildRequires:	libstdc++-devel
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aMule is a Linux port of eMule client.

%description -l pl
aMule to linuksowy port klienta eMule.

%prep
%setup  -q

%build

%configure \
	--with-wx-config=/usr/bin/wxgtk-2.4-config 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc AUTHORS Changelog ED2K-Links.HOWTO README TODO
%attr(755,root,root) %{_bindir}/*
