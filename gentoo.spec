Summary:	gentoo is a Gtk+ file manager for Linux
Summary(pl):	gentoo jest opartym na Gtk+ zarz±dc± plików pod Linuksa
Name:		gentoo
Version:	0.11.51
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gentoo/%{name}-%{version}.tar.gz
# Source0-md5:	e9bcc95dd5c16a607a202cb7b5d2d73a
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

%description -l pl
gentoo jest zarz±dc± plików dla Linuksa napisanym 'od zera' w czystym
C. U¿ywa zestawu narzêdzi GTK+ do zaspokojenia wszystkich potrzeb
zwi±zanych z interfejsem. gentoo zapewnia 100%-ow± konfigurowalno¶æ
graficznego interfejsu; nie ma potrzeby rêcznego edytowania plików
konfiguracyjnch i ponownego uruchamiania programu. gentoo dostarcza
identyfikacjê typów ró¿nych plików (u¿ywaj±c rozszerzenia, wyra¿eñ
regularnych i/lub polecenia 'file') oraz potrafi wy¶wietlaæ pliki
ró¿nego typu w ró¿nych kolorach i z ró¿nymi ikonami. gentoo zapo¿ycza
trochê ze swojego wygl±du od klasycznego zarz±dcy plików Amigi --
"Directory OPUS"(TM) (napisanego przez Jonathana Pottera).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/ru{_RU.utf8,}.po
rm -f po/ru_RU.*

%build
rm -f missing
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
