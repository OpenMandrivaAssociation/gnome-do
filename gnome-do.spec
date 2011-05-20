Name:			gnome-do
Version:		0.8.4
Release:		%mkrel 1
Summary:		Quick launch and search

License:		GPLv3+
Group:			Graphical desktop/GNOME
URL:			http://do.davebsd.com/
Source0:		http://launchpad.net/do/0.8/%version/+download/%name-%version.tar.gz
Patch0:			gnome-do-0.8.4-mono-2.8.patch
Patch1:			gnome-do-0.8.3.1-gdk.patch
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root
Suggests:		gnome-do-plugins >= 0.8
BuildRequires:		mono-addins-devel
BuildRequires:		desktop-file-utils
BuildRequires:		ndesk-dbus-glib-devel
BuildRequires:		gtk-sharp2-devel
BuildRequires:		gnome-sharp2-devel, gnome-desktop-sharp-devel
BuildRequires:		gnome-keyring-sharp
BuildRequires:		notify-sharp-devel
BuildRequires:		gettext
BuildRequires:		intltool
BuildRequires:		gtk2-devel

%description
Allows you to quickly search for many objects present in your
GNOME desktop environment and perform commonly used commands 
on those objects

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x --disable-schemas-install
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYRIGHT
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_libdir}/gnome-do
%{_iconsdir}/hicolor/*/*/*
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/applications/gnome-do.desktop
%{_libdir}/pkgconfig/*
