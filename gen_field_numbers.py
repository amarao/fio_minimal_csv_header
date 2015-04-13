#!/usr/bin/python

csv = open('fio_minimal_header.csv','r').read().strip()
fn = open('fio_field_names.txt','w')
for h in enumerate(csv.split(','), start=1):
    fn.write("%s\t%s\n" % (h[0], h[1]))
del fn
