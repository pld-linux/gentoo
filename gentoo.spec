%define	name	gentoo
%define	version	0.11.4
%define	release	1
%define	serial	2

Summary:	gentoo is a Gtk+ file manager for Linux.
Name:		%{name}
Version:	%{version}
Release:	%{release}
Serial:		%{serial}
Copyright:	GPL
Group:		X11/Utilities
URL:		http://www.obsession.se/gentoo
Vendor:		Emil Brink <emil@obsession.se>
Source:		ftp://ftp.obsession.se/gentoo/%{name}-%{version}.tar.gz
Patch:		%{name}-makefile.patch
Distribution:	Freshmeat RPMs
Packager:	Ryan Weaver <ryanw@infohwy.com>
Requires:	gtk+ >= 1.2.0
BuildRoot:	/tmp/%{name}-%{version}

%description
gentoo is a file manager for Linux written from scratch in pure C. It
uses the GTK+ toolkit for all of its interface needs. gentoo provides
100%% GUI configurability; no need to edit config files by hand and re-
start the program. gentoo supports identifying the type of various
files (using extension, regular expressions, and/or the 'file' command),
and can display files of different types with different colors and icons.
	gentoo borrows some of its look and feel from the classic Amiga
file manager "Directory OPUS"(TM) (written by Jonathan Potter).

%prep
%setup -q
%patch -p1

%build
make

%install
if [ -e $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi

install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/lib/gentoo/icons
install -d $RPM_BUILD_ROOT/usr/man/man1

install -s -m 755 gentoo	$RPM_BUILD_ROOT/usr/bin
install -m 644 gentoorc-example $RPM_BUILD_ROOT/usr/lib/gentoo
install -m 644 gentoorc-example $RPM_BUILD_ROOT/usr/lib/gentoo/gentoorc
install -m 644 icons/*		$RPM_BUILD_ROOT/usr/lib/gentoo/icons
install -m 644 docs/gentoo.1x	$RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs BUGS COPYING FIXES-0.11 FIXES-0.9 INSTALL README
%doc README.gtkrc gentoogtkrc-example gentoorc-example
/usr/bin/gentoo
/usr/lib/gentoo
/usr/man/man1/gentoo.1x

%changelog
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
