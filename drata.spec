Name:       drata-agent
Version:    3.5.0
Release:    1
Summary:    Drata Agent repackaged in RPM
License:    © 2023 Drata Inc. All rights reserved.
Vendor:     Drata Inc. <drata@drata.com>
Url:        https://github.com/drata/the-agent
Source0:    https://github.com/drata/agent-releases/releases/download/v%{version}/Drata-Agent-linux.deb
BuildRequires:  binutils
AutoReqProv:    no
Provides:   drata-agent

%description
The Drata Agent is a light-weight tray-application that runs in the background, reporting important read-only data to Drata about your machine’s state for compliance tracking.

%prep
mkdir -p "control" "data"
ar x %{_sourcedir}/Drata-Agent-linux.deb --output=%{_builddir}
cd control; tar xf ../control.tar.*
cd ../data; tar xf ../data.tar.*
cd ..;
rm *.tar.* debian-binary ;

%install
mv data/usr %{buildroot}
mv data/opt %{buildroot}
ls %{buildroot}

%files
/opt/
/usr/

%changelog
* Wed Jan 17 2024 Guilherme Cardoso <gjc@ua.pt> 3.5.0
- First version. Repackage *.deb as *.rpm
