Summary:	gentoo is a Gtk+ file manager for Linux.
Summary(pl):	gentoo jest opartym na Gtk+ zarz±dc± plików pod Linuxa.
Name:		gentoo
Version:	0.11.6
Release:	1
Copyright:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
URL:		http://www.obsession.se/gentoo
Source0:	ftp://ftp.obsession.se/gentoo/%{name}-%{version}.tar.gz
Source1:	gentoo.wmconfig
Patch0:		gentoo-makefile.patch
Patch1:		gentoo-config.patch
BuildPrereq:	gtk+-devel >= 1.2.0
BuildPrereq:	glib-devel >= 1.2.0
BuildPrereq:	XFree86-devel
Requires:	file
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix		/usr/X11R6

%description
gentoo is a file manager for Linux written from scratch in pure C. It
uses the GTK+ toolkit for all of its interface needs. gentoo provides
100%% GUI configurability; no need to edit config files by hand and re-
start the program. gentoo supports identifying the type of various
files (using extension, regular expressions, and/or the 'file' command),
and can display files of different types with different colors and icons.
	gentoo borrows some of its look and feel from the classic Amiga
file manager "Directory OPUS"(TM) (written by Jonathan Potter).

%description -l pl
gentoo jest zarz±dc± plików dla Linuxa napisanym 'od zera' w czystym C.
U¿ywa zestawu narzêdzi GTK+ do zaspokojenia wszystkich potrzeb zwi±zanych
z interfejsem. gentoo zapewnia 100%-ow± konfigurowalno¶æ graficznego 
interfejsu; nie ma potrzeby rêcznego edytowania plików konfiguracyjnch
i ponownego uruchamiania programu. gentoo dostarcza identyfikacjê typów
ró¿nych plików (u¿ywaj±c rozszerzenia, wyra¿eñ regularnych i/lub polecenia
'file') oraz potrafi wy¶wietlaæ pliki ró¿nego typu w ró¿nych kolorach
i z ró¿nymi ikonami. gentoo zapo¿ycza trochê ze swojego wygl±du od 
klasycznego zarz±dcy plików Amigi -- "Directory OPUS"(TM) (napisanego
przez Jonathana Pottera).

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build

CFLAGS="$RPM_OPT_FLAGS" \
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_datadir}/%{name}/icons,/etc/X11/wmconfig}

install -s %{name} $RPM_BUILD_ROOT%{_bindir}
install gentoorc-example $RPM_BUILD_ROOT%{_datadir}/%{name}/gentoorc
install icons/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/icons
install docs/%{name}.1x $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	BUGS FIXES-0.11 FIXES-0.9 README README.gtkrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,FIXES-0.11,FIXES-0.9,README,README.gtkrc}.gz
%doc docs %{name}gtkrc-example %{name}rc-example

%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*

/etc/X11/wmconfig/%{name}

%changelog
- added gentoo.desktop instead of wmconfig file,
- minor fixes.
- updated to 0.11.6,
- added using more rpm macros,
- package is now FHS 2.0 compliant.

* Mon Apr 26 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.11.5-2]
- fixed some options in gentoo config file (gentoo-config.patch).

* Mon Apr 26 1999 Piotr Czerwiñski <pius@pld.org.pl>
- updated to 0.11.5,
- added pl translation,
- changed install prefix to /usr/X11R6,
- changed gentoo's files path to /usr/X11R6/share/gentoo 
  (new gentoo-makefile.patch),
- fixed passing $RPM_OPT_FLAGS during compile,
- modified %install and %files section,
- added gzipping documentation and man pages,
- added full %defattr and %attr description,
- added some BuildPrereqs and Requires,
- added wmconfig file,
- recompiled on rpm 3,
- minor changes.

* Tue Apr  6 1999 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.4-1]
- 0.11.4
- Statusbar now shows the amount of free space for the filesystem
  the current pane's directory is in. Note that the call that makes
  this possible (statfs(2) on Linux, statvfs(2) on e.g. Solaris and
  Irix) seems to be somewhat unstandardized. There might be trouble.
- Fixed a problem with nesting modal dialogs. Noticable when e.g.
  Rename caused an overwrite confirmation to occur.
- Fixed a related dialog problem; now, if you close the Rename
  dialog with the Overwrite confirm window still open, nothing evil
  will happen.
- Did numerous clean-ups in the main "gentoo.h" header file, moving
  many type definitions into separate C files, thus reducing coupling.
- Removed a useless dialog (the "child_dialog" module).
- Discovered what I suppose is a compiler bug in gcc 2.8.1; when
  compiling gentoo with optimization level 2 (-O2), a supposedly
  harmless statement in the dialog module will cause a segfault...
- When you write a path, the keyboard events no longer trigger
  commands. This is better. Reported by J. Hanson <johan@tiq.com>.
- Added a freeze/thaw pair to the textviewer used for command output
  capturing, resulting in way better performance and no flickering.
- Removed the (nonfunctional) "Print" button from the text viewer,
  slightly changing the button layout in the process.
- Slowed down the animation of the busy indicator (used by the
  Information and GetSize commands) a bit. It made me nervous. :)
- The hex text viewing (used by ViewHex & ViewTextOrHex) code was
  *very* memory-inefficient (it always loaded the entire file, but
  only looked at 16 bytes at a time). Now it reads 16 bytes at a
  time, thus using constant buffer space (and running slower).
- ViewTextOrHex now correctly reports the error if it fails to
  open a file for reading. Er, ViewText & ViewHex don't (yet).
- Designed and implemented a system for keeping track of each
  command's individual configuration options. The options them-
  selves have been around for quite a while, but they haven't been
  configurable (without editing source, that is). Now they appear
  on the "Command Options" page in the configuration window, and
  are loaded and saved along with the rest of the config. Neat.
    Please read "docs/scratch/command_options.txt" to learn what
  different options do.

* Tue Mar 30 1999 Ryan Weaver <ryanw@infohwy.com>
  [gentoo-0.11.3-1]
- Damn! That command sequence selection dialog just didn't work.
  Typical, since I spent about 3 hrs banging on it before releasing
  0.11.2. Perhaps I should have tested it. Reported by J. Minnberg.
- Eh, seems I broke the main "gentoo.h" include file, too. Fixed.
- Fixed a minor error (typo) in the cmdgrab module.

- package is FHS 2.0 compliant,
- spec file rewritten for PLD use,
- based on spec written by Ryan Weaver <ryanw@infohwy.com>.
