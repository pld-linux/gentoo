Summary:	gentoo is a Gtk+ file manager for Linux.
Summary(pl):	gentoo jest opartym na Gtk+ zarz�dc� plik�w pod Linuxa.
Name:		gentoo
Version:	0.11.14
Release:	1
License:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narz�dzia
Source0:	ftp://ftp.obsession.se/gentoo/%{name}-%{version}.tar.gz
Source1:	gentoo.desktop
Patch0:		gentoo-makefile.patch
URL:		http://www.obsession.se/gentoo/
BuildRequires:	gtk+-devel >= 1.2.0
Requires:	file
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
gentoo is a file manager for Linux written from scratch in pure C. It
uses the GTK+ toolkit for all of its interface needs. gentoo provides
100%% GUI configurability; no need to edit config files by hand and
re- start the program. gentoo supports identifying the type of various
files (using extension, regular expressions, and/or the 'file'
command), and can display files of different types with different
colors and icons. gentoo borrows some of its look and feel from the
classic Amiga file manager "Directory OPUS"(TM) (written by Jonathan
Potter).

%description -l pl
gentoo jest zarz�dc� plik�w dla Linuxa napisanym 'od zera' w czystym
C. U�ywa zestawu narz�dzi GTK+ do zaspokojenia wszystkich potrzeb
zwi�zanych z interfejsem. gentoo zapewnia 100%-ow� konfigurowalno��
graficznego interfejsu; nie ma potrzeby r�cznego edytowania plik�w
konfiguracyjnch i ponownego uruchamiania programu. gentoo dostarcza
identyfikacj� typ�w r�nych plik�w (u�ywaj�c rozszerzenia, wyra�e�
regularnych i/lub polecenia 'file') oraz potrafi wy�wietla� pliki
r�nego typu w r�nych kolorach i z r�nymi ikonami. gentoo zapo�ycza
troch� ze swojego wygl�du od klasycznego zarz�dcy plik�w Amigi --
"Directory OPUS"(TM) (napisanego przez Jonathana Pottera).

%prep
%setup -q
%patch0 -p1

%build
make DEBUG="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_datadir}/%{name}/icons,%{_applnkdir}/Utilities}

install -s %{name} 	 $RPM_BUILD_ROOT%{_bindir}
install gentoorc-example $RPM_BUILD_ROOT%{_datadir}/%{name}/gentoorc
install icons/*		 $RPM_BUILD_ROOT%{_datadir}/%{name}/icons
install docs/%{name}.1x  $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1}	 $RPM_BUILD_ROOT%{_applnkdir}/Utilities

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	BUGS FIXES-0.11 FIXES-0.9 README README.gtkrc CONFIG-CHANGES \
	CREDITS docs/scratch/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,FIXES-0.11,FIXES-0.9,README,README.gtkrc,CONFIG-CHANGES,CREDITS}.gz
%doc docs/{*.{html,css},images,config,scratch} 
%doc gentoogtkrc-example gentoorc-example

%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*

%{_applnkdir}/Utilities/gentoo.desktop
