Summary:	gentoo - a GTK+ file manager for Linux
Summary(pl.UTF-8):	gentoo - oparty na GTK+ zarządca plików pod Linuksa
Name:		gentoo
Version:	0.11.57
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gentoo/%{name}-%{version}.tar.gz
# Source0-md5:	00ec2afd0254aa815f87980a27dcf242
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-locale_names.patch
URL:		http://www.obsession.se/gentoo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
Requires:	file
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11

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

%description -l pl.UTF-8
gentoo jest zarządcą plików dla Linuksa napisanym 'od zera' w czystym
C. Używa zestawu narzędzi GTK+ do zaspokojenia wszystkich potrzeb
związanych z interfejsem. gentoo zapewnia 100%%-ową konfigurowalność
graficznego interfejsu; nie ma potrzeby ręcznego modyfikowania plików
konfiguracyjnych i ponownego uruchamiania programu. gentoo dostarcza
identyfikację typów różnych plików (używając rozszerzenia, wyrażeń
regularnych i/lub polecenia 'file') oraz potrafi wyświetlać pliki
różnego typu w różnych kolorach i z różnymi ikonami. gentoo zapożycza
trochę ze swojego wyglądu od klasycznego zarządcy plików Amigi --
"Directory OPUS"(TM) (napisanego przez Jonathana Pottera).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/ru{_RU.utf8,}.po
rm -f po/ru_RU.*
mv -f po/ja{_JP.UTF-8,}.po

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install docs/gentoo.1x $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS CREDITS ChangeLog NEWS README* TODO docs
%config %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/gentoo.desktop
%{_pixmapsdir}/*
