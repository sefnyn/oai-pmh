import sys
import xml.dom.minidom
from sickle import Sickle

ENDPOINT = 'https://durham-repository.worktribe.com/oaiprovider'
sickle = Sickle(ENDPOINT)

prefix = 'oai:durham-repository.worktribe.com:'
rioxx  = 'rioxx.xml'
log    = 'logfile.log'

fh1 = open(rioxx, 'w')
fh2 = open(log, 'w')


def get_rioxx(repo_id):
    longid = prefix + repo_id
    try:
        r = sickle.GetRecord(identifier=longid, metadataPrefix='rioxx')
#        print("Got record " + repo_id + " in rioxx format")
        pp = pprint(r)
        fh1.write(pp)
        return pp
    except:
        print("Skipping invalid output ID")
        fh2.write("Skipping invalid output ID " + repo_id + "\n")
        return None

def analyse(r, id, ctr):
    if '<ali:license_ref' in r:
        ctr['licence'] += 1
    if '<dc:identifier' in r:
        ctr['ident'] += 1
    if '<dc:language' in r:
        ctr['lang'] += 1
    if '<dcterms:dateAccepted' in r:
        ctr['dateacc'] += 1
    if '<rioxxterms:project' in r:
        ctr['project'] += 1
    if '<rioxxterms:publication_date' in r:
        ctr['pubdate'] += 1
    if '<rioxxterms:type' in r:
        ctr['type'] += 1
    if '<rioxxterms:version>' in r:
        ctr['version'] += 1
    if '<rioxxterms:version_of_record>' in r:
        ctr['doi'] += 1
    ctr['total'] += 1


def pprint(x):
    dom = xml.dom.minidom.parseString(str(x))
    pretty = dom.toprettyxml()
#    print(pretty) #for testing
    return pretty
    
def main():
    count = {'licence': 0, 'ident': 0, 'lang': 0, 'dateacc': 0, 'project': 0, 'pubdate': 0,  'type': 0, 'version': 0,  'doi': 0, 'total': 0}
    try:
        with open(sys.argv[1]) as f:
            for oid in f:
                rec = get_rioxx(oid.rstrip())
                if rec is not None:
                    analyse(rec, oid, count)
                if count['total'] % 1000 == 0:
                    print(str(count['total'])      + " outputs processed")
        print("Total outputs analysed: "           + str(count['total']))
        print("Outputs with a LICENCE: "           + str(count['licence']))
        print("Outputs with an IDENTIFIER: "       + str(count['ident']))
        print("Outputs with a LANGUAGE: "          + str(count['lang']))
        print("Outputs with a DATEACCEPTED: "      + str(count['dateacc']))
        print("Outputs with a PROJECT (FUNDER): "  + str(count['project']))
        print("Outputs with a PUBLICATION DATE: "  + str(count['pubdate']))
        print("Outputs with a TYPE: "              + str(count['type']))
        print("Outputs with a VERSION: "           + str(count['version']))
        print("Outputs with a DOI: "               + str(count['doi']))

        
    except IndexError:
        print("Usage:\n", sys.argv[0], "FileContainingWorktribeOutputIDs")
    fh1.close()
    fh2.close()


if __name__ == '__main__':
    sys.exit(main())  #
