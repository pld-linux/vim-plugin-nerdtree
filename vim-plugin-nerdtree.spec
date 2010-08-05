%define		plugin	nerdtree
Summary:	Vim plugin: NERD tree
Name:		vim-plugin-%{plugin}
Version:	4.10
Release:	1
License:	WTFPL v2 (free, redistributable)
Group:		Applications/Editors/Vim
Source0:	http://www.vim.org/scripts/download_script.php?src_id=11834#/%{plugin}.zip
# Source0-md5:	a15fa66b36c3261e598d93dc830398f6
URL:		http://www.vim.org/scripts/script.php?script_id=1658
# for _vimdatadir
Requires:	vim-rt >= 4:7.2.170
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
The NERD tree allows you to explore your filesystem and to open files
and directories. It presents the filesystem to you in the form of a
tree which you manipulate with the keyboard and/or mouse. It also
allows you to perform simple filesystem operations.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -a . $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_vimdatadir}/doc/*.txt
%{_vimdatadir}/plugin/*.vim
%dir %{_vimdatadir}/nerdtree_plugin
%{_vimdatadir}/nerdtree_plugin/*.vim
