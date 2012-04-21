Summary:	A curses-based tty Jabber, IRC, AIM and Zephyr client
Name:		barnowl
Version:	1.8.1
Release:	0.1
# Perl libraries LGPL v2.1
License:	BSD, LGPL v2.1
Group:		Applications/Communications
Source0:	http://barnowl.mit.edu/dist/%{name}-%{version}-src.tgz
# Source0-md5:	ef8d2a71fc8d63ec2f9f4512a22c516b
URL:		http://barnowl.mit.edu/
BuildRequires:	autoconf
BuildRequires:	glib2-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-AnyEvent
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Glib-devel
BuildRequires:	perl-devel
BuildRequires:	pkg-config
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BarnOwl is a fully integrated tty‐based instant messaging client.
Currently it supports AOL Instant Messenger, MIT Zephyr, Jabber, IRC,
and Twitter. It is curses‐based, allows for emacs‐style editing of
outgoing messages, and uses Perl as an extension and configuration
language. BarnOwl will also run happily without a configuration file.

%prep
%setup -q -n %{name}-%{version}-src

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README ChangeLog doc/*.txt examples
%attr(755,root,root) %{_bindir}/barnowl
%attr(755,root,root) %{_bindir}/zcrypt
%{_datadir}/%{name}
%{_mandir}/man1/barnowl.1*
