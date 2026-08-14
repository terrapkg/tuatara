set -x

dirs=$2
export p="{\"id\":\"$5\",\"ver\":\"%v\",\"rel\":\"%r\",\"arch\":\"$4\",\"dirs\":\"$dirs\",\"succ\":$1,\"commit\":\"$7\"}"

if [[ $1 == false ]]; then
	d=${p/\%v/?}
	d=${d/\%r/?}
	curl -H "Authorization: Bearer $6" https://madoguchi.fyralabs.com/ci5/tuatara-$3/builds/f -X PUT -H "Content-Type: application/json" -d "$d" --fail-with-body
	exit 0
fi

for f in anda-build/rpm/rpms/*; do
	n=$(rpm -q --qf='%{name}' $f)
	v=$(rpm -q --qf='%{version}' $f)
	r=$(rpm -q --qf='%{release}' $f)
	d=${p/\%v/$v}
	d=${d/\%r/$r}
	curl -H "Authorization: Bearer $6" https://madoguchi.fyralabs.com/ci5/tuatara-$3/builds/$n -X PUT -H "Content-Type: application/json" -d $d --fail-with-body
done
