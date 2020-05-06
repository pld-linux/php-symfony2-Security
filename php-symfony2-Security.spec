%define		package	Security
%define		php_min_version 5.3.9
Summary:	Symfony2 Security Component
Name:		php-symfony2-Security
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	1fbd8e2addcead868966b0bd0ae9bc55
URL:		http://symfony.com/doc/2.7/book/security.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(hash)
Requires:	php(json)
Requires:	php(pcre)
Requires:	php(session)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
Requires:	php-symfony2-EventDispatcher >= 2.2
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
%setup -q -n security-%{version}

rm */.gitignore
rm */composer.json
rm */phpunit.xml.dist
for c in Core Guard Http; do
	mv $c/LICENSE LICENSE_$c
	mv $c/README.md README_$c.md
done

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Core/Tests
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Csrf/Tests
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Guard/Tests
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Http/Tests
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README*.md LICENSE*
%dir %{php_data_dir}/Symfony/Component/Security
%{php_data_dir}/Symfony/Component/Security/*.php
%{php_data_dir}/Symfony/Component/Security/Core
%{php_data_dir}/Symfony/Component/Security/Csrf
%{php_data_dir}/Symfony/Component/Security/Guard
%{php_data_dir}/Symfony/Component/Security/Http

%dir %{php_data_dir}/Symfony/Component/Security/Resources
%dir %{php_data_dir}/Symfony/Component/Security/Resources/translations
%lang(ar) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.ar.xlf
%lang(az) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.az.xlf
%lang(bg) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.bg.xlf
%lang(ca) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.ca.xlf
%lang(cs) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.cs.xlf
%lang(da) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.da.xlf
%lang(de) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.de.xlf
%lang(el) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.el.xlf
%lang(en) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.en.xlf
%lang(es) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.es.xlf
%lang(fa) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.fa.xlf
%lang(fr) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.fr.xlf
%lang(gl) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.gl.xlf
%lang(he) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.he.xlf
%lang(hr) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.hr.xlf
%lang(hu) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.hu.xlf
%lang(id) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.id.xlf
%lang(it) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.it.xlf
%lang(ja) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.ja.xlf
%lang(lb) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.lb.xlf
%lang(lt) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.lt.xlf
%lang(lv) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.lv.xlf
%lang(nb) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.nb.xlf
%lang(nl) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.nl.xlf
%lang(nn) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.nn.xlf
%lang(no) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.no.xlf
%lang(pl) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.pl.xlf
%lang(pt_BR) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.pt_BR.xlf
%lang(pt_PT) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.pt_PT.xlf
%lang(ro) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.ro.xlf
%lang(ru) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.ru.xlf
%lang(sk) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.sk.xlf
%lang(sl) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.sl.xlf
%lang(sr@cyrillic) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.sr_Cyrl.xlf
%lang(sr@latin) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.sr_Latn.xlf
%lang(sv) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.sv.xlf
%lang(th) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.th.xlf
%lang(tl) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.tl.xlf
%lang(tr) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.tr.xlf
%lang(ua) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.ua.xlf
%lang(vi) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.vi.xlf
%lang(zh_CN) %{php_data_dir}/Symfony/Component/Security/Resources/translations/security.zh_CN.xlf
