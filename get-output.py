import sys
import xml.dom.minidom
from sickle import Sickle

ENDPOINT = 'https://durham-repository.worktribe.com/oaiprovider'
sickle = Sickle(ENDPOINT)

prefix = 'oai:durham-repository.worktribe.com:'
TESTID = '1168839'
rioxx = 'rioxx.xml'
dc    = 'dc.xml'

fh1 = open(rioxx, 'w')
fh2 = open(dc, 'w')



def get_rioxx(repo_id):
    id = prefix + repo_id
    r = sickle.GetRecord(identifier=id, metadataPrefix='rioxx')
    print("Got record in rioxx format")
    pp = pprint(r)
    fh1.write(pp)
    fh1.close()

def get_dc(repo_id):
    id = prefix + repo_id
    r = sickle.GetRecord(identifier=id, metadataPrefix='oai_dc')
    print("Got record in oai_dc format")
    pp = pprint(r)
    fh2.write(pp)
    fh2.close()

def pprint(x):
    dom = xml.dom.minidom.parseString(str(x))
    pretty = dom.toprettyxml()
#    print(pretty) #for testing
    return pretty
    
def main():
    try:
        get_rioxx(sys.argv[1])
        get_dc(sys.argv[1])
    except IndexError:
        print("Usage:\n", sys.argv[0], "WorktribeOutputID")

if __name__ == '__main__':
    sys.exit(main())  #
