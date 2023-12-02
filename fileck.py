import sys
import xml.dom.minidom
from sickle import Sickle

ENDPOINT = 'https://durham-repository.worktribe.com/oaiprovider'
FILE = '<dc:identifier>https://durham-repository.worktribe.com/file'
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
    found = r.count(FILE)
    if found > 1:
        ctr['file'] += 1
        fh2.write("Found record with multiple files " + id)
    ctr['total'] += 1


def pprint(x):
    dom = xml.dom.minidom.parseString(str(x))
    pretty = dom.toprettyxml()
#    print(pretty) #for testing
    return pretty
    
def main():
    count = {'file': 0, 'total': 0}
    try:
        with open(sys.argv[1]) as f:
            for oid in f:
                rec = get_rioxx(oid.rstrip())
                if rec is not None:
                    analyse(rec, oid, count)
                if count['total'] % 1000 == 0:
                    print(str(count['total']) + " outputs processed")
        print("Total outputs analysed: "      + str(count['total']))
        print("Outputs with multiple files: " + str(count['file']))

        
    except IndexError:
        print("Usage:\n", sys.argv[0], "FileContainingWorktribeOutputIDs")
    fh1.close()
    fh2.close()


if __name__ == '__main__':
    sys.exit(main())  #
