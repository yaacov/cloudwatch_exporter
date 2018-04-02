Name:           cloudwatch_exporter
Version:        0.1.0
Release:        1%{?dist}
Summary:        Metrics exporter for Amazon AWS CloudWatch
License:        ASL 2.0
URL:            https://github.com/yaacov/cloudwatch_exporter
Source0:        <%name>-<%version>.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local

%description
Metrics exporter for Amazon AWS CloudWatch

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE NOTICE
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Apr 2 2018 Yaacov Zamir <yzamir@redhat.com> - 0.1.0-1
- Initial packaging
