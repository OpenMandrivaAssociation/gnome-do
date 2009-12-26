Name:			gnome-do
Version:		0.8.3.1
Release:		%mkrel 1
Summary:		Quick launch and search

License:		GPLv3+
Group:			Graphical desktop/GNOME
URL:			http://do.davebsd.com/
Source0:		http://launchpad.net/do/0.8/%version/+download/%name-%version.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root
Suggests:		gnome-do-plugins >= 0.8
BuildRequires:		mono-devel mono-addins
BuildRequires:		desktop-file-utils
BuildRequires:		ndesk-dbus
BuildRequires:		ndesk-dbus-glib
BuildRequires:		gtk-sharp2-devel
BuildRequires:		gnome-sharp2-devel, gnome-desktop-sharp-devel
BuildRequires:		gnome-keyring-sharp
BuildRequires:		notify-sharp
BuildRequires:		gettext
BuildRequires:		perl-XML-Parser
BuildRequires:		intltool
BuildRequires:		gtk2-devel

%description
Allows you to quickly search for many objects present in your
GNOME desktop environment and perform commonly used commands 
on those objects

%prep
%setup -q 

%build
%configure2_5x
%make 


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

desktop-file-install --vendor gnome \
	--dir $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart	\
	--add-only-show-in=GNOME				\
	$RPM_BUILD_ROOT%{_datadir}/applications/gnome-do.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYRIGHT
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/gnome-do
%{_datadir}/gnome-do
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/gnome-do.desktop
%config(noreplace) %{_sysconfdir}/xdg/autostart/*.desktop
%{_libdir}/pkgconfig/*
