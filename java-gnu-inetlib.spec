#
Summary:	GNU inetlib - library of clients for common internet protocols. 
Name:		java-gnu-inetlib
Version:	1.1.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/gnu/classpath/inetlib-%{version}.tar.gz
# Source0-md5:	aaa24be4bc8d172ac675be8bdfa636ee
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.gnu.org/software/classpath/inetlib.html
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	jdk
Requires:	jre
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU inetlib is a library of clients for common internet protocols. The
following protocols are currently supported:

    - Hypertext Transfer Protocol (HTTP)
    - File Transfer Protocol (FTP)
    - Simple Mail Transfer Protocol (SMTP)
    - Internet Message Access Protocol (IMAP)
    - Post Office Protocol (POP)
    - Network News Transfer Protocol (NNTP)
    - Lightweight Directory Access Protocol (LDAP) (alpha)
    - Gopher
    - Finger

The inetlib library is similar in intent to the Python internet
protocols library - the API is as close as possible to the intent of
the underlying protocol design. This allows for very efficient coding
of user agents.

Additionally, inetlib includes URLStreamHandler implementations for
some of the protocols. These can be used to add support for the
corresponding URL scheme to the java.net.URL class.

%package doc
Summary:	API documentation for GNU inetlib
Summary(pl):	Dokumentacja API GNU inetlib
Group:		Documentation

%description doc
API documentation for GNU inetlib.

%description doc -l pl
Dokumentacja API GNU inetlib.

%prep
%setup -q -n inetlib-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
# Sun java requires . in CLASSPATH for configure test
export CLASSPATH=.
export JAVAC=%{_bindir}/javac
export JAVA=%{_bindir}/java
%configure

%{__make}
%{__make} javadoc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs/*
