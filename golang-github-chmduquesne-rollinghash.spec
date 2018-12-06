Name:           golang-github-chmduquesne-rollinghash
Summary:        Some rolling checksum implementations in go
Version:        4.0.0
Release:        2%{?dist}
License:        MIT and BSD

# https://github.com/chmduquesne/rollinghash
%global repo    rollinghash
%global goipath github.com/chmduquesne/%{repo}
%global tag     v4.0.0

%gometa

URL:            %{gourl}
Source0:        %{gourl}/archive/%{tag}/%{repo}-%{version}.tar.gz

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1

# remove test program; it pulls in extra dependencies
rm -r ./roll


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE.txt
%doc README.md


%changelog
* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0.0-2
- Use standard GitHub SourceURL again for consistency between releases.
- Use forgeautosetup instead of gosetup.

* Thu Sep 13 2018 Fabio Valentini <decathorpe@gmail.com> - 4.0.0-1
- Update to version 4.0.0.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1-5
- Remove test program, it pulls in extra dependencies.

* Thu Aug 16 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1-4
- Update to spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Fabio Valentini <decathorpe@gmail.com> - 3.0.1-1
- Update to version 3.0.1.

* Tue Nov 28 2017 Fabio Valentini <decathorpe@gmail.com> - 3.0.0-1
- Bump to version 3.0.0.

* Thu Nov 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-4.20171121.gite6b39c4
- Bump to commit e6b39c4.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3.1.git043b8fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2.1.git043b8fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-1.1.git043b8fd
- Bump to commit 043b8fdecc9816f0011a056f6d92f9a091ab63dd.
- Adapt provides to upstream changes.

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.2-0.1.git56b51d0
- First package for Fedora

