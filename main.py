# -*- encoding: utf-8 -*-
from converter import CountryConverter
import pprint as p

dbname="ademe (copia).db"
dbtable="COUNTRY"
dbcolumnID="rowid"
dbcolumnName="country"

# IF (write = False) you will see the exceptions before write anything
write=False
## And with this info, you could add those exceptions to countries_alternatives.txt

inst = CountryConverter(dbname,dbtable,dbcolumnID,dbcolumnName)

ISO=inst.getCountries("countries_ISO3166.txt")
Alternatives=inst.getCountries("countries_alternatives.txt")
inst.createInvertedDicts(ISO,Alternatives)

fails=inst.convertAll(write)

print "\nfinish\n---------------------\n"
print "failures:"
p.pprint(fails)
print
for i in fails:
	print fails[i]+" :"
	print '\tUPDATE '+dbtable+' SET '+dbcolumnName+'="¿¿CountryCode??" WHERE '+dbcolumnID+'='+`i`
	print
