%define		pearname	Security
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Security Component
Name:		php-symfony2-Security
Version:	2.4.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{pearname}/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	60f339fe437c326e516e82fd2da50880
URL:		http://symfony.com/doc/2.4/book/security.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(hash)
Requires:	php(json)
Requires:	php(pcre)
Requires:	php(session)
Requires:	php(spl)
Requires:	php-pear >= 4:1.3.10
Requires:	php-symfony2-EventDispatcher >= 2.1
Requires:	php-symfony2-HttpFoundation >= 2.1
Requires:	php-symfony2-HttpKernel >= 2.1
Suggests:	php-symfony2-ClassLoader
Suggests:	php-symfony2-Finder
Suggests:	php-symfony2-Form
Suggests:	php-symfony2-Routing
Suggests:	php-symfony2-Validator
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an infrastructure for sophisticated authorization systems.

%prep
%setup -q -n %{pearname}-%{version}

# Security_Csrf merged to this package...
rm Csrf/.gitignore
rm Csrf/composer.json
rm Csrf/phpunit.xml.dist
mv Csrf/LICENSE LICENSE_Csrf
mv Csrf/README.md README_Csrf.md

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Tests
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Csrf/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%doc README_Csrf.md LICENSE_Csrf
%dir %{php_pear_dir}/Symfony/Component/Security
%{php_pear_dir}/Symfony/Component/Security/*.php
%{php_pear_dir}/Symfony/Component/Security/Acl
%{php_pear_dir}/Symfony/Component/Security/Core
%{php_pear_dir}/Symfony/Component/Security/Http

%dir %{php_pear_dir}/Symfony/Component/Security/Csrf
%{php_pear_dir}/Symfony/Component/Security/Csrf/*.php
%{php_pear_dir}/Symfony/Component/Security/Csrf/Exception
%{php_pear_dir}/Symfony/Component/Security/Csrf/TokenGenerator
%{php_pear_dir}/Symfony/Component/Security/Csrf/TokenStorage

%dir %{php_pear_dir}/Symfony/Component/Security/Resources
%dir %{php_pear_dir}/Symfony/Component/Security/Resources/translations
%lang(ar) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.ar.xlf
%lang(bg) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.bg.xlf
%lang(ca) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.ca.xlf
%lang(cs) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.cs.xlf
%lang(da) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.da.xlf
%lang(de) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.de.xlf
%lang(el) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.el.xlf
%lang(en) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.en.xlf
%lang(es) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.es.xlf
%lang(fa) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.fa.xlf
%lang(fr) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.fr.xlf
%lang(gl) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.gl.xlf
%lang(hr) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.hr.xlf
%lang(hu) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.hu.xlf
%lang(id) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.id.xlf
%lang(it) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.it.xlf
%lang(ja) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.ja.xlf
%lang(lb) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.lb.xlf
%lang(nl) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.nl.xlf
%lang(no) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.no.xlf
%lang(pl) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.pl.xlf
%lang(pt_BR) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.pt_BR.xlf
%lang(pt_PT) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.pt_PT.xlf
%lang(ro) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.ro.xlf
%lang(ru) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.ru.xlf
%lang(sk) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.sk.xlf
%lang(sl) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.sl.xlf
%lang(sr@cyrillic) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.sr_Cyrl.xlf
%lang(sr@latin) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.sr_Latn.xlf
%lang(sv) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.sv.xlf
%lang(th) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.th.xlf
%lang(tr) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.tr.xlf
%lang(ua) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.ua.xlf
%lang(vi) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.vi.xlf
%lang(zh_CN) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.zh_CN.xlf
