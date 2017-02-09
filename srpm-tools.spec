Name:           srpm-tools
Version:        0.1
Release:        3%{?dist}
Summary:        Generate SRPMs from git

License:        GPLv2+
URL:            https://github.com/praiskup/srpm-tools
Source0:        https://github.com/praiskup/srpm-tools/releases/download/v0.1/srpm-tools-0.1.tar.gz

Requires:       rpmdevtools, rpm-build, git, perl-YAML
BuildArch:      noarch

%description
Set of tools to obtain all sources to build SRPM, which then can be built into
binary RPM.

This is useful for continuous integration/development purposes;  when you e.g.
want to (a) generate SRPM for each "git push" into repository, and (b) then try
to build RPMs.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%license COPYING
%doc README
%_bindir/*
%_libexecdir/*


%changelog
* Thu Feb 09 2017 Pavel Raiskup <praiskup@redhat.com> - 0.1-3
- git is needed for 'git_archive' generator
- add also perl-YAML (config file reading)

* Sat Nov 05 2016 Pavel Raiskup <praiskup@redhat.com> - 0.1-1
- intial release for package review
