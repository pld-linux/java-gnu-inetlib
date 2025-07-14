Summary:	GNU inetlib - library of clients for common Internet protocols
Summary(pl.UTF-8):	GNU inetlib - biblioteka klientów popularnych protokołów internetowych
Name:		java-gnu-inetlib
Version:	1.1.2
Release:	2
License:	GPL v2+
Group:		Libraries/Java
Source0:	http://ftp.gnu.org/gnu/classpath/inetlib-%{version}.tar.gz
# Source0-md5:	e28147996e70b63b6caa743319a4bf46
Patch0:		0001-make-logger-static-again.patch
Patch1:		javadoc.patch
URL:		http://www.gnu.org/software/classpath/inetlib.html
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU inetlib is a library of clients for common Internet protocols. The
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

The inetlib library is similar in intent to the Python Internet
protocols library - the API is as close as possible to the intent of
the underlying protocol design. This allows for very efficient coding
of user agents.

Additionally, inetlib includes URLStreamHandler implementations for
some of the protocols. These can be used to add support for the
corresponding URL scheme to the java.net.URL class.

%description -l pl.UTF-8
GNU inetlib to biblioteka klientów popularnych protokołów
internetowych. Aktualnie obsługiwane są następujące protokoły:

 - Hypertext Transfer Protocol (HTTP)
 - File Transfer Protocol (FTP)
 - Simple Mail Transfer Protocol (SMTP)
 - Internet Message Access Protocol (IMAP)
 - Post Office Protocol (POP)
 - Network News Transfer Protocol (NNTP)
 - Lightweight Directory Access Protocol (LDAP) (alpha)
 - Gopher
 - Finger

Biblioteka inetlib w zamierzeniu jest podobna do biblioteki protokołów
internetowych Pythona - API jest jak najbardziej zbliżone do projektu
samych protokołów. Pozwala to na bardzo wydajne kodowanie aplikacji
klienckich.

Ponadto inetlib zawiera implementacje URLStreamHandler dla niektórych
protokołów. Można ich używać w celu dodania obsługi odpowiednich
schematów URL-i do klasy java.net.URL.

%package javadoc
Summary:	API documentation for GNU inetlib
Summary(pl.UTF-8):	Dokumentacja API GNU inetlib
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	java-gnu-inetlib-doc

%description javadoc
API documentation for GNU inetlib.

%description javadoc -l pl.UTF-8
Dokumentacja API GNU inetlib.

%prep
%setup -q -n inetlib-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
unset CLASSPATH || :
export JAVA_HOME=%{java_home}
export JAVAC=%{_bindir}/javac
export JAVA=%{_bindir}/java
%configure

%{__make} -j1
%{__make} -j1 javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -R docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_javadir}/inetlib.jar

%files javadoc
%defattr(644,root,root,755)
%doc %{_javadocdir}/%{name}-%{version}
